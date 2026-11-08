# Junta a leitura das notas (ler_nota.py) com a gravação no banco (banco.py).
from pathlib import Path

from ler_nota import ler_nota
from banco import criar_tabelas, gravar_nota


# Função salvar_notas: lê cada XML da pasta e grava no banco, sem repetir notas.
def salvar_notas(caminho_pasta, caminho_banco):
    # Pega todos os arquivos XML da pasta
    notas = sorted(Path(caminho_pasta).glob("*.xml"))

    # Cria as tabelas, se ainda não existirem
    criar_tabelas(caminho_banco)

    for caminho_nota in notas:
        # Lê a nota e guarda o dicionário
        nota_info = ler_nota(caminho_nota)

        # Tenta gravar: a função devolve True (gravou) ou False (já existia)
        gravou = gravar_nota(caminho_banco, nota_info)

        if gravou:
            print(f"Nota {nota_info['numero']} do fornecedor {nota_info['fornecedor']} gravada no banco de dados.")
        else:
            print(f"A nota {nota_info['numero']} do fornecedor {nota_info['fornecedor']} já está no banco de dados.")


if __name__ == "__main__":
    salvar_notas("notas_exemplo", "notas.db")