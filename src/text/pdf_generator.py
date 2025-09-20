def generate_pdf(html_content: str, output_pdf_path: str):
    from weasyprint import HTML

    # HTML template com cabeçalho e estilos
    html_template = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
            }}
            .header {{
                border-bottom: 2px solid #444;
                margin-bottom: 30px;
                padding-bottom: 10px;
            }}
            .header-title {{
                font-size: 1.8em;
                font-weight: bold;
                color: #222;
            }}
            .header-subtitle {{
                font-size: 1.1em;
                color: #555;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="header-title">Transcrição por TranscriberBR</div>
            <div class="header-subtitle">Por Pedro Leon</div>
        </div>
        {html_content}
    </body>
    </html>
    """

    # Generate PDF from HTML template
    HTML(string=html_template).write_pdf(output_pdf_path)

def main():
    # Example usage
    html_content = "<h1>Transcrição</h1><p>This is a sample transcription.</p>"
    output_pdf_path = "output/transcription.pdf"
    
    generate_pdf(html_content, output_pdf_path)
    print(f"PDF gerado. Caminho: {output_pdf_path}")

if __name__ == "__main__":
    main()