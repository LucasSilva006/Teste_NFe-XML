import os
from datetime import datetime, timedelta

def criar_xmls_teste():
    """Cria 2 XMLs de teste para o sistema PCP"""
    
    # Criar pasta nfs se não existir
    os.makedirs("nfs", exist_ok=True)
    
    # Data de hoje menos alguns dias (simulando vendas recentes)
    hoje = datetime.now()
    data_nf1 = (hoje - timedelta(days=5)).strftime("%Y-%m-%d")
    data_nf2 = (hoje - timedelta(days=8)).strftime("%Y-%m-%d")
    
    # ========== XML 1 - NF com produtos de fixação ==========
    xml1_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe">
    <NFe>
        <infNFe Id="NFe00000100001">
            <ide>
                <cUF>35</cUF>
                <cNF>00001001</cNF>
                <natOp>Venda</natOp>
                <mod>55</mod>
                <serie>1</serie>
                <nNF>1001</nNF>
                <dhEmi>{data_nf1}T10:30:00-03:00</dhEmi>
                <dEmi>{data_nf1}</dEmi>
                <tpNF>1</tpNF>
                <idDest>2</idDest>
                <cMunFG>2611606</cMunFG>
                <tpImp>1</tpImp>
                <tpEmis>1</tpEmis>
                <cDV>1</cDV>
                <tpAmb>1</tpAmb>
                <finNFe>1</finNFe>
                <indFinal>1</indFinal>
                <indPres>1</indPres>
            </ide>
            
            <emit>
                <CNPJ>12345678000190</CNPJ>
                <xNome>METALURGICA EXEMPLO LTDA</xNome>
                <xFant>Metalurgica Exemplo</xFant>
                <enderEmit>
                    <xLgr>RUA DA INDUSTRIA</xLgr>
                    <nro>500</nro>
                    <xBairro>DISTRITO INDUSTRIAL</xBairro>
                    <cMun>2611606</cMun>
                    <xMun>VITORIA DE SANTO ANTAO</xMun>
                    <UF>PE</UF>
                    <CEP>55608000</CEP>
                </enderEmit>
                <IE>032141840</IE>
            </emit>
            
            <dest>
                <CNPJ>98765432000111</CNPJ>
                <xNome>CONSTRUCOES ABC LTDA</xNome>
                <enderDest>
                    <xLgr>AV PRINCIPAL</xLgr>
                    <nro>1200</nro>
                    <xBairro>CENTRO</xBairro>
                    <cMun>2611606</cMun>
                    <xMun>VITORIA DE SANTO ANTAO</xMun>
                    <UF>PE</UF>
                    <CEP>55608100</CEP>
                </enderDest>
                <IE>032445671</IE>
            </dest>
            
            <det nItem="1">
                <prod>
                    <cProd>001001</cProd>
                    <cEAN></cEAN>
                    <xProd>PARAFUSO PHILLIPS M8X30 ZINCADO</xProd>
                    <NCM>73181500</NCM>
                    <CFOP>5102</CFOP>
                    <uCom>PC</uCom>
                    <qCom>800.00</qCom>
                    <vUnCom>0.75</vUnCom>
                    <vProd>600.00</vProd>
                    <cEANTrib></cEANTrib>
                    <uTrib>PC</uTrib>
                    <qTrib>800.00</qTrib>
                    <vUnTrib>0.75</vUnTrib>
                    <indTot>1</indTot>
                </prod>
                <imposto>
                    <ICMS>
                        <ICMS00>
                            <orig>0</orig>
                            <CST>00</CST>
                            <modBC>3</modBC>
                            <vBC>600.00</vBC>
                            <pICMS>18.00</pICMS>
                            <vICMS>108.00</vICMS>
                        </ICMS00>
                    </ICMS>
                </imposto>
            </det>
            
            <det nItem="2">
                <prod>
                    <cProd>001002</cProd>
                    <cEAN></cEAN>
                    <xProd>PORCA SEXTAVADA M8 ZINCADA</xProd>
                    <NCM>73181600</NCM>
                    <CFOP>5102</CFOP>
                    <uCom>PC</uCom>
                    <qCom>800.00</qCom>
                    <vUnCom>0.35</vUnCom>
                    <vProd>280.00</vProd>
                    <cEANTrib></cEANTrib>
                    <uTrib>PC</uTrib>
                    <qTrib>800.00</qTrib>
                    <vUnTrib>0.35</vUnTrib>
                    <indTot>1</indTot>
                </prod>
                <imposto>
                    <ICMS>
                        <ICMS00>
                            <orig>0</orig>
                            <CST>00</CST>
                            <modBC>3</modBC>
                            <vBC>280.00</vBC>
                            <pICMS>18.00</pICMS>
                            <vICMS>50.40</vICMS>
                        </ICMS00>
                    </ICMS>
                </imposto>
            </det>
            
            <det nItem="3">
                <prod>
                    <cProd>001003</cProd>
                    <cEAN></cEAN>
                    <xProd>ARRUELA LISA M8 ZINCADA</xProd>
                    <NCM>73269090</NCM>
                    <CFOP>5102</CFOP>
                    <uCom>PC</uCom>
                    <qCom>1200.00</qCom>
                    <vUnCom>0.15</vUnCom>
                    <vProd>180.00</vProd>
                    <cEANTrib></cEANTrib>
                    <uTrib>PC</uTrib>
                    <qTrib>1200.00</qTrib>
                    <vUnTrib>0.15</vUnTrib>
                    <indTot>1</indTot>
                </prod>
                <imposto>
                    <ICMS>
                        <ICMS00>
                            <orig>0</orig>
                            <CST>00</CST>
                            <modBC>3</modBC>
                            <vBC>180.00</vBC>
                            <pICMS>18.00</pICMS>
                            <vICMS>32.40</vICMS>
                        </ICMS00>
                    </ICMS>
                </imposto>
            </det>
            
            <total>
                <ICMSTot>
                    <vBC>1060.00</vBC>
                    <vICMS>190.80</vICMS>
                    <vICMSDeson>0.00</vICMSDeson>
                    <vBCST>0.00</vBCST>
                    <vST>0.00</vST>
                    <vProd>1060.00</vProd>
                    <vFrete>0.00</vFrete>
                    <vSeg>0.00</vSeg>
                    <vDesc>0.00</vDesc>
                    <vII>0.00</vII>
                    <vIPI>0.00</vIPI>
                    <vPIS>0.00</vPIS>
                    <vCOFINS>0.00</vCOFINS>
                    <vOutro>0.00</vOutro>
                    <vNF>1060.00</vNF>
                </ICMSTot>
            </total>
            
            <transp>
                <modFrete>1</modFrete>
            </transp>
            
            <infAdic>
                <infCpl>PEDIDO CLIENTE: PED-2025-001 | PRAZO ENTREGA: 30 DIAS</infCpl>
            </infAdic>
        </infNFe>
    </NFe>
