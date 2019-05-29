from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
from random import randint
token = "d2b30d2d8194414bb292d20b02c797b11f72fbed397bedebf628c103e8ea762a35e4a586cfa5be7c7da31"
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print("Сообщение пришло в " + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print("Текст сообщения:", event.text)
            print("От: ", event.user_id)
            response = event.text.lower()
            if response == "беседа":
                vk_session.method("message.send", {"user_id": event.user_id, "message": "Заполни анкету", "random_id": randint})
