# a função tmp_path é uma fixture do pytest que cria um diretório temporário para os testes. Esse diretório é automaticamente limpo após o teste ser concluído, garantindo que os testes não deixem resíduos no sistema de arquivos.
from pathlib import Path
from ler_nota import ler_nota
from banco import criar_tabelas, gravar_nota

# Teste da função gravar_nota
def test_nota_repetida_nao_grava(tmp_path):
    banco = tmp_path / "teste.db"
    criar_tabelas(banco)
    nota = ler_nota(Path("notas_exemplo/NFe_35260945678901000123550010000015321000015325.xml"))

# Verifica se a nota foi gravada com sucesso na primeira tentativa e não foi gravada na segunda tentativa (nota repetida)
    assert gravar_nota(banco, nota) == True
    assert gravar_nota(banco, nota) == False