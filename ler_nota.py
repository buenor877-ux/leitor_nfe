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
    print("Arquivo:", nota_info["arquivo"])
    print("Fornecedor:", nota_info["fornecedor"])
    print("Número da NF-e:", nota_info["numero"])
    print("Data de emissão:", nota_info["data_emissao"])
    print("valor total da NF-e:", raiz.find(".//nfe:total/nfe:ICMSTot/nfe:vNF", NS).text)

    # --- 2. Pega os produtos da nota
    print("cada produto da NF-e:")
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
        print(f"  {nome} | {qtd:.0f} un x R$ {unit:.2f} = R$ {valor:.2f}")

    # 1. Soma dos produtos, item por item
    soma_itens = sum(float(produto.find("nfe:prod/nfe:vProd", NS).text) for produto in produtos)

    # 2. Pega os valores do bloco de totais
    total = raiz.find(".//nfe:total/nfe:ICMSTot", NS)
    total_produtos = float(total.find("nfe:vProd", NS).text)
    frete = float(total.find("nfe:vFrete", NS).text)
    valor_nota = float(total.find("nfe:vNF", NS).text)

    nota_info["total_produtos"] = total_produtos
    nota_info["frete"] = frete
    nota_info["valor_nota"] = valor_nota

    # 3. Conferência
    if round(soma_itens, 2) == round(total_produtos, 2):
        print("Conferência OK: a soma dos itens bate com o total de produtos.")
    else:
        print(f"Diferença: itens R$ {soma_itens:.2f} x total da nota R$ {total_produtos:.2f}")

    # 4. Bônus: mostrar a conta do total
    print(f"Produtos R$ {total_produtos:.2f} + Frete R$ {frete:.2f} = Nota R$ {valor_nota:.2f}")

    return nota_info

def main():
    # Caminho do arquivo XML da nota fiscal
    caminho_nota = "notas_exemplo"

    # Chama a função ler_nota e armazena o resultado em uma variável
    nota_info = ler_nota(Path(caminho_nota) / "NFe_35260945678901000123550010000015321000015325.xml")  


    # Exibe o dicionário completo da nota
    print("\nDicionário completo da nota:")
    print(nota_info)


main()