</nfeProc>'''

    # ========== XML 2 - NF com produtos estruturais ==========
    xml2_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe">
    <NFe>
        <infNFe Id="NFe00000200001">
            <ide>
                <cUF>35</cUF>
                <cNF>00002001</cNF>
                <natOp>Venda</natOp>
                <mod>55</mod>
                <serie>1</serie>
                <nNF>2001</nNF>
                <dhEmi>{data_nf2}T14:15:00-03:00</dhEmi>
                <dEmi>{data_nf2}</dEmi>
                <tpNF>1</tpNF>
                <idDest>2</idDest>
                <cMunFG>2611606</cMunFG>
                <tpImp>1</tpImp>
                <tpEmis>1</tpEmis>
                <cDV>1</cDV>
                <tpAmb>1</tpAmb>
                <finNFe>1</finNFe>
                <indFinal>1</indFinal>
                <indPres>1</indPres>
            </ide>
            
            <emit>
                <CNPJ>12345678000190</CNPJ>
                <xNome>METALURGICA EXEMPLO LTDA</xNome>
                <xFant>Metalurgica Exemplo</xFant>
                <enderEmit>
                    <xLgr>RUA DA INDUSTRIA</xLgr>
                    <nro>500</nro>
                    <xBairro>DISTRITO INDUSTRIAL</xBairro>
                    <cMun>2611606</cMun>
                    <xMun>VITORIA DE SANTO ANTAO</xMun>
                    <UF>PE</UF>
                    <CEP>55608000</CEP>
                </enderEmit>
                <IE>032141840</IE>
            </emit>
            
            <dest>
                <CNPJ>11223344000155</CNPJ>
                <xNome>ESTRUTURAS METALICAS XYZ LTDA</xNome>
                <enderDest>
                    <xLgr>RUA DAS OFICINAS</xLgr>
                    <nro>850</nro>
                    <xBairro>INDUSTRIAL</xBairro>
                    <cMun>2611606</cMun>
                    <xMun>VITORIA DE SANTO ANTAO</xMun>
                    <UF>PE</UF>
                    <CEP>55608200</CEP>
                </enderDest>
                <IE>032998877</IE>
            </dest>
            
            <det nItem="1">
                <prod>
                    <cProd>002001</cProd>
                    <cEAN></cEAN>
                    <xProd>CHAPA ACO 1020 ESP 3MM 1000X2000</xProd>
                    <NCM>72085100</NCM>
                    <CFOP>5102</CFOP>
                    <uCom>PC</uCom>
                    <qCom>25.00</qCom>
                    <vUnCom>85.50</vUnCom>
                    <vProd>2137.50</vProd>
                    <cEANTrib></cEANTrib>
                    <uTrib>PC</uTrib>
                    <qTrib>25.00</qTrib>
                    <vUnTrib>85.50</vUnTrib>
                    <indTot>1</indTot>
                </prod>
                <imposto>
                    <ICMS>
                        <ICMS00>
                            <orig>0</orig>
                            <CST>00</CST>
                            <modBC>3</modBC>
                            <vBC>2137.50</vBC>
                            <pICMS>18.00</pICMS>
                            <vICMS>384.75</vICMS>
                        </ICMS00>
                    </ICMS>
                </imposto>
            </det>
            
            <det nItem="2">
                <prod>
                    <cProd>002002</cProd>
                    <cEAN></cEAN>
                    <xProd>TUBO QUADRADO 40X40X2MM - 6M</xProd>
                    <NCM>73063090</NCM>
                    <CFOP>5102</CFOP>
                    <uCom>PC</uCom>
                    <qCom>15.00</qCom>
                    <vUnCom>42.80</vUnCom>
                    <vProd>642.00</vProd>
                    <cEANTrib></cEANTrib>
                    <uTrib>PC</uTrib>
                    <qTrib>15.00</qTrib>
                    <vUnTrib>42.80</vUnTrib>
                    <indTot>1</indTot>
                </prod>
                <imposto>
                    <ICMS>
                        <ICMS00>
                            <orig>0</orig>
                            <CST>00</CST>
                            <modBC>3</modBC>
                            <vBC>642.00</vBC>
                            <pICMS>18.00</pICMS>
                            <vICMS>115.56</vICMS>
                        </ICMS00>
                    </ICMS>
                </imposto>
            </det>
            
            <det nItem="3">
                <prod>
                    <cProd>001001</cProd>
                    <cEAN></cEAN>
                    <xProd>PARAFUSO PHILLIPS M8X30 ZINCADO</xProd>
                    <NCM>73181500</NCM>
                    <CFOP>5102</CFOP>
                    <uCom>PC</uCom>
                    <qCom>300.00</qCom>
                    <vUnCom>0.75</vUnCom>
                    <vProd>225.00</vProd>
                    <cEANTrib></cEANTrib>
                    <uTrib>PC</uTrib>
                    <qTrib>300.00</qTrib>
                    <vUnTrib>0.75</vUnTrib>
                    <indTot>1</indTot>
                </prod>
                <imposto>
                    <ICMS>
                        <ICMS00>
                            <orig>0</orig>
                            <CST>00</CST>
                            <modBC>3</modBC>
                            <vBC>225.00</vBC>
                            <pICMS>18.00</pICMS>
                            <vICMS>40.50</vICMS>
                        </ICMS00>
                    </ICMS>
                </imposto>
            </det>
            
            <total>
                <ICMSTot>
                    <vBC>3004.50</vBC>
                    <vICMS>540.81</vICMS>
                    <vICMSDeson>0.00</vICMSDeson>
                    <vBCST>0.00</vBCST>
                    <vST>0.00</vST>
                    <vProd>3004.50</vProd>
                    <vFrete>0.00</vFrete>
                    <vSeg>0.00</vSeg>
                    <vDesc>0.00</vDesc>
                    <vII>0.00</vII>
                    <vIPI>0.00</vIPI>
                    <vPIS>0.00</vPIS>
                    <vCOFINS>0.00</vCOFINS>
                    <vOutro>0.00</vOutro>
                    <vNF>3004.50</vNF>
                </ICMSTot>
            </total>
            
            <transp>
                <modFrete>1</modFrete>
            </transp>
            
            <infAdic>
                <infCpl>PEDIDO CLIENTE: PED-2025-002 | PROJETO: GALPAO INDUSTRIAL</infCpl>
            </infAdic>
        </infNFe>
    </NFe>
</nfeProc>'''

    # Salvar os arquivos
    with open("nfs/NFe_001001_" + data_nf1.replace('-', '') + ".xml", 'w', encoding='utf-8') as f:
        f.write(xml1_content)
    
    with open("nfs/NFe_002001_" + data_nf2.replace('-', '') + ".xml", 'w', encoding='utf-8') as f:
        f.write(xml2_content)
    
    print("🎯 XMLs de teste criados com sucesso!")
    print("=" * 50)
    print("📁 Pasta: nfs/")
    print(f"📄 Arquivo 1: NFe_001001_{data_nf1.replace('-', '')}.xml")
    print(f"   📅 Data: {data_nf1} ({(datetime.now() - datetime.strptime(data_nf1, '%Y-%m-%d')).days} dias atrás)")
    print("   📦 Produtos: Parafusos M8 (800un), Porcas M8 (800un), Arruelas M8 (1200un)")
    print("   💰 Valor: R$ 1.060,00")
    print()
    print(f"📄 Arquivo 2: NFe_002001_{data_nf2.replace('-', '')}.xml")
    print(f"   📅 Data: {data_nf2} ({(datetime.now() - datetime.strptime(data_nf2, '%Y-%m-%d')).days} dias atrás)")
    print("   📦 Produtos: Chapas aço (25un), Tubos 40x40 (15un), Parafusos M8 (300un)")
    print("   💰 Valor: R$ 3.004,50")
    print()
    print("🔍 Cenários de teste incluídos:")
    print("   ✅ Produto repetido (Parafuso M8) em ambas NFs")
    print("   ✅ Datas diferentes para testar distribuição semanal")
    print("   ✅ Quantidades variadas para testar consolidação")
    print("   ✅ Carência de 30 dias aplicada automaticamente")
    print()
    print("🚀 Agora rode o sistema PCP para ver o plano de produção!")

if __name__ == "__main__":
    criar_xmls_teste()