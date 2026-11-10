# Importe o streamlit com o apelido st
import streamlit as st

# Imports: traga o ler_nota (do ler_nota.py) e o criar_tabelas e o gravar_nota (do banco.py). Os imports ficam no topo, junto com o do Streamlit.
from ler_nota import ler_nota
from banco import criar_tabelas, gravar_nota

# titulo da página
st.title("Leitor de NF-e")


# Explique para o cliente a finalidade e os ganhos do sistema.
st.write("""
O sistema ajuda você a conferir se os totais da nota estão corretos, evitar o
lançamento duplicado de uma mesma nota e acompanhar os gastos por fornecedor,
mês e produto.
""")

# tabelas
criar_tabelas("notas.db")

# Campo de upload de arquivo XML
arquivos = st.file_uploader("Escolha os arquivos XML", type="xml", accept_multiple_files=True)

# Para cada arquivo enviado, faça a leitura da nota e tente gravar no banco de dados.
for file in arquivos:  
    # Ler a nota fiscal do arquivo XML
    nota_info = ler_nota(file)

    # Tentar gravar a nota no banco de dados
    sucesso = gravar_nota("notas.db", nota_info)

    # Exibir mensagem de sucesso ou erro
    if sucesso:
        st.success(f"Nota {nota_info['numero']} gravada com sucesso!")
    else:
        st.info(f"Nota {nota_info['numero']} do fornecedor {nota_info['fornecedor']} já existe no banco de dados.")





