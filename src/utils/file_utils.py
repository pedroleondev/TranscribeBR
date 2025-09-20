import os

def is_valid_file(file_path: str) -> bool:
    valid_extensions = ('.mp3', '.m4a', '.mp4', '.wav', '.txt')
    return os.path.isfile(file_path) and file_path.lower().endswith(valid_extensions)

def read_urls_from_txt(file_path: str) -> list:
    if not is_valid_file(file_path):
        raise ValueError("Invalid file path or file type. Please provide a valid .txt file.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls