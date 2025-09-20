def format_to_html(transcribed_text: str) -> str:
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Transcription</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
            }}
            h1 {{
                color: #333;
            }}
            p {{
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        <h1>Transcription</h1>
        <p>{transcribed_text.replace('\n', '</p><p>')}</p>
    </body>
    </html>
    """
    return html_content