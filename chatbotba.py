from nltk.chat.util import Chat, reflections
mis_reflexions = {
"ir": "fui",
"hola": "hey"
}

pares = [
    [
        r"(.*) donde|ubicacion (.*) Baston (.*)",
        ["El baston de encuentra, entrando por la entrada principal de peatones, el primer edificio a la izquierda, Ademas te dejo la ubicacion por si quieres buscarlo en google maps: https://goo.gl/maps/U4q71uFA3xBJ7QD36 "]
    ],
     [
        r"cuando hay que pagar la factura (.*)",
        ["Hay que pagarla el dia 15 de cada mes por tarjeta de crédito",]
    ],
    [
        r"(.*) ampliar el servicio",
        ["Para ampliar el servicio, contacta con facturacion"]
    ],
    [
        r"disculpa (.*)",
        ["https://goo.gl/maps/Bh46jB2FpMgL7GHG6",]
    ],
    [
        r"hola|hey|buenas",
        ["el priemr edificio a la izquierda por la entrada principal, \n ademas te dejamos la ubicacion: https://goo.gl/maps/Bh46jB2FpMgL7GHG6", "Que tal",]
    ],
    [
        r"(.*) baño (.*) baston (.*)",
        ["no este chingando y vaya a surrar a su casa"]
        
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],
    [
        r"finalizar",
        ["Chao","Fue bueno hablar contigo"]
],
]
def chatear():
    print("Hola, soy el servicio de hosting") #mensaje por defecto
    chat = Chat(pares, mis_reflexions)
    chat.converse()
if __name__ == "__main__":
    chatear()

chatear()