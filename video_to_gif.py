import subprocess
import os

def video_to_gif(video_file, output_gif, fps=5, scale=640):
    """
    Convierte un video a GIF usando ffmpeg
    
    Args:
        video_file: ruta del video de entrada
        output_gif: ruta del GIF de salida
        fps: fotogramas por segundo
        scale: ancho del GIF en píxeles
    """
    
    # Verificar si ffmpeg está instalado
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Error: ffmpeg no está instalado o no está en el PATH")
        print("Instala ffmpeg desde: https://ffmpeg.org/download.html")
        return False
    
    # Verificar si el video existe
    if not os.path.exists(video_file):
        print(f"Error: el archivo '{video_file}' no existe")
        return False
    
    print(f"Convirtiendo {video_file} a GIF...")
    
    # Comando ffmpeg
    cmd = [
        "ffmpeg",
        "-i", video_file,
        "-vf", f"fps={fps},scale={scale}:-1:flags=lanczos",
        "-y",  # Overwrite output file
        output_gif
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✓ GIF creado exitosamente: {output_gif}")
        return True
    except subprocess.CalledProcessError:
        print("Error al convertir el video")
        return False

if __name__ == "__main__":
    video_to_gif("demo.mp4", "demo.gif", fps=10, scale=640)
