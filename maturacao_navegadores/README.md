# maturacao_navegadores (em desenvolvimento)

> ⚠️ **Não executável no estado atual.** `madara.py` tem erro de sintaxe e trechos incompletos.

Ideia do script: detectar janelas do **Chrome e do Edge**, gerar conversas a partir de `Assuntos.py` e, em cada janela, iniciar conversa com cada número de `numeros_wpp.py` (navegando por Tab/Enter) e enviar a mensagem.

## Arquivos

- `madara.py` — script principal (incompleto).
- `Assuntos.py` — banco de frases (cópia idêntica à de `maturacao_emuladores/`).
- `numeros_wpp.py` — lista `numeros` com os números de destino.
- `teste.py` — fragmento de código (trecho do temporizador/reinício do kurama), não é um script independente.

## Pendências conhecidas

- `madara.py:258-260` — o bloco `for j, janela in enumerate(reversed(janelas_Chrome)):` está sem indentação no corpo → `IndentationError`.
- `ag.moveTo("_____________")` e `ag.moveTo('_______________')` — coordenadas ainda não preenchidas.
- `digitar(conversa[envio][janela])` — a variável `conversa` não existe neste ponto (provavelmente deveria usar `conversas`); `envio` é um número (string), não um índice.
- `teste.py:13` — indentação inesperada; é um trecho solto.

## Executar (quando concluído)

```powershell
cd maturacao_navegadores
python madara.py
```
