import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

# Функция для загрузки видео
def download_video():
    link = link_entry.get()
    save_path = filedialog.askdirectory()

    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download(save_path)
    status_label.config(text='Видео загружено')

# Создаем основное окно
root = tk.Tk()
root.title('Загрузчик видео с YouTube')

# Создаем и размещаем элементы интерфейса
label = tk.Label(root, text='Введите ссылку на видео:')
label.pack()

link_entry = tk.Entry(root, width=50)
link_entry.pack()

download_button = tk.Button(root, text='Скачать видео', command=download_video)
download_button.pack()

status_label = tk.Label(root, text='')
status_label.pack()

root.mainloop()
