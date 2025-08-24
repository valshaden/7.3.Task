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

import asyncio
from g4f.client import AsyncClient

async def main():
    client = AsyncClient()
    response = await client.images.generate(
        prompt="a white siamese cat",
        model="flux",
        response_format="url"
        # Add any other necessary parameters
    )
    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")

asyncio.run(main())
