import typing
from .settings import *

from .root import chat

@app.post("/submit")
async def submit(text: typing.Annotated[bytes, fastapi.Form()]):
    """
        ОПИСАНИЕ ДЛЯ ЧАЙНИКОВ:\n
            submit вызовется при отправке формы (form) по адресу http://localhost:8000/submit, и функция, извлеча данные из объекта формы, добавит их в историю чата. Попытка открытия ссылки в браузере, вероятнее всего, приведет к ошибке.
        \nАргументы:
            text является fastapi.Form(), заанотированным (ну типа как соединенным) с bytes и представляет собой поле ввода с именем text (см. templates/index.html строка 11).
        \nВозвращает:
            После добавления сообщения в историю отправляет клиента на главную страницу.
    """

    chat.append(text.decode())
    return fastapi.responses.RedirectResponse("/", 303)