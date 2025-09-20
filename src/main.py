import os
import sys
from audio.converter import convert_to_wav
from audio.transcriber import transcribe_audio
from text.formatter import format_to_html
from text.pdf_generator import generate_pdf
from utils.file_utils import is_valid_file
from utils.download_utils import is_youtube, is_instagram, baixar_youtube, baixar_instagram, converter_para_wav

def main():
    input_files = sys.argv[1:]  # Get input files from command line arguments
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for input_file in input_files:
        # Se for link do YouTube
        if is_youtube(input_file):
            print(f"🔗 Baixando do YouTube: {input_file}")
            wav_file = baixar_youtube(input_file, output_dir)
        # Se for link do Instagram
        elif is_instagram(input_file):
            print(f"🔗 Baixando do Instagram: {input_file}")
            video_file = baixar_instagram(input_file, output_dir)
            wav_file = converter_para_wav(video_file, output_dir)
        # Se for arquivo local
        elif is_valid_file(input_file):
            wav_file = convert_to_wav(input_file, output_dir)
        else:
            print(f"🚨 Caminho inválido ou link não suportado: {input_file}")
            continue

        print(f"🎧 Arquivo WAV pronto: {wav_file}")

        # Transcrição e geração de arquivos
        transcribed_text = transcribe_audio(wav_file)
        print("📝 Transcription completed.")

        html_content = format_to_html(transcribed_text)
        print("📄 Formatted text to HTML.")

        pdf_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(input_file))[0]}.pdf")
        generate_pdf(html_content, pdf_file)
        print(f"✅ PDF generated: {pdf_file}")

        txt_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(input_file))[0]}.txt")
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(transcribed_text)
        print(f"✅ Transcription saved as TXT: {txt_file}")

    print("🎉 Process completed for all files.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file1> <input_file2> ...")
        sys.exit(1)

    main()