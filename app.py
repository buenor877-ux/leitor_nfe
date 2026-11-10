# Importe o streamlit com o apelido st
import streamlit as st

# Imports: traga o ler_nota (do ler_nota.py) e o criar_tabelas e o gravar_nota (do banco.py). Os imports ficam no topo, junto com o do Streamlit.
from ler_nota import ler_nota
from banco import criar_tabelas, gravar_nota, carregar_notas, carregar_itens

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

# Carrega as tabelas do banco (já com as notas que acabaram de ser enviadas)
notas_df = carregar_notas("notas.db")
itens_df = carregar_itens("notas.db")

# --- 5.4 Indicadores ---
st.subheader("Resumo das notas")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total gasto", f"R$ {notas_df['valor_nota'].sum():.2f}")
col2.metric("Notas", len(notas_df))
col3.metric("Fornecedores", notas_df["fornecedor"].nunique())
col4.metric("Média por nota", f"R$ {notas_df['valor_nota'].mean():.2f}")

# --- 5.5 Gráficos ---

# Gasto por fornecedor
st.subheader("Gasto por fornecedor")
gasto_fornecedor = notas_df.groupby("fornecedor")["valor_nota"].sum()
st.bar_chart(gasto_fornecedor)

# Próximos passos da 5.5 (continuar daqui):
# 1. Gasto por mês: criar a coluna "mes" com os 7 primeiros caracteres da data_emissao,
#    agrupar por "mes", somar "valor_nota" e mostrar com st.bar_chart.
# 2. Produtos mais comprados: agrupar itens_df por "nome_produto", somar "quantidade",
#    ordenar do maior para o menor e mostrar com st.bar_chart.
# 3. Tabela completa: st.subheader("Notas no banco") e st.dataframe(notas_df).
