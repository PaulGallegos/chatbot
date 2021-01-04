from ChatBotBrain import ChatBotBrain
import re

class ChatBot:
    def __init__(self, context, seed, model, tokenizer, first_message):
        self.brain = ChatBotBrain(context, seed, model, tokenizer)
        self.first_message = first_message
        self.init_answers()

    def run(self):
        print('RoboTec dice >>', self.first_message)
        while True:
            question = input('>> ')
            if self.filter_question(question):
                print('RoboTec dice >>', self.brain.talk(question))

    def filter_question(self, question):
        for answer in self.answers:
            pattern = answer[0]
            p = re.compile(pattern)
            if not p.search(question) is None:
                print('RoboTec dice >>', answer[1])
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
        ]
