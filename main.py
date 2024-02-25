import time
from time import sleep
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import SpotifyClientCredentials

from tkinter import *
from tkinter import ttk
from tkinterhtml import HtmlFrame
from tkhtmlview import HTMLLabel, RenderHTML

load_dotenv()

scope = "user-read-playback-state"

user = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

while True:
    # issue: timestamp is not updated every call, only when something changes. due to this, if the user seeks in the song, the timestamp will be off
    
    result = user.currently_playing()
    print(time.time()*1000 - result["timestamp"])
    print(result["item"]["name"] if result["is_playing"] else "Not playing")
    sleep(3)

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

root = Tk()
root.title("Feet to Meters")

label = HTMLLabel(root, html=RenderHTML("index.html"))
label.pack(pady=10, padx=10)


# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): 
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

root.mainloop()