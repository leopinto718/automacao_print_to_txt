# Visão geral do projeto

Este projeto tem como objetivo demonstrar uma abordagem **experimental e educacional** para automação da captura visual do histórico de mensagens no WhatsApp Web, em cenários onde a exportação direta em formato texto não está disponível.

A estratégia adotada nesta fase inicial é baseada em:

1. Automação da interface gráfica (UI automation)
2. Rolagem controlada da conversa
3. Captura sequencial de screenshots da área de mensagens
4. Detecção automática do fim do histórico por similaridade visual

Os screenshots gerados podem posteriormente ser processados com técnicas de **OCR**, permitindo a extração e análise textual das mensagens para fins de estudo.

---

## Estrutura atual do projeto

Nesta etapa, o projeto contém **dois scripts principais**, que devem ser utilizados em sequência:

```
projeto/
├── descobrir_coordenadas.py
├── scroll_and_screenshot_minimo.py
└── screenshots/
```

---

## Script 1 — `descobrir_coordenadas.py`

### Objetivo

Este script serve para **calibrar manualmente a área da tela** correspondente à janela de mensagens do WhatsApp Web.

Ele captura:
- O canto **superior esquerdo** da área de mensagens
- O canto **inferior direito** da área de mensagens

A partir disso, calcula a região `(x, y, width, height)` que será utilizada no script principal de captura.

---

### Como usar

1. Abra o navegador e acesse o **WhatsApp Web**
2. Abra o grupo cuja conversa será capturada
3. Ajuste o zoom do navegador (recomendado: **100%**)
4. Execute o script:

```bash
python descobrir_coordenadas.py
```

5. Após a mensagem inicial:
   - Posicione o mouse no **canto superior esquerdo** da área da conversa
   - Aguarde o sinal sonoro
6. Em seguida:
   - Posicione o mouse no **canto inferior direito** da área da conversa
   - Aguarde o segundo sinal sonoro

7. O script imprimirá no terminal algo como:

```
Região: x = 476, y = 88, width = 883, height = 626
```

---

### Saída

- Coordenadas da região da conversa
- Esses valores devem ser copiados para a variável `REGION` do script `scroll_and_screenshot_minimo.py`

---

## Script 2 — `scroll_and_screenshot_minimo.py`

### Objetivo

Este script realiza a **captura automatizada do histórico da conversa**, executando:

- Scroll progressivo para cima
- Screenshot da região definida
- Detecção automática do fim do histórico
- Emissão de alerta sonoro ao finalizar

---

### Pré-requisitos

- WhatsApp Web aberto no navegador
- Grupo correto já selecionado
- Janela do navegador **não deve ser redimensionada** durante a execução
- Coordenadas da região (`REGION`) previamente calibradas

---

### Configurações principais

No início do script, ajuste os parâmetros conforme necessário:

- `REGION`: região da conversa (obtida no script anterior)
- `SCROLL_AMOUNT`: quantidade de scroll em pixels
- `WAIT_AFTER_SCROLL`: tempo de espera para carregamento das mensagens
- `DIFF_THRESHOLD`: limiar de diferença entre imagens
- `STABLE_LIMIT`: número de repetições consecutivas para detectar fim do histórico

---

### Como usar

1. Copie os valores de `x`, `y`, `width` e `height` obtidos em `descobrir_coordenadas.py` para a variável `REGION`
2. Certifique-se de que o grupo correto está aberto no WhatsApp Web
3. Execute o script:

```bash
python scroll_and_screenshot_minimo.py
```

4. Após o alerta sonoro inicial:
   - Clique na janela do navegador para garantir o foco

5. O script irá:
   - Capturar screenshots sequenciais
   - Salvar as imagens na pasta `screenshots/`
   - Parar automaticamente ao atingir o início do histórico

6. Um alerta sonoro final indicará o término da captura

---

### Saída

- Série de arquivos PNG numerados sequencialmente:

```
screenshots/
├── chat_00001.png
├── chat_00002.png
├── chat_00003.png
└── ...
```

---

## Observações importantes

- Pequena sobreposição entre imagens é esperada e desejável
- Não interaja com o mouse ou teclado durante a execução
- Emojis, stickers e fundos podem afetar etapas posteriores de OCR

---

## Próximos passos previstos

- Pré-processamento de imagens para OCR
- Extração de texto via Tesseract ou PaddleOCR
- Remoção de duplicações
- Reconstrução do diálogo (timestamps, remetentes)

---

## Aviso ético e legal

Este repositório é disponibilizado **exclusivamente para fins educacionais e de pesquisa**.

O uso do código aqui apresentado deve respeitar:

- Os Termos de Uso do WhatsApp
- A legislação vigente em cada país (incluindo normas de proteção de dados)
- O consentimento explícito das partes envolvidas na conversa

Os autores não se responsabilizam por usos indevidos deste código.

---

## Status do projeto


- [x] Calibração da área da conversa
- [x] Captura automatizada com detecção de fim
- [ ] OCR
- [ ] Pós-processamento textual

