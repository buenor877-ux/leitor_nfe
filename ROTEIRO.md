# Roteiro do projeto: Leitor de NF-e

Marque cada etapa com [x] quando terminar.

- [x] **Etapa 1: Preparar o projeto e ler uma nota.** Ambiente virtual, Git, estrutura do XML e primeiro script com ElementTree.
- [ ] **Etapa 2: Função que lê uma nota inteira.** `ler_nota(caminho)` devolve um dicionário com cabeçalho e itens.
- [ ] **Etapa 3: Ler várias notas de uma vez.** Ler a pasta inteira, montar tabelas com pandas e exportar para Excel.
- [ ] **Etapa 4: Guardar no banco SQLite.** Tabelas de fornecedores, notas e itens; não gravar a mesma nota duas vezes (pela chave de acesso).
- [ ] **Etapa 5: Interface e painel com Streamlit.** Upload dos XML, indicadores e gráficos (gasto por fornecedor, por mês, produtos mais comprados).
- [ ] **Etapa 6: Testes com pytest.** Testar leitura, totais e duplicidade.
- [ ] **Etapa 7: Publicar.** README com prints, deploy no Streamlit Cloud e post no LinkedIn.

As notas da pasta `notas_exemplo` são fictícias: as empresas e os CNPJs não existem.
Notas reais têm dados de empresas e pessoas, então nunca suba notas reais para o GitHub.
