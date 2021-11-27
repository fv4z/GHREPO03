from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot('robot')

conversa = ['Oi',
            'Olá',
            'Tudo bem?',
            'Tudo ótimo',
			'Você gosta de programar?',
            'Sim, eu programo em Python'
            ]

trainer = ListTrainer(bot)
trainer.train(conversa)

#while True:
#    pergunta = input("Usuário: ")
#    resposta = bot.get_response(pergunta)
#    if float(resposta.confidence) > 0.5:
#        print('Robot: ', resposta)
#    else:
#        print('Robot: Ainda não manjo essas paradas')

