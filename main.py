import os
import telebot
import time
bot_token = os.environ['TOKEN']
bot= telebot.TeleBot(token=bot_token)

AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/send - No envia nada. \n/youtube - Manda video random \n/IngDorian - Manda una pagina \n/html - manda un Html \n/Notas - Envia Notas\n'
@bot.message_handler(commands=['ayuda']) 
def command_ayuda(m): 
 
    cid = m.chat.id 
 
    bot.send_chat_action(cid, 'typing') 
 
    time.sleep(1) 
 
    bot.send_message( cid, AYUDA) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Bienvenido Usuario')

@bot.message_handler(commands=['send'])
def send(message):
    bot.reply_to(message, 'No envio nada')

@bot.message_handler(commands=['youtube'])
def twitter(message):
    bot.reply_to(message, 'https://www.youtube.com/watch?v=jhFsFZXZbu4&ab_channel=TechMind')

@bot.message_handler(commands=['IngDorian'])
def Ing(message):
    bot.reply_to(message, 'https://www.w3schools.com/tags/att_input_pattern.asp')

@bot.message_handler(commands=['Notas'])
def Ing(message):
    bot.reply_to(message, 'Aqui tienes tus notas mi amigo'+' https://t.me/randomsaoko/2')

@bot.message_handler(commands=['Archivos'])
def pca_papers(message):
    bot.send_message(message.chat.id, "Files incoming")
    bot.send_document(message.chat.id, 'https://atikegalle.com/uploads/1514125303.pdf')

bot.polling()
