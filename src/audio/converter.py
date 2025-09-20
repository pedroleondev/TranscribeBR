import os
import subprocess

def convert_to_wav(input_file_path: str, output_dir: str) -> str:
    """
    Converts various audio file formats to 16kHz mono WAV format.
    
    Parameters:
        input_file_path (str): The path to the input audio file.
        output_dir (str): The directory where the output WAV file will be saved.
    
    Returns:
        str: The path to the converted WAV file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_name = os.path.splitext(os.path.basename(input_file_path))[0]
    output_file_path = os.path.join(output_dir, f"{base_name}_16k.wav")

    cmd = [
        "ffmpeg", "-y",
        "-i", input_file_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        output_file_path
    ]
    
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    return output_file_path