import os
import re
import subprocess

def baixar_youtube(url, output_dir):
    from yt_dlp import YoutubeDL
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s-%(id)s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "prefer_ffmpeg": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "0",
            }
        ],
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title", "audio")
        video_id = info.get("id", "")
        wav_path = os.path.join(output_dir, f"{title}-{video_id}.wav")
        return wav_path

def baixar_instagram(url, output_dir):
    import instaloader
    expr = r'\/p\/([^\/]*)/'
    found = re.search(expr, url)
    if not found:
        raise ValueError("URL do Instagram inválida.")
    shortcode = found.group(1)
    loader = instaloader.Instaloader(
        download_pictures=False,
        download_videos=True,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False,
        dirname_pattern=output_dir,
        filename_pattern='{profile}_{mediaid}'
    )
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, output_dir)
    # Procura o arquivo mp4 baixado
    for file in os.listdir(output_dir):
        if file.endswith(".mp4") and shortcode in file:
            return os.path.join(output_dir, file)
    raise FileNotFoundError("Vídeo do Instagram não encontrado.")

def is_youtube(url):
    return "youtube.com" in url or "youtu.be" in url

def is_instagram(url):
    return "instagram.com" in url

def converter_para_wav(input_path, output_dir):
    # Converte qualquer vídeo para wav 16kHz mono
    base = os.path.splitext(os.path.basename(input_path))[0]
    wav_path = os.path.join(output_dir, f"{base}_16k.wav")
    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        wav_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    return wav_path