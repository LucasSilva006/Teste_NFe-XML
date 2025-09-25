import xml.etree.ElementTree as ET
import pandas as pd
import os
import math
from datetime import datetime, timedelta

def processar_nfs():
    """Processa todas as NFes da pasta nfs/"""
    pasta = "nfs"
    carencia = 30
    dados = []
    
    print("🔄 Iniciando processamento das NFes...")
    
    # Verificar se pasta existe
    if not os.path.exists(pasta):
        print("❌ Pasta 'nfs' não encontrada!")
        print("💡 Crie a pasta 'nfs' e coloque os XMLs dentro dela")
        return
    
    # Listar arquivos XML
    arquivos_xml = [f for f in os.listdir(pasta) if f.endswith('.xml')]
    
    if not arquivos_xml:
        print("❌ Nenhum arquivo XML encontrado na pasta 'nfs'!")
        return
    
    print(f"📁 Encontrados {len(arquivos_xml)} arquivos XML")
    
    # Processar cada XML
    for arquivo in arquivos_xml:
        print(f"📄 Processando: {arquivo}")
        
        try:
            caminho = os.path.join(pasta, arquivo)
            tree = ET.parse(caminho)
            root = tree.getroot()

            # Buscar data de emissão
            data_emissao_tag = root.find(".//{http://www.portalfiscal.inf.br/nfe}dEmi")
            if data_emissao_tag is None:
                # Tentar sem namespace
                data_emissao_tag = root.find(".//dEmi")
            
            if data_emissao_tag is None:
                print(f"⚠️  Data de emissão não encontrada em {arquivo}")
                continue
                
            try:
                data_emissao = datetime.strptime(data_emissao_tag.text, "%Y-%m-%d")
            except ValueError:
                print(f"⚠️  Formato de data inválido em {arquivo}: {data_emissao_tag.text}")
                continue
            
            data_limite = data_emissao + timedelta(days=carencia)
            
            # Buscar produtos
            produtos_encontrados = 0
            
            # Tentar com namespace
            produtos = root.findall(".//{http://www.portalfiscal.inf.br/nfe}det")
            if not produtos:
                # Tentar sem namespace
                produtos = root.findall(".//det")
            
            for det in produtos:
                # Buscar dados do produto
                prod = det.find("{http://www.portalfiscal.inf.br/nfe}prod")
                if prod is None:
                    prod = det.find("prod")
                
                if prod is None:
                    continue
                
                # Extrair nome do produto
                nome_tag = prod.find("{http://www.portalfiscal.inf.br/nfe}xProd")
                if nome_tag is None:
                    nome_tag = prod.find("xProd")
                
                # Extrair quantidade
                qtd_tag = prod.find("{http://www.portalfiscal.inf.br/nfe}qCom")
                if qtd_tag is None:
                    qtd_tag = prod.find("qCom")
                
                if nome_tag is not None and qtd_tag is not None:
                    try:
                        nome = nome_tag.text.strip()
                        qtd = float(qtd_tag.text)
                        
                        dados.append({
                            "Produto": nome,
                            "Quantidade": qtd,
                            "Data_Faturamento": data_emissao,
                            "Data_Limite": data_limite,
                            "Arquivo": arquivo.replace('.xml', '')
                        })
                        produtos_encontrados += 1
                        
                    except (ValueError, TypeError) as e:
                        print(f"⚠️  Erro ao processar produto em {arquivo}: {e}")
                        continue
            
            print(f"   ✅ {produtos_encontrados} produtos extraídos")
            
        except ET.ParseError as e:
            print(f"❌ Erro XML em {arquivo}: {e}")
            continue
        except Exception as e:
            print(f"❌ Erro geral em {arquivo}: {e}")
            continue
    
    if not dados:
        print("❌ Nenhum produto foi extraído dos XMLs!")
        print("💡 Verifique se os XMLs estão no formato correto")
        return
    
    print(f"\n📊 RESUMO DO PROCESSAMENTO:")
    print(f"   • Total de produtos extraídos: {len(dados)}")
    print(f"   • Produtos únicos: {len(set(d['Produto'] for d in dados))}")
    
    return dados

def calcular_plano_semanal(dados):
    """Calcula distribuição semanal de produção"""
    if not dados:
        return pd.DataFrame()
    
    print("🔧 Calculando plano de produção semanal...")
    
    plano_semanal = []
    
    for item in dados:
        # Calcular dias disponíveis
        dias_total = (item["Data_Limite"] - item["Data_Faturamento"]).days
        semanas = max(1, math.ceil(dias_total / 7))
        
        # Dividir quantidade por semanas
        qtd_por_semana = math.ceil(item["Quantidade"] / semanas)
        qtd_restante = item["Quantidade"]
        
        data_inicio = item["Data_Faturamento"]
        
        for semana in range(1, semanas + 1):
            qtd_esta_semana = min(qtd_por_semana, qtd_restante)
            
            if qtd_esta_semana <= 0:
                break
            
            data_fim_semana = min(
                data_inicio + timedelta(days=6),
                item["Data_Limite"]
            )
            
            plano_semanal.append({
                "Produto": item["Produto"],
                "Semana": f"Semana {semana}",
                "Quantidade": int(qtd_esta_semana),
                "Data_Faturamento": item["Data_Faturamento"].strftime("%d/%m/%Y"),
                "Data_Limite": item["Data_Limite"].strftime("%d/%m/%Y"),
                "Periodo_Semana": f"{data_inicio.strftime('%d/%m')} - {data_fim_semana.strftime('%d/%m')}",
                "NF_Origem": item["Arquivo"]
            })
            
            qtd_restante -= qtd_esta_semana
            data_inicio += timedelta(days=7)
    
    return pd.DataFrame(plano_semanal)

