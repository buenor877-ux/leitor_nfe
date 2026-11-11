# pathlib é uma biblioteca que ajuda a lidar com caminhos de arquivos e diretórios de forma mais fácil e intuitiva. patyh.Path é uma classe dentro dessa biblioteca que representa um caminho de arquivo ou diretório. Ela permite criar, manipular e acessar arquivos e pastas de maneira mais conveniente do que usando strings simples.
from pathlib import Path
from ler_nota import ler_nota
# Teste da função ler_nota
def test_le_nota_1532():
    nota = ler_nota(Path("notas_exemplo/NFe_35260945678901000123550010000015321000015325.xml"))

# Verifica se os valores lidos da nota estão corretos
    assert nota["numero"] == "1532"
    assert nota["fornecedor"] == "DISTRIBUIDORA ALFA ELETRONICOS LTDA"
    assert len(nota["produtos"]) == 3
    assert nota["valor_nota"] == 749.5

def test_totais_batem():
    for arquivo in sorted(Path("notas_exemplo").glob("*.xml")):
        nota = ler_nota(arquivo)
        print(f"Nota {nota['numero']} do fornecedor {nota['fornecedor']} lida com sucesso!")

        total_calculado = round(sum(produto["valor_total"] for produto in nota["produtos"]), 2)
        assert total_calculado == round(nota["total_produtos"], 2), f"Erro na nota {nota['numero']}: total calculado não bate com o valor da nota."
        assert round(nota["total_produtos"] + nota["frete"], 2) == round(nota["valor_nota"], 2)