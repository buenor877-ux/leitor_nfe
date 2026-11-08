# Onde paramos (atualizado em 08/11/2026)

## Leitor de NF-e

**Etapa 1: concluída.** A versão comentada para estudo está em `estudos/etapa1_comentado.py`.

**Etapa 2: concluída.** A função `ler_nota(caminho)` devolve um dicionário com os dados da nota, e o `main()` cuida da exibição e da conferência. Testada com as 3 notas de exemplo.

**Etapa 3: concluída.** O `gerar_relatorio.py` lê todos os XML da pasta, monta as tabelas de notas e de itens com pandas e grava o `relatorio_notas.xlsx` com as abas `Notas` e `Itens`. Conferido: a soma das notas (R$ 3.071,75) menos a soma dos itens (R$ 2.988,25) dá o frete (R$ 83,50).

**Próximo: Etapa 4 (branch `etapa-4`).** Guardar as notas em um banco SQLite, com as tabelas `fornecedores`, `notas` e `itens`, sem gravar a mesma nota duas vezes.
- Ler a chave de acesso (atributo `Id` da tag `infNFe`) e o CNPJ do fornecedor, que o `ler_nota` ainda não pega.
- Pronto quando rodar duas vezes e o banco continuar com 3 notas e 9 itens.

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
