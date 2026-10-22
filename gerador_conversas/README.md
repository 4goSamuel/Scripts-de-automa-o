# gerador_conversas

Gera um par de conversas e as envia em uma janela do WhatsApp.

## Arquivos

- `gerador_mensagens.py` — sorteia `TOTAL_MENSAGENS` (40) pares de frases e **sobrescreve** `conversas8.py` no diretório atual, com `conversa1` (perguntas) e `conversa2` (respostas).
- `conversas8.py` — conversas geradas (dados).
- `envio_5_contra_1.py` — importa `conversas8.py`, aguarda 5 s e, para cada mensagem, clica nas coordenadas de `wpps`, digita e aperta Enter.

## Executar

```powershell
cd gerador_conversas
python gerador_mensagens.py    # opcional: gera um novo conversas8.py
python envio_5_contra_1.py     # deixe o campo de mensagem visível na coordenada configurada
```

## Configuração

- `envio_5_contra_1.py`: a lista `wpps` tem só uma coordenada `(765, 686)`, então apenas `conversa1` é enviada. Para usar mais janelas, adicione coordenadas a `wpps` e conversas correspondentes a `conversas`.
- Velocidade de digitação: `delay=random.uniform(0.035, 0.059)` em `digitar()`.
