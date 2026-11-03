import xml.etree.ElementTree as ET
from pathlib import Path

# Toda tag da NF-e pertence a este "namespace". Sem ele, o find() não encontra nada.
NS = {"nfe": "http://www.portalfiscal.inf.br/nfe"}

# Pega o primeiro arquivo .xml da pasta
caminho = sorted(Path("notas_exemplo").glob("*.xml"))[0]

raiz = ET.parse(caminho).getroot()

fornecedor = raiz.find(".//nfe:emit/nfe:xNome", NS).text
print("Arquivo:", caminho.name)
print("Fornecedor:", fornecedor)
print("número da NF-e:", raiz.find(".//nfe:ide/nfe:nNF", NS).text)
print("data de emissão:", raiz.find(".//nfe:ide/nfe:dhEmi", NS).text)
print("valor total da NF-e:", raiz.find(".//nfe:total/nfe:ICMSTot/nfe:vNF", NS).text)
print("cada produto da NF-e:")
produtos = raiz.findall(".//nfe:det", NS)
for produto in produtos:
    nome = produto.find(".//nfe:prod/nfe:xProd", NS).text
    valor = produto.find(".//nfe:prod/nfe:vProd", NS).text
    print(f"  {nome} - R$ {valor}")
vProd = sum(float(produto.find(".//nfe:prod/nfe:vProd", NS).text) for produto in produtos)
vNF = float(raiz.find(".//nfe:total/nfe:ICMSTot/nfe:vNF", NS).text)
if vProd == vNF:
    print("O valor total da NF-e está correto.")

