
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
    nome = produto.find("nfe:prod/nfe:xProd", NS).text
    qtd = float(produto.find("nfe:prod/nfe:qCom", NS).text)
    unit = float(produto.find("nfe:prod/nfe:vUnCom", NS).text)
    valor = float(produto.find("nfe:prod/nfe:vProd", NS).text)
    print(f"  {nome} | {qtd:.0f} un x R$ {unit:.2f} = R$ {valor:.2f}")


# 1. Soma dos produtos, item por item (isso você já tinha)
soma_itens = sum(float(produto.find("nfe:prod/nfe:vProd", NS).text) for produto in produtos)

# 2. Pegue os valores do bloco de totais
total = raiz.find(".//nfe:total/nfe:ICMSTot", NS)
total_produtos = float(total.find("nfe:vProd", NS).text)   # soma dos produtos segundo a nota
frete          = float(total.find("nfe:vFrete", NS).text)   # frete
valor_nota     = float(total.find("nfe:vNF", NS).text)   # valor final

# 3. Conferência
if round(soma_itens, 2) == round(total_produtos, 2):
    print("Conferência OK: a soma dos itens bate com o total de produtos.")
else:
    print(f"Diferença: itens R$ {soma_itens:.2f} x total da nota R$ {total_produtos:.2f}")

# 4. Bônus: mostrar a conta do total
print(f"Produtos R$ {total_produtos:.2f} + Frete R$ {frete:.2f} = Nota R$ {valor_nota:.2f}")


