# maturacao_emuladores

`kurama.py` — maturação contínua em todas as janelas cujo título contém **"Chrome"**.

## Arquivos

- `kurama.py` — script principal.
- `Assuntos.py` — banco de pares (pergunta, resposta) por tema: empresa, universo, livros, comida, social, aleatórios.
- `conversas.py` — gerado pelo `kurama.py` a cada ciclo (pode começar vazio, mas precisa existir: é importado).

## O que o script faz

Repete 5 ciclos (`for l in range(5)`); em cada ciclo:

1. Encontra as janelas "Chrome" e, em cada uma: maximiza, `Ctrl+0`, clica em `(167, 174)` e `(165, 175)`, digita `Projeto e25 <ciclo>` + uma saudação aleatória e minimiza.
2. Sorteia `TOTAL_MENSAGENS` (5) pares de frases para cada par de janelas e grava em `conversas.py`.
3. Para cada mensagem, percorre as janelas (na ordem inversa), clica em `(943, 1268)` e `(1321, 1266)`, digita a frase e aperta Enter.
4. Aguarda `temporizador` × 5 min (padrão 12 → 1 hora).

Depois dos 5 ciclos, **o script se reinicia sozinho** (`os.execv`), ou seja, roda indefinidamente até ser interrompido.

## Configuração (no topo do loop em `kurama.py`)

| Variável | Padrão | Significado |
|---|---|---|
| `TOTAL_MENSAGENS` | 5 | mensagens por janela em cada ciclo |
| `temporizador` | 12 | pausa entre ciclos, em blocos de 5 min |
| coordenadas em `ag.moveTo(...)` | — | dependem da sua tela |

## Executar

```powershell
cd maturacao_emuladores
python kurama.py
```

## Observações

- A linha `ag.hotkey('ctrl'+ 'f5')` passa uma única string `"ctrlf5"`; provavelmente não envia Ctrl+F5 como pretendido. Não foi alterada.
- `local_digitacao` é definida mas não é usada.
