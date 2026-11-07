# Onde paramos (atualizado em 06/11/2026)

## Leitor de NF-e

**Etapa 1: concluída.** A versão comentada para estudo está em `estudos/etapa1_comentado.py`.

**Etapa 2: concluída.** A função `ler_nota(caminho)` devolve um dicionário com os dados da nota, e o `main()` cuida da exibição e da conferência. Testada com as 3 notas de exemplo.

**Próximo: Etapa 3 (branch `etapa-3`).** Ler a pasta inteira, montar tabelas com pandas e exportar para Excel.
- Antes de importar `ler_nota` em outro arquivo, proteger a chamada do `main()` com `if __name__ == "__main__":`.

**Jeito de estudar:** receber o objetivo e os passos gerais e aplicar com a minha interpretação, pedindo dica quando travar.

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
