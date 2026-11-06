# Onde paramos (atualizado em 03/11/2026)

## Leitor de NF-e

**Etapa 1: concluída.** O `ler_nota.py` lê a primeira nota de `notas_exemplo`, mostra o cabeçalho e os produtos (quantidade × valor unitário = total) e confere a soma dos itens com o `vProd` do total. Também mostra a conta produtos + frete = valor da nota.

**Em andamento:** comentar o `ler_nota.py` para estudo.
- [ ] Terminar os comentários da parte da conferência (blocos 1 a 4)
- [ ] Commit: `git commit -m "Adiciona anotações de estudo da Etapa 1"`
- [ ] Antes da Etapa 2, guardar a versão comentada em `estudos/etapa1_comentado.py`

**Próximo: Etapa 2.** Transformar o código numa função `ler_nota(caminho)` que **devolve** um dicionário (fornecedor, número, data, totais e `itens` como lista de dicionários), em vez de imprimir.
- Pergunta para responder antes de começar: *por que é melhor a função devolver os dados com `return` do que imprimir com `print`?*

## O que já aprendi
- Ler XML com `ElementTree` e usar o namespace `nfe:`
- `find` × `findall`; caminho com `.//` × caminho direto
- Converter texto em número com `float()` e formatar com `:.2f` e `:.0f`
- Comparar dinheiro com `round(..., 2)` (`0.1 + 0.2` não dá `0.3`)
- Regra de negócio: valor da nota (`vNF`) = produtos (`vProd`) + frete (`vFrete`) + outros − descontos
- Ambiente virtual (`.venv`), `.gitignore`, commits pequenos
- PowerShell: liberar o `activate` com `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
