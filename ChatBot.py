from ChatBotBrain import ChatBotBrain

class ChatBot:
    def __init__(self, context, seed, model, tokenizer, first_message):
        self.brain = ChatBotBrain(context, seed, model, tokenizer)
        self.first_message = first_message

    def run(self):
        print('RoboTec dice >>', self.first_message)
        while True:
            question = input('>> ')
            print('RoboTec dice >>', self.brain.talk(question))