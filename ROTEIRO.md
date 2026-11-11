# Roteiro do projeto: Leitor de NF-e

Marque cada etapa com [x] quando terminar.

- [x] **Etapa 1: Preparar o projeto e ler uma nota.** Ambiente virtual, Git, estrutura do XML e primeiro script com ElementTree.
- [x] **Etapa 2: Função que lê uma nota inteira.** `ler_nota(caminho)` devolve um dicionário com cabeçalho e itens.
- [x] **Etapa 3: Ler várias notas de uma vez.** Ler a pasta inteira, montar tabelas com pandas e exportar para Excel.
- [x] **Etapa 4: Guardar as notas em banco de dados.** SQLite com tabelas de fornecedores, notas e itens, sem gravar nota repetida.
- [x] **Etapa 5: Interface e painel com Streamlit.** Upload dos XML, indicadores e gráficos (gasto por fornecedor, por mês, produtos mais comprados).
- [x] **Etapa 6: Testes com pytest.** Testar leitura, totais e duplicidade.
- [ ] **Etapa 7: Publicar.** README com prints, deploy no Streamlit Cloud e post no LinkedIn.

As notas da pasta `notas_exemplo` são fictícias: as empresas e os CNPJs não existem.
Notas reais têm dados de empresas e pessoas, então nunca suba notas reais para o GitHub.
