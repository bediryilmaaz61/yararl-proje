from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import os

# path seçtiren fonmksion

def select_directory():
    path_select = filedialog.askdirectory()
    path_label.config(text=path_select)


#indirme işlemşi yapan fonksiyon
def download_file():
    link=link_field.get()
    yt=YouTube(link)
    folder= path_label.cget("text")
    uzanti =cmb.get()

    if uzanti == ".mp3" :

        mp3 = yt.streams.filter(only_audio=True).first()
        output =mp3.download(folder)
        base,ext = os.path.splitext(output)
        to_mp3 = base + ".mp3"
        os.rename(output,to_mp3)
    elif uzanti == ".mp4" :
        mp4 = yt.streams.get_highest_resolution().download(folder)

#screen aarları

screen =Tk()
screen.iconbitmap(default="youtube.ico")
title = screen.title("Youtube İndirici")
canvas = Canvas(screen,width=500,height=500)
canvas.pack()

#youtube logosu

yt_logo = PhotoImage(file="youtube.png")
canvas.create_image(250,80,image=yt_logo)
#link alanı

link_field = Entry(screen,width=50)
link_label = Label(screen,text="Link Giriniz",font=("Helvetica",12,BOLD),fg="#911b13")

canvas.create_window(250,175,window=link_label)
canvas.create_window(250,220,window=link_field)

#path alanı

path_label = Label(screen,text="...",font=("Helvetica",12,BOLD),fg="#4c8712")
canvas.create_window(250,260,window=path_label)

path_button = Button(screen,text="Konum Seciniz",fg="white",bg="#911b13",command=select_directory)
canvas.create_window(250,300,window=path_button)

#extension alanı
ayarlar = [
    ".mp3",
    ".mp4"
]
cmb = ttk.Combobox(screen,value=ayarlar,width=10)
canvas.create_window(250,350,window=cmb)

#download button
download_button = Button(screen,text="download",fg="white",bg="#911b13",command=download_file)
canvas.create_window(250,400,window=download_button)


screen.mainloop()