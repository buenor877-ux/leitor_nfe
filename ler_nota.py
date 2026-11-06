#import xml.etree.ElementTree as ET serve para ler arquivos XML, que é o formato das notas fiscais eletrônicas (NF-e). E pathlib.Path serve para manipular caminhos de arquivos e diretórios de forma mais conveniente.
import xml.etree.ElementTree as ET
from pathlib import Path

# Toda tag da NF-e pertence a este "namespace". Sem ele, o find() não encontra nada.
NS = {"nfe": "http://www.portalfiscal.inf.br/nfe"}

# Coloque a leitura do XML dentro de uma função chamada ler_nota, que recebe o caminho do arquivo.
def ler_nota(caminho):
    caminho = Path(caminho)

    # Lê o arquivo XML e pega a raiz do documento
    raiz = ET.parse(caminho).getroot()

    # --- 1. ao em vez de imprimir Juntar dados do cabeçalho da nota: fornecedor, número, data e valor total num dicionario
    fornecedor = raiz.find(".//nfe:emit/nfe:xNome", NS).text
    nota_info = {
        "arquivo": caminho.name,
        "fornecedor": fornecedor,
        "numero": raiz.find(".//nfe:ide/nfe:nNF", NS).text,
        "data_emissao": raiz.find(".//nfe:ide/nfe:dhEmi", NS).text
    }

    # --- 2. Pega os produtos da nota
    produtos = raiz.findall(".//nfe:det", NS)

    # --- 3. Guarde os produtos numa lista de dicionários, um para cada produto, e coloque essa lista dentro do dicionário da nota e Faça a função devolver esse dicionário.
    nota_info["produtos"] = []
    for produto in produtos:
        nome = produto.find("nfe:prod/nfe:xProd", NS).text
        qtd = float(produto.find("nfe:prod/nfe:qCom", NS).text)
        unit = float(produto.find("nfe:prod/nfe:vUnCom", NS).text)
        valor = float(produto.find("nfe:prod/nfe:vProd", NS).text)
        nota_info["produtos"].append({
            "nome": nome,
            "quantidade": qtd,
            "valor_unitario": unit,
            "valor_total": valor
        })

    # 2. Pega os valores do bloco de totais
    total = raiz.find(".//nfe:total/nfe:ICMSTot", NS)
    total_produtos = float(total.find("nfe:vProd", NS).text)
    frete = float(total.find("nfe:vFrete", NS).text)
    valor_nota = float(total.find("nfe:vNF", NS).text)

    nota_info["total_produtos"] = total_produtos
    nota_info["frete"] = frete
    nota_info["valor_nota"] = valor_nota

    return nota_info

def main():
    # Pega uma nota da pasta: troque o [0] por [1] ou [2] para testar as outras
    caminho_nota = sorted(Path("notas_exemplo").glob("*.xml"))[0]

    # Lê a nota e guarda o dicionário devolvido pela função
    nota_info = ler_nota(caminho_nota)

    # Cabeçalho
    print("Arquivo:", nota_info["arquivo"])
    print("Fornecedor:", nota_info["fornecedor"])
    print("Número da NF-e:", nota_info["numero"])
    print("Data de emissão:", nota_info["data_emissao"])
    print(f"Valor total da NF-e: R$ {nota_info['valor_nota']:.2f}")

    # Produtos
    print("Cada produto da NF-e:")
    for produto in nota_info["produtos"]:
        print(f"  {produto['nome']} | {produto['quantidade']:.0f} un x R$ {produto['valor_unitario']:.2f} = R$ {produto['valor_total']:.2f}")

    # Conferência
    soma_produtos = sum(produto["valor_total"] for produto in nota_info["produtos"])
    if round(soma_produtos, 2) == round(nota_info["total_produtos"], 2):
        print("Conferência OK: a soma dos itens bate com o total de produtos.")
    else:
        print(f"Diferença: itens R$ {soma_produtos:.2f} x total da nota R$ {nota_info['total_produtos']:.2f}")

    # Conta do total
    print(f"Produtos R$ {nota_info['total_produtos']:.2f} + Frete R$ {nota_info['frete']:.2f} = Nota R$ {nota_info['valor_nota']:.2f}")


main()



