# Sua função será percorrer todos os XML da pasta e guarda os dicionários numa lista.
from pathlib import Path
import pandas as pd

from ler_nota import ler_nota

# Gerar relatório de notas implemente a função gerar_relatorio(pasta_notas) que percorre todos os XML da pasta e guarda os dicionários numa lista. A função deve devolver essa lista.
def gerar_relatorio(pasta_notas):
    relatorio = []
    for caminho_nota in sorted(Path(pasta_notas).glob("*.xml")):
        nota_info = ler_nota(caminho_nota)
        relatorio.append(nota_info)
    return relatorio

# montar tabela usando pandas uma linha por nota.

def montar_tabela_notas(relatorio):
    return pd.DataFrame(relatorio).drop(columns=["produtos"])


# montar_tabela_itens com a mesma ideia, mas agora cada linha da tabela será um produto de uma nota. A tabela terá as colunas: arquivo, fornecedor, numero, data_emissao, nome_produto, quantidade, valor_unitario, valor_total. Use print no resultado. Devem aparecer 9 linhas.
def montar_tabela_itens(relatorio):
    itens = []
    for nota in relatorio:
        for produto in nota["produtos"]:
            item = {
                "arquivo": nota["arquivo"],
                "fornecedor": nota["fornecedor"],
                "numero": nota["numero"],
                "data_emissao": nota["data_emissao"],
                "nome_produto": produto["nome"],
                "quantidade": produto["quantidade"],
                "valor_unitario": produto["valor_unitario"],
                "valor_total": produto["valor_total"]
            }
            itens.append(item)
    return pd.DataFrame(itens)

  # Crie uma função que recebe as duas tabelas e grava um arquivo .xlsx, depois de montar as tabelas, para gravar o arquivo relatorio.xlsx com as duas tabelas. Use pd.ExcelWriter() para gravar as duas tabelas em planilhas diferentes do mesmo arquivo.
def gravar_relatorio_excel(tabela_notas, tabela_itens, nome_arquivo):
    with pd.ExcelWriter(nome_arquivo) as writer:
        tabela_notas.to_excel(writer, sheet_name="Notas", index=False)
        tabela_itens.to_excel(writer, sheet_name="Itens", index=False)  


def main():
    # Ler as notas da pasta uma vez
    relatorio = gerar_relatorio("notas_exemplo")

    # Montar a tabela de notas
    tabela_notas = montar_tabela_notas(relatorio)

    # Montar a tabela de itens
    tabela_itens = montar_tabela_itens(relatorio)

    # Mostrar as duas tabelas
    print("Tabela de notas:")
    print(tabela_notas)
    print("\nTabela de itens:")
    print(tabela_itens)

    
    # Gravar as duas tabelas no Excel
    gravar_relatorio_excel(tabela_notas, tabela_itens, "relatorio_notas.xlsx")


if __name__ == "__main__":
    main()

   

