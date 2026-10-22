# Scripts de maturação de WhatsApp

Coleção de scripts Python que automatizam conversas no WhatsApp Web (navegador ou emulador) controlando mouse e teclado. Os scripts sorteiam pares de frases ("pergunta" / "resposta") e as digitam alternadamente em várias janelas, simulando conversas entre números.

> ⚠️ Automatizar o WhatsApp viola os Termos de Uso do WhatsApp/Meta. Use por sua conta e risco e prefira manter este repositório **privado**.

## Estrutura

| Pasta | Conteúdo | Ponto de entrada |
|---|---|---|
| [maturacao_emuladores/](maturacao_emuladores/) | Maturação contínua em janelas "Chrome" (ciclos + reinício automático) | `kurama.py` |
| [maturacao_navegadores/](maturacao_navegadores/) | Versão para Chrome + Edge com envio por número — **em desenvolvimento, não roda** | `madara.py` |
| [gerador_conversas/](gerador_conversas/) | Gera `conversas8.py` e envia essas conversas em uma janela | `gerador_mensagens.py`, `envio_5_contra_1.py` |
| [utilitarios/](utilitarios/) | Ferramentas pequenas para descobrir janelas e coordenadas | ver abaixo |
| [arquivo/](arquivo/) | Versões antigas e de teste, preservadas como referência | — |

## Requisitos

- **Windows** (o `pygetwindow` só tem suporte completo no Windows).
- **Python 3.6+** (usa f-strings). Testado com Python 3.12.10.
- Pacotes: `pyautogui`, `pygetwindow`, `keyboard` (ver [requirements.txt](requirements.txt)).
- Fora do pip:
  - Navegador (Chrome/Edge) ou emulador com WhatsApp Web aberto e logado.
  - **Mesma resolução de tela e mesma disposição de janelas** usadas na criação dos scripts: as posições de clique são coordenadas fixas no código (ex.: `(943, 1268)`). Em outra tela, ajuste-as com `utilitarios/pegar_posicao.py`.

## Instalação

```powershell
cd Scripts
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Execução

Os scripts importam módulos da **própria pasta** (`Assuntos.py`, `conversas8.py`…) e gravam arquivos gerados no **diretório atual**. Por isso, sempre entre na pasta antes de rodar:

```powershell
cd maturacao_emuladores
python kurama.py
```

Durante a execução o script assume o mouse e o teclado. Para interromper: `Ctrl+C` no terminal, ou mova o mouse para um canto da tela (failsafe padrão do PyAutoGUI).

### Utilitários

| Script | O que faz | Comando |
|---|---|---|
| `listar_janelas.py` | Lista o título de todas as janelas abertas | `python utilitarios\listar_janelas.py` |
| `pegar_posicao.py` | Espera 5 s e mostra a posição atual do mouse | `python utilitarios\pegar_posicao.py` |
| `teste_mat.py` | Conta as janelas com "Chrome" no título | `python utilitarios\teste_mat.py` |
| `test_tab.py` | Segura Alt e aperta Tab 10 vezes (troca de janela) | `python utilitarios\test_tab.py` |
