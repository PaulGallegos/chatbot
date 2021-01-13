from ChatBotBrain import ChatBotBrain
from Api import Api
import re

class ChatBot:
    def __init__(self, context, seed, model, tokenizer, first_message):
        self.brain = ChatBotBrain(context, seed, model, tokenizer)
        self.first_message = first_message
        self.init_answers()
        self.api = Api()

    def run(self):
        while True:
            dictionary = self.api.update(self.api.last_message)
            for m in dictionary['result']:
                id_chat, user, question, id_update = self.api.read_messages(m)

                if id_update > (self.api.last_message-1):
                    self.api.last_message = id_update + 1

                if self.filter_question(question.lower(), id_chat):
                    self.api.send_message(id_chat, self.brain.talk(question))
                    # print('RoboTec dice >>', self.brain.talk(question))

    def filter_question(self, question, id_chat):
        for answer in self.answers:
            pattern = answer[0]
            p = re.compile(pattern)
            if not p.search(question.lower()) is None:
                self.api.send_message(id_chat, answer[1])
                # print('RoboTec dice >>', answer[1])
                return False
        return True
        

    def init_answers(self):
        self.answers = [
            (
                '(.*)telefono(.*)escuela(.*)',
                'el telefono es 3111421169'
            ),
            (
                '(.*)gg(.*)f(.*)',
                'parece que jala xd'
            ),
            (
                'hola',
                self.first_message
            )
        ]
