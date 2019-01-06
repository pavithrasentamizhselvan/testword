from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot=ChatBot('Test')
con=open('C:\\Users\\swami\\Documents\\bot.txt').readlines()
bot.set_trainer(ListTrainer)
bot.train(con)
while True:
    req=input("you: ")
    res=bot.get_response(req)
    print('bot: ',res)
con.close()
