# 7.3. Задание
## Доработайте проект, который генерирует изображение с помощью ИИ. 
## Добавьте в проект интерфейс tkinter. Пользователь должен вводить запрос 
## в поле ввода и нажимать на кнопку "Отправить". Изображение, сгенерированное 
## по ссылке, должно открываться в отдельном вторичном окне. 
#Код проекта:
#import asyncio
#from g4f.client import AsyncClient
#def main():
#    client = AsyncClient()
#    response = await client.images.generate(
#        prompt="a white siamese cat",
#        model="flux",
#        response_format="url"
#        # Add any other necessary parameters
#    )
#    image_url = response.data[0].url
#    print(f"Generated image URL: {image_url}")
#asyncio.run(main())

from g4f.client import AsyncClient
import asyncio
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((640, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None

async def generate_image(prompt):
    client = AsyncClient()
    response = await client.images.generate(
        prompt=prompt,
        model="flux",
        response_format="url"
    )
    return response.data[0].url

def open_new_window():
    prompt = prompt_entry.get()
    if not prompt:
        return
    
    def run_async():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            image_url = loop.run_until_complete(generate_image(prompt))
            img = load_image(image_url)
            if img:
                new_window = Toplevel()
                new_window.title("Generated Image")
                new_window.geometry("600x480")
                label = Label(new_window, image=img)
                label.image = img
                label.pack()
        finally:
            loop.close()
    
    threading.Thread(target=run_async, daemon=True).start()

def exit_app():
    window.destroy()

window = Tk()
window.title("AI Image Generator")
window.geometry("300x200")

label = Label(window)
label.pack()

# Создаем меню
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Добавляем пункты меню
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Генерировать изображение", command=open_new_window)

file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_app)

# Поле ввода для запроса
prompt_entry = Entry()
prompt_entry.pack()

# Кнопка для генерации изображения
generate_button = Button(text="Отправить", command=open_new_window)
generate_button.pack()

window.mainloop()

