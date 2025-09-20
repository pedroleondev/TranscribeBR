# Audio Text Processor

This project is designed to process various audio and text files. It converts audio files to a 16kHz mono WAV format, transcribes the audio using GPU capabilities, formats the transcriptions to HTML, and then converts the HTML to a formatted PDF. The output includes both a formatted PDF and a simple TXT file with UTF-8 line breaks.

## Project Structure

```
audio_text_processor
├── src
│   ├── __init__.py
│   ├── audio
│   │   ├── __init__.py
│   │   ├── converter.py
│   │   └── transcriber.py
│   ├── text
│   │   ├── __init__.py
│   │   ├── formatter.py
│   │   └── pdf_generator.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── file_utils.py
│   └── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd audio_text_processor
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your audio files in supported formats (.mp4, .m4a, .mp3, .wav).
2. Update the `.env` file with the necessary paths for input and output directories.
3. Run the main application:
   ```
   python src/main.py
   ```

## Functionality

- **Audio Conversion**: Converts various audio formats to 16kHz mono WAV format.
- **Transcription**: Utilizes GPU for efficient transcription of audio files.
- **Text Formatting**: Formats transcribed text into HTML for better presentation.
- **PDF Generation**: Converts formatted HTML into a well-structured PDF document.
- **Output**: Saves the transcriptions in both PDF and simple TXT formats.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.