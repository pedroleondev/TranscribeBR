-----

# TranscribeBR

Ferramenta para transcrição de arquivos de áudio para texto em PDF.

Este projeto processa diversos arquivos de áudio e texto. Ele converte arquivos de áudio para o formato WAV mono de 16kHz, transcreve o áudio (utilizando GPU, se disponível), formata as transcrições para HTML e, por fim, converte o HTML para um PDF formatado. A saída inclui tanto o PDF formatado quanto um arquivo `.txt` simples (com quebras de linha UTF-8).

## Estrutura do Projeto

```
audio_text_processor
├── src
│   ├── __init__.py
│   ├── audio
│   │   ├── __init__.py
│   │   ├── converter.py
│   │   └── transcriber.py
│   ├── text
│   │   ├── __init__.py
│   │   ├── formatter.py
│   │   └── pdf_generator.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── file_utils.py
│   └── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Instalação

1.  Clone o repositório:

    ```
    git clone <url-do-repositorio>
    cd audio_text_processor
    ```

2.  Crie um ambiente virtual (virtual environment):

    ```
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  Instale os pacotes necessários:

    ```
    pip install -r requirements.txt
    ```

## Uso

1.  Prepare seus arquivos de áudio nos formatos suportados (.mp4, .m4a, .mp3, .wav).
2.  Atualize o arquivo `.env` com os caminhos necessários para os diretórios de entrada (input) e saída (output).
3.  Execute a aplicação principal:
    ```
    python src/main.py
    ```

## Funcionalidades

  - **Conversão de Áudio**: Converte vários formatos de áudio para o formato WAV mono de 16kHz.
  - **Transcrição**: Utiliza GPU (se disponível) para transcrição eficiente de arquivos de áudio.
  - **Formatação de Texto**: Formata o texto transcrito em HTML para melhor apresentação.
  - **Geração de PDF**: Converte o HTML formatado em um documento PDF bem estruturado.
  - **Saída (Output)**: Salva as transcrições nos formatos PDF e TXT simples.

## Contribuição

Contribuições são bem-vindas\! Sinta-se à vontade para enviar um pull request ou abrir uma issue para sugestões ou melhorias.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

-----

*Pedro Leon Dev Python*