def consolidar_plano(df_plano):
    """Consolida plano por produto e semana"""
    if df_plano.empty:
        return pd.DataFrame()
    
    print("📋 Consolidando plano por produto e semana...")
    
    # Consolidar por produto e período
    df_consolidado = df_plano.groupby([
        "Produto", "Semana", "Periodo_Semana"
    ]).agg({
        "Quantidade": "sum",
        "Data_Faturamento": "first",
        "Data_Limite": "max",
        "NF_Origem": lambda x: ", ".join(sorted(set(x)))
    }).reset_index()
    
    return df_consolidado

def gerar_planilha(df_consolidado, df_detalhado):
    """Gera planilha Excel com resultado"""
    if df_consolidado.empty:
        print("❌ Não há dados para gerar planilha")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"plano_producao_semanal_{timestamp}.xlsx"
    
    print(f"💾 Gerando planilha: {nome_arquivo}")
    
    try:
        with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:
            # Aba principal: Plano consolidado
            df_consolidado.to_excel(writer, sheet_name='Plano de Produção', index=False)
            
            # Aba: Detalhamento
            if not df_detalhado.empty:
                df_detalhado.to_excel(writer, sheet_name='Detalhamento', index=False)
            
            # Aba: Resumo por produto
            resumo = df_consolidado.groupby('Produto').agg({
                'Quantidade': 'sum',
                'Semana': 'count'
            }).rename(columns={'Semana': 'Total_Semanas'}).reset_index()
            resumo = resumo.sort_values('Quantidade', ascending=False)
            resumo.to_excel(writer, sheet_name='Resumo por Produto', index=False)
        
        print(f"✅ Planilha salva: {nome_arquivo}")
        return nome_arquivo
        
    except Exception as e:
        print(f"❌ Erro ao salvar planilha: {e}")
        return None

def exibir_resumo(df_consolidado):
    """Exibe resumo do plano gerado"""
    if df_consolidado.empty:
        return
    
    print("\n" + "="*60)
    print("📈 PLANO DE PRODUÇÃO SEMANAL - RESUMO")
    print("="*60)
    
    total_produtos = df_consolidado['Produto'].nunique()
    total_semanas = df_consolidado['Semana'].nunique()
    qtd_total = df_consolidado['Quantidade'].sum()
    
    print(f"📦 Produtos únicos: {total_produtos}")
    print(f"📅 Total de semanas: {total_semanas}")
    print(f"🔢 Quantidade total a produzir: {qtd_total:,.0f} unidades")
    
    # Top 5 produtos por volume
    top_produtos = df_consolidado.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(5)
    
    print(f"\n🏆 TOP 5 PRODUTOS (maior volume):")
    for i, (produto, qtd) in enumerate(top_produtos.items(), 1):
        print(f"   {i}. {produto}: {qtd:,.0f} unidades")
    
    # Distribuição semanal
    por_semana = df_consolidado.groupby('Semana')['Quantidade'].sum().sort_index()
    print(f"\n📊 DISTRIBUIÇÃO SEMANAL:")
    for semana, qtd in por_semana.items():
        print(f"   {semana}: {qtd:,.0f} unidades")
    
    print("="*60)

def main():
    """Função principal do sistema PCP"""
    print("🚀 SISTEMA PCP - PLANEJAMENTO DE PRODUÇÃO SEMANAL")
    print("="*60)
    
    try:
        # 1. Processar NFes
        dados = processar_nfs()
        if not dados:
            return
        
        # 2. Calcular plano semanal
        df_detalhado = calcular_plano_semanal(dados)
        if df_detalhado.empty:
            print("❌ Erro ao calcular plano semanal")
            return
        
        # 3. Consolidar plano
        df_consolidado = consolidar_plano(df_detalhado)
        if df_consolidado.empty:
            print("❌ Erro ao consolidar plano")
            return
        
        # 4. Gerar planilha
        nome_arquivo = gerar_planilha(df_consolidado, df_detalhado)
        
        # 5. Exibir resumo
        exibir_resumo(df_consolidado)
        
        if nome_arquivo:
            print(f"\n🎯 SUCESSO! Abra o arquivo '{nome_arquivo}' para ver o plano completo")
            print("💡 Use a aba 'Plano de Produção' para organizar a produção semanal")
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")
        print("💡 Verifique se:")
        print("   • A pasta 'nfs' existe")
        print("   • Há arquivos XML na pasta")
        print("   • Os XMLs estão no formato correto")

if __name__ == "__main__":
    main()