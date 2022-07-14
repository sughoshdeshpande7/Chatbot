from chatterbot import ChatBot
chatbot=ChatBot('Charlie',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
               logic_adapter=['chatterbot.logic.MathematicalEvaluation',
                             'chatterbot.logic.TimeLogicAdapter',
                             'chatterbot.logic.BestMatch',
                             {
                                 'import_path':'chatterbot.logic.BestMatch',
                                 'default_response':'I am sorry,I do not understand',
                                 'maximum_similarity_threshold':0.90
                             }
                        ],
               database_uri='sqlite:///database.sqlite3'
               )
               
from chatterbot.trainers import ChatterBotCorpusTrainer
trainercorpus=ChatterBotCorpusTrainer(chatbot)
trainercorpus.train('chatterbot.corpus.english')

import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
name=input("Enter your name:")
print('Hello',name,'Hope you are doing well! How can i help you?')
while True:
    request=input(name+':')
    if request=='Bye' or request=='bye':
        print('Bot: Bye',name,'! Have a Great Time Ahead!')
        break
