import tkinter as tk
from pytube import YouTube
from tkinter import messagebox
from tkinter import ttk
import threading

def download_video():
    try:
        video_url = url_entry.get()
        yt = YouTube(video_url)
        stream = yt.streams.filter(file_extension=file_type.get(), res=quality.get()).first()

        download_thread = threading.Thread(target=download_with_progress, args=(stream,))
        download_thread.start()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def download_with_progress(stream):
    download_button.config(state=tk.DISABLED)
    progress_bar.start()

    try:
        stream.download()
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

    progress_bar.stop()
    download_button.config(state=tk.NORMAL)

# GUI setup
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x300")
root.configure(bg="#1f1f1f")  # Dark background color

# URL Entry
url_label = tk.Label(root, text="Enter YouTube URL:", fg="#00FFFF", bg="#1f1f1f")  # Cyan blue neon color
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50, bg="#2a2a2a", fg="#00FFFF", insertbackground="#00FFFF")  # Dark background and cyan blue neon color
url_entry.pack(pady=10)

# Quality selection
quality_label = tk.Label(root, text="Select Quality:", fg="#00FFFF", bg="#1f1f1f")
quality_label.pack()

quality = tk.StringVar(root)
quality.set("720p")  # Default quality

quality_options = ["144p", "240p", "360p", "480p", "720p", "1080p"]
quality_dropdown = tk.OptionMenu(root, quality, *quality_options)
quality_dropdown.config(bg="#2a2a2a", fg="#00FFFF")  # Dark background and cyan blue neon color
quality_dropdown.pack(pady=10)

# File type selection
file_type_label = tk.Label(root, text="Select File Type:", fg="#00FFFF", bg="#1f1f1f")
file_type_label.pack()

file_type = tk.StringVar(root)
file_type.set("mp4")  # Default file type

file_type_options = ["mp4", "webm"]
file_type_dropdown = tk.OptionMenu(root, file_type, *file_type_options)
file_type_dropdown.config(bg="#2a2a2a", fg="#00FFFF")  # Dark background and cyan blue neon color
file_type_dropdown.pack(pady=10)

# Download button
download_button = tk.Button(root, text="Download", command=download_video, bg="#00FFFF", fg="#1f1f1f")  # Cyan blue neon button
download_button.pack(pady=20)

# Progress bar
progress_bar = ttk.Progressbar(root, mode="indeterminate", length=300)
progress_bar.pack(pady=10)

root.mainloop()
