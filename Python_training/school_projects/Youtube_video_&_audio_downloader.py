import os
import threading
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from yt_dlp import YoutubeDL

# Function to select download location
def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

# Function to update the progress bar
def hook(d):
    if d['status'] == 'downloading':
        total_size = d.get('total_bytes') or d.get('total_bytes_estimate')
        if total_size is not None:
            percentage = d['downloaded_bytes'] / total_size * 100
            progress_var.set(percentage)
            progress_bar.update_idletasks()
            progress_label.config(text=f"Progress: {percentage:.2f}% ({d['downloaded_bytes'] / (1024*1024):.2f} MB / {total_size / (1024*1024):.2f} MB)")
    elif d['status'] == 'finished':
        progress_label.config(text="Download complete!")
        progress_var.set(100)
        messagebox.showinfo("Success", "Download complete!")
        reset_progress_bar()

# Function to reset the progress bar
def reset_progress_bar():
    progress_var.set(0)
    progress_label.config(text="Progress: 0%")

# Function to start download
def start_download():
    url = url_entry.get()
    folder = folder_path.get()
    format_choice = format_var.get()

    if not url or not folder:
        messagebox.showerror("Error", "Please enter a valid URL and select a folder.")
        return

    # Set options for downloading video, audio, or both
    if format_choice == 'Video only':
        ydl_opts = {
            'format': 'bestvideo',
            'outtmpl': os.path.join(folder, '%(title)s_video.%(ext)s'),
            'progress_hooks': [hook],
            'noplaylist': True,
        }
    elif format_choice == 'Audio only':
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': os.path.join(folder, '%(title)s_audio.%(ext)s'),
            'progress_hooks': [hook],
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    elif format_choice == 'Video + Audio':  # Merging video + audio
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
            'progress_hooks': [hook],
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }

    # Run the download in a separate thread
    def download(ydl_opts):
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    reset_progress_bar()
    threading.Thread(target=download, args=(ydl_opts,)).start()

# GUI Application Setup
root = Tk()
root.title("YouTube Downloader (Video/Audio)")
root.geometry("600x550")
root.config(bg="#f0f0f0")

# Variables
folder_path = StringVar()
progress_var = DoubleVar()

# URL input
Label(root, text="Enter YouTube URL:", bg="#f0f0f0").pack(pady=10)
url_entry = Entry(root, width=50)
url_entry.pack(pady=5)

# Download type selection (Audio/Video/Video+Audio)
format_var = StringVar(value="Video + Audio")
Label(root, text="Select format:", bg="#f0f0f0").pack(pady=5)
Radiobutton(root, text="Video only", variable=format_var, value="Video only", bg="#f0f0f0").pack()
Radiobutton(root, text="Audio only", variable=format_var, value="Audio only", bg="#f0f0f0").pack()
Radiobutton(root, text="Video + Audio", variable=format_var, value="Video + Audio", bg="#f0f0f0").pack()

# Select folder
Label(root, text="Select download folder:", bg="#f0f0f0").pack(pady=10)
Button(root, text="Browse", command=select_folder).pack()
folder_label = Label(root, textvariable=folder_path, bg="#f0f0f0")
folder_label.pack(pady=5)

# Download button
Button(root, text="Download", command=start_download, bg="#4CAF50", fg="white").pack(pady=10)

# Progress bar and label
progress_bar = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate', variable=progress_var, maximum=100)
progress_bar.pack(pady=20)
progress_label = Label(root, text="Progress: 0%", bg="#f0f0f0")
progress_label.pack()

# Exit button
Exit_button = Button(root, text='Exit', command=root.destroy, width=15, padx=10, bg='red')
Exit_button.pack(pady=11)

root.mainloop()
