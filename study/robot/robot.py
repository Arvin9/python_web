# -*- coding:utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from ne_util import network_utils
import time

chatbot = ChatBot(
        "Nebula",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database='./database.sqlite3'
    )

def train(ask, ret):
    conversation = [
        ask,
        ret
    ]

    chatbot.set_trainer(ListTrainer)
    chatbot.train(conversation)

def tuling(text):
    BASE_URL = "http://openapi.tuling123.com/openapi/api/v2"
    body = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": text
            }
        },
        "userInfo": {
            "apiKey": "72307a3ae94c424381b2a023a9df3520",
            "userId": "1"
        }
    }
    return network_utils.post(BASE_URL, body)


if __name__ == '__main__':

    response = chatbot.get_response("啦啦啦")
    print(response)
    ask_text = "你是谁"

    # while True:
    #     try:
    #         print("ask_text: ", ask_text)
    #         tuling_response = tuling(ask_text)
    #         print("tuling_response:", tuling_response)
    #         ret_text = tuling_response['results'][0]['values']['text']
    #         print("ret_text", ret_text)
    #
    #         train(ask_text, ret_text)
    #
    #         bot_input = chatbot.get_response(ask_text)
    #         ask_text = ret_text
    #         print("rebot_ret:", bot_input)
    #         print("======")
    #         time.sleep(1)
    #     except(Exception):
    #         print("error")
    #         ask_text = "你是谁"