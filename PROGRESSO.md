# Onde paramos (atualizado em 10/11/2026, Etapa 5 parada na parte 5.5)

## Leitor de NF-e

**Etapa 1: concluída.** A versão comentada para estudo está em `estudos/etapa1_comentado.py`.

**Etapa 2: concluída.** A função `ler_nota(caminho)` devolve um dicionário com os dados da nota, e o `main()` cuida da exibição e da conferência. Testada com as 3 notas de exemplo.

**Etapa 3: concluída.** O `gerar_relatorio.py` lê todos os XML da pasta, monta as tabelas de notas e de itens com pandas e grava o `relatorio_notas.xlsx` com as abas `Notas` e `Itens`. Conferido: a soma das notas (R$ 3.071,75) menos a soma dos itens (R$ 2.988,25) dá o frete (R$ 83,50).

**Etapa 4: concluída.** O `ler_nota` passou a ler a chave de acesso e o CNPJ do fornecedor. O `banco.py` cria as tabelas `fornecedores`, `notas` e `itens` e tem a `gravar_nota`, que consulta a chave antes de gravar e devolve `True` ou `False`. O `salvar_notas.py` lê a pasta e grava tudo. Conferido: rodando duas vezes, o banco fica com 2 fornecedores, 3 notas (R$ 3.071,75) e 9 itens (R$ 2.988,25).

**Etapa 5: em andamento (branch `etapa-5`).** Interface e painel com Streamlit. Rodar com `streamlit run app.py`.
- [x] 5.0 Preparação: branch, Streamlit instalado e `PRAGMA foreign_keys = ON` na função `conectar_banco`.
- [x] 5.1 Primeira tela: título e texto explicando o sistema.
- [x] 5.2 Upload dos XML: o `ler_nota` passou a aceitar o arquivo enviado (não usa mais `Path(...)`), e nota repetida aparece com `st.info`.
- [x] 5.3 Leitura do banco: `carregar_notas` (com `JOIN` para trazer o nome do fornecedor) e `carregar_itens` no `banco.py`.
- [x] 5.4 Indicadores: total gasto (R$ 3071.75), 3 notas, 2 fornecedores e média por nota (R$ 1023.92).
- [ ] **5.5 Gráficos: continuar daqui.** O de gasto por fornecedor já está pronto (ALFA 2219.00, BETA 852.75). Faltam, nesta ordem, os passos que estão em comentário no fim do `app.py`:
  1. Gasto por mês: coluna `mes` com `data_emissao.str[:7]`, `groupby`, `sum` e `st.bar_chart`. Esperado: 2026-09 = 1602.25 e 2026-10 = 1469.50.
  2. Produtos mais comprados: `itens_df` agrupado por `nome_produto`, soma da `quantidade`, `sort_values(ascending=False)`. Esperado: CABO HDMI 50 e PENDRIVE 32GB 40 no topo.
  3. Tabela completa: `st.subheader("Notas no banco")` e `st.dataframe(notas_df)`.
- [ ] 5.6 Fechamento: conferir os valores, commit, merge na `master`, `git push`, marcar a etapa no `ROTEIRO.md` (incluir a linha da Etapa 4, que está faltando) e atualizar este arquivo.

**Jeito de estudar:** receber o objetivo e os passos gerais, escrever o plano em comentários, aceitar sugestões do VS Code em pedaços pequenos e conseguir explicar cada linha antes de manter.

## O que já aprendi
- Ler XML com `ElementTree` e usar o namespace `nfe:`
- `find` × `findall`; caminho com `.//` × caminho direto
- Converter texto em número com `float()` e formatar com `:.2f` e `:.0f`
- Comparar dinheiro com `round(..., 2)` (`0.1 + 0.2` não dá `0.3`)
- Regra de negócio: valor da nota (`vNF`) = produtos (`vProd`) + frete (`vFrete`) + outros − descontos
- Funções: `def`, parâmetros, `return` e diferença entre definir e chamar
- `return` × `print`: `print` só mostra na tela; `return` entrega os dados para o programa continuar usando. Sem `return`, a função devolve `None`
- Dicionários e lista de dicionários para organizar os dados de uma nota
- Recuo define a qual bloco a linha pertence; variável criada numa função só existe nela
- Ambiente virtual (`.venv`), `.gitignore`, commits pequenos
- Git: branch, `git switch`, `git switch -c`, `git merge` e `git branch -d`
- PowerShell: liberar o `activate` com `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
- Instalar bibliotecas com `pip install` dentro do `.venv`
- Separar responsabilidades em arquivos e usar `import` entre eles, sem importação circular
- `if __name__ == "__main__":` roda o `main()` só quando o arquivo é executado direto
- Ordem no arquivo: imports, funções e, no fim, o bloco que chama o `main()`
- `sorted(Path(pasta).glob("*.xml"))` para ler todos os arquivos da pasta em ordem
- pandas: `pd.DataFrame` a partir de lista de dicionários e `.drop(columns=[...])`
- `for` dentro de `for` para dados dentro de dados (produtos dentro de notas)
- `pd.ExcelWriter` + `to_excel` para gravar várias abas; `index=False` tira a numeração
- Conferir sugestões de código: o `Path` certo vem de `pathlib`, não de `zipfile`
- Rodar sem erro não basta: conferir o resultado com os totais
- Publicar no GitHub: `git remote add`, `git push -u` e conferir antes se não há dado pessoal no histórico
- SQLite: banco num arquivo `.db`, com tabelas ligadas por chave primária e chave estrangeira
- Tipos: `REAL` para valores com que se faz conta, `TEXT` para identificadores como CNPJ e número da nota
- `CREATE TABLE IF NOT EXISTS`, `INSERT` com `?` (evita SQL injection) e `INSERT OR IGNORE`
- `SELECT` + `fetchone()` para consultar antes de gravar (`None` quando não acha)
- `commit` confirma tudo de uma vez; `try`/`finally` fecha a conexão mesmo com erro
- Atributo do XML se lê com `.get("Id")`; `[3:]` corta o começo de um texto
- Para campo obrigatório, usar colchetes e não `.get(campo, padrão)`, que esconde erro de nome
