import tkinter as tk
from tkinter import scrolledtext, messagebox
import lyricsgenius

# Replace with your Genius API Token
GENIUS_API_TOKEN = "AEjuzKtEgj1UPXj-IiekMHlVe_5OEfWcdVSsGgle8UxFNIYuYWdB5DgwPlfmuTzH"
genius = lyricsgenius.Genius(GENIUS_API_TOKEN)

def get_lyrics():
    artist = artist_entry.get().strip()
    song = song_entry.get().strip()
    if not artist or not song:
        messagebox.showwarning("Input Error", "Please enter both artist and song name.")
        return
    
    try:
        song_data = genius.search_song(song, artist)
        if song_data:
            lyrics_text.config(state=tk.NORMAL)
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, song_data.lyrics)
            lyrics_text.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Not Found", "Lyrics not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch lyrics: {e}")

# Creating the GUI window
root = tk.Tk()
root.title("Lyrics Finder")
root.geometry("500x600")

# Labels and Entry Fields
tk.Label(root, text="Artist Name:").pack()
artist_entry = tk.Entry(root, width=40)
artist_entry.pack()

tk.Label(root, text="Song Name:").pack()
song_entry = tk.Entry(root, width=40)
song_entry.pack()

# Fetch Lyrics Button
fetch_button = tk.Button(root, text="Get Lyrics", command=get_lyrics)
fetch_button.pack(pady=10)

# Lyrics Display Area
lyrics_text = scrolledtext.ScrolledText(root, width=60, height=20, state=tk.DISABLED)
lyrics_text.pack()

# Run the application
root.mainloop()