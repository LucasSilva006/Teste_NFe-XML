import os
from datetime import datetime, timedelta

def criar_3_xmls_simples():
    """Cria 3 XMLs simples para teste do sistema PCP"""
    
    # Criar pasta nfs se não existir
    os.makedirs("nfs", exist_ok=True)
    
    # Datas dos últimos dias (simulando vendas recentes)
    hoje = datetime.now()
    data1 = (hoje - timedelta(days=3)).strftime("%Y-%m-%d")
    data2 = (hoje - timedelta(days=7)).strftime("%Y-%m-%d") 
    data3 = (hoje - timedelta(days=12)).strftime("%Y-%m-%d")
    
    # ========== XML 1 - NF 3001 ==========
    xml1 = f'''<?xml version="1.0" encoding="UTF-8"?>
<nfeProc>
    <NFe>
        <infNFe>
            <ide>
                <nNF>3001</nNF>
                <dEmi>{data1}</dEmi>
            </ide>
            
            <det nItem="1">
                <prod>
                    <xProd>PARAFUSO ALLEN M6X25</xProd>
                    <qCom>500.00</qCom>
                </prod>
            </det>
            
            <det nItem="2">
                <prod>
                    <xProd>CHAVE ALLEN 6MM</xProd>
                    <qCom>20.00</qCom>
                </prod>
            </det>
        </infNFe>
    </NFe>
</nfeProc>'''

    # ========== XML 2 - NF 3002 ==========
    xml2 = f'''<?xml version="1.0" encoding="UTF-8"?>
<nfeProc>
    <NFe>
        <infNFe>
            <ide>
                <nNF>3002</nNF>
                <dEmi>{data2}</dEmi>
            </ide>
            
            <det nItem="1">
                <prod>
                    <xProd>BARRA ROSCADA M8 - 1M</xProd>
                    <qCom>100.00</qCom>
                </prod>
            </det>
            
            <det nItem="2">
                <prod>
                    <xProd>PARAFUSO ALLEN M6X25</xProd>
                    <qCom>300.00</qCom>
                </prod>
            </det>
            
            <det nItem="3">
                <prod>
                    <xProd>SOLDA MIG 0.8MM</xProd>
                    <qCom>50.00</qCom>
                </prod>
            </det>
        </infNFe>
    </NFe>
</nfeProc>'''

    # ========== XML 3 - NF 3003 ==========
    xml3 = f'''<?xml version="1.0" encoding="UTF-8"?>
<nfeProc>
    <NFe>
        <infNFe>
            <ide>
                <nNF>3003</nNF>
                <dEmi>{data3}</dEmi>
            </ide>
            
            <det nItem="1">
                <prod>
                    <xProd>ELETRODO 2.5MM</xProd>
                    <qCom>200.00</qCom>
                </prod>
            </det>
            
            <det nItem="2">
                <prod>
                    <xProd>DISCO CORTE 4.5 POLEGADAS</xProd>
                    <qCom>80.00</qCom>
                </prod>
            </det>
            
            <det nItem="3">
                <prod>
                    <xProd>BARRA ROSCADA M8 - 1M</xProd>
                    <qCom>75.00</qCom>
                </prod>
            </det>
            
            <det nItem="4">
                <prod>
                    <xProd>PARAFUSO ALLEN M6X25</xProd>
                    <qCom>150.00</qCom>
                </prod>
            </det>
        </infNFe>
    </NFe>
</nfeProc>'''

    # Salvar os arquivos
    arquivos_criados = []
    
    # Arquivo 1
    nome1 = f"NFe_003001_{data1.replace('-', '')}.xml"
    with open(f"nfs/{nome1}", 'w', encoding='utf-8') as f:
        f.write(xml1)
    arquivos_criados.append(nome1)
    
    # Arquivo 2
    nome2 = f"NFe_003002_{data2.replace('-', '')}.xml"
    with open(f"nfs/{nome2}", 'w', encoding='utf-8') as f:
        f.write(xml2)
    arquivos_criados.append(nome2)
    
    # Arquivo 3
    nome3 = f"NFe_003003_{data3.replace('-', '')}.xml"
    with open(f"nfs/{nome3}", 'w', encoding='utf-8') as f:
        f.write(xml3)
    arquivos_criados.append(nome3)
    
    print("🎯 3 XMLs simples criados com sucesso!")
    print("=" * 55)
    print("📁 Pasta: nfs/")
    print()
    
    print(f"📄 {nome1}")
    print(f"   📅 Data: {data1} ({(datetime.now() - datetime.strptime(data1, '%Y-%m-%d')).days} dias atrás)")
    print("   📦 Produtos: Parafuso Allen M6 (500un), Chave Allen 6mm (20un)")
    print()
    
    print(f"📄 {nome2}")
    print(f"   📅 Data: {data2} ({(datetime.now() - datetime.strptime(data2, '%Y-%m-%d')).days} dias atrás)")
    print("   📦 Produtos: Barra Roscada M8 (100un), Parafuso Allen M6 (300un), Solda MIG (50un)")
    print()
    
    print(f"📄 {nome3}")
    print(f"   📅 Data: {data3} ({(datetime.now() - datetime.strptime(data3, '%Y-%m-%d')).days} dias atrás)")
    print("   📦 Produtos: Eletrodo 2.5mm (200un), Disco Corte (80un), Barra Roscada M8 (75un), Parafuso Allen M6 (150un)")
    print()
    
    print("🔍 Cenários incluídos:")
    print("   ✅ Produto repetido: 'PARAFUSO ALLEN M6X25' em todas as 3 NFs")
    print("   ✅ Produto repetido: 'BARRA ROSCADA M8 - 1M' em 2 NFs")
    print("   ✅ 3 datas diferentes (3, 7 e 12 dias atrás)")
    print("   ✅ Quantidades variadas para testar consolidação")
    print()
    
    # Calcular totais consolidados
    total_parafuso = 500 + 300 + 150
    total_barra = 100 + 75
    
    print("📊 TOTAIS CONSOLIDADOS (o que o sistema vai calcular):")
    print(f"   🔩 PARAFUSO ALLEN M6X25: {total_parafuso} unidades")
    print(f"   📏 BARRA ROSCADA M8 - 1M: {total_barra} unidades")
    print(f"   🔧 CHAVE ALLEN 6MM: 20 unidades")
    print(f"   ⚡ SOLDA MIG 0.8MM: 50 unidades")
    print(f"   🔌 ELETRODO 2.5MM: 200 unidades")
    print(f"   ⚙️  DISCO CORTE 4.5 POLEGADAS: 80 unidades")
    print()
    
    print("🚀 Agora execute: python index.py")
    
    return arquivos_criados

if __name__ == "__main__":
    criar_3_xmls_simples()