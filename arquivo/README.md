# arquivo

Versões antigas e de teste, mantidas como referência. Não são mantidas e várias não funcionam com os dados atuais.

## rodando/

- `kurama_2.py` — variante de `maturacao_emuladores/kurama.py` com `TOTAL_MENSAGENS = 2` e o temporizador fora do loop de 5 ciclos (espera 1 hora só ao final dos 5 ciclos).
- `Assuntos.py`, `conversas.py` — cópias locais das quais ele depende.

## obsoletos/

Bots de primeira geração: clicam em coordenadas fixas de várias janelas lado a lado (`wpps`) e nos "blocos" de reorganização.

| Script | Dados que usa | Estado |
|---|---|---|
| `bot_wpp.py` | conversas embutidas (8) | sintaxe OK |
| `final_12_sequencia.py` | conversas embutidas (12) | sintaxe OK |
| `teste_matura_envio.py` | conversas embutidas (10) | sintaxe OK |
| `tx.py`, `teste_3_entre_eles.py` | `conversas9.py` | sintaxe OK |
| `maturacao_3_numeros.py` | `conversas8.py` | ⚠️ usa `conversa3`…`conversa10`, que não existem no `conversas8.py` atual |
| `teste_matura_envio2.py`, `teste_maturacao_envio3.py` | `conversas8.py`, `numeros_wpp.py`, `mensagens_clientes.py` | ⚠️ usam `conversa3`…`conversa12`, que não existem no `conversas8.py` atual |
| `testeclick.py` | — | ⚠️ usa `conversa1`…`conversa4` sem importar nada |
| `gerador.py` | — | gera `conversastestes.py` (18 conversas × 50 mensagens) |

`conversas8.py` aqui é uma cópia do arquivo de `gerador_conversas/`, colocada para que os imports locais funcionem. `conversas9.py`, `conversas_50.py` e `conversastestes.py` são saídas antigas de geradores.

Para rodar qualquer um: `cd arquivo\obsoletos` e `python <script>.py`.
