# Jogo da Cobrinha

Este é um jogo simples da cobrinha (Snake) feito em Python usando a biblioteca Pygame.

## Descrição

- Tela: 600x600 pixels
- Controles: setas do teclado (cima, baixo, esquerda, direita)
- Objetivo: comer as maçãs vermelhas para ganhar pontos e evitar colidir com as paredes, obstáculos ou o próprio corpo.
- A cada maçã comida, um obstáculo é adicionado e a velocidade aumenta a cada 5 pontos.

## Arquivos

- `jogo.py` - código fonte principal do jogo.
- `README.md` - este arquivo.
- `requirements.txt` - dependências do projeto (opcional).

## Requisitos

- Python 3.10 a 3.12 recomendado.
- Pygame

## Como executar

No PowerShell, dentro da pasta do projeto:

```powershell
python jogo.py
```

## Observações sobre o código (`jogo.py`)

- Variáveis principais:
  - `WINDOWS_WITDH`, `WINDOWS_HEIGTH`: tamanho da janela
  - `BLOCK`: tamanho do bloco da cobra / maçã
  - `velocidade`: controla a taxa de atualização do jogo

- Pontos de melhoria / bugs conhecidos:
  - `gera_pos_aleatoria` chama `gera_pos_aleatoria()` recursivamente mas não retorna corretamente em alguns caminhos e tem repetição desnecessária.
  - `verifica_margens` inverte a lógica (retorna False quando dentro das margens). Embora funcione com o uso atual, isso causa confusão.
  - Chamadas a `game_over` em alguns locais estão sem parênteses (por exemplo `game_over` em vez de `game_over()`).
  - Algumas variáveis e nomes têm pequenos erros de digitação (`WINDOWS_WITDH`, `OBISTACULO` vs `obistaculo` etc.).

## requirements.txt

```
pygame
```

## Contribuição

Se quiser contribuir com melhorias, abra um fork e envie pull requests. Exemplos de melhorias sugeridas:

- Corrigir bugs listados em "Observações sobre o código"
- Adicionar telas de menu e pausa
- Salvar recordes em arquivo

Se quiser que eu atualize o README com imagens, GIFs, instruções de build específicas para sua máquina, ou se desejar que eu corrija os bugs no código, me avise.
