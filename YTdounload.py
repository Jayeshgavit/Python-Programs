from pytube import YouTube
import os
import subprocess

def download_youtube_video():
    # Get URL input from the user
    video_url = input("Enter the YouTube video URL: ")
    
    try:
        # Create YouTube object
        yt = YouTube(video_url)
        
        # Display the title of the video
        print(f"Video Title: {yt.title}")
        
        # Select the highest resolution video-only stream (1080p)
        video_stream = yt.streams.filter(res="1080p", progressive=False, file_extension="mp4").first()
        if not video_stream:
            print("1080p resolution not available for this video.")
            return
        
        # Select the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
        
        # Set output directory
        output_dir = "downloads"
        os.makedirs(output_dir, exist_ok=True)
        
        # Download video-only and audio streams
        print("Downloading video...")
        video_file = video_stream.download(output_path=output_dir, filename="video.mp4")
        
        print("Downloading audio...")
        audio_file = audio_stream.download(output_path=output_dir, filename="audio.mp4")
        
        # Combine video and audio using ffmpeg
        output_file = os.path.join(output_dir, f"{yt.title}.mp4")
        print("Combining video and audio...")
        
        ffmpeg_command = [
            "ffmpeg", "-i", video_file, "-i", audio_file,
            "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", output_file
        ]
        subprocess.run(ffmpeg_command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        
        # Clean up temporary files
        os.remove(video_file)
        os.remove(audio_file)
        
        print(f"Download complete! Saved as: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
download_youtube_video()
