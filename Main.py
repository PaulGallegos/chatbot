from ChatBot import ChatBot

context = """who are you?
My name is RoboTec, I'm a robot from the future, I'm very grumpy, and I like programming"""

first_message = """Hola, mi nombre es RoboTec y estoy aquí para ayudarte
en lo que necesites saber sobre el tec. ¿En qué te puedo ayudar?"""

seed = 44
tokenizer = model = 'microsoft/DialoGPT-large'

if __name__ == "__main__":
    ChatBot(context, seed, model, tokenizer, first_message).run()