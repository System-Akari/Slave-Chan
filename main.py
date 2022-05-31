import os
import telebot
import time
bot_token = os.environ['TOKEN']
bot= telebot.TeleBot(token=bot_token)

AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/send - No envia nada. \n/youtube - Manda video random \n/IngDorian - Manda una pagina \n/html - manda un Html \n/Notas - Envia Notas\n'
@bot.message_handler(commands=['ayuda']) # Indicamos que lo siguiente va a controlar el comando '/ayuda'
def command_ayuda(m): # Definimos una función que resuleva lo que necesitemos.
 
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
 
    bot.send_chat_action(cid, 'typing') # Enviando ...
 
    time.sleep(1) #La respuesta del bot tarda 1 segundo en ejecutarse
 
    bot.send_message( cid, AYUDA) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.

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
    bot.reply_to(message, 'Aqui tienes tus notas'+' https://t.me/randomsaoko/2')

@bot.message_handler(commands=['html'])
def html(message):
    bot.reply_to(message, """ <!DOCTYPE html>
<html>
<body>

<h1>The input pattern attribute</h1>

<form action="/action_page.php">
  <label for="country_code">Country code:</label>
  <input type="text" id="country_code" name="country_code" pattern="[+][5][0][4]\s[2389][1-9][0-9]{2}[-][0-9]{4}" required title="Three letter country code"><br><br>
  <input type="submit">
</form>

<p><strong>Note:</strong> The pattern attribute of the input tag is not supported in Safari 10 (or earlier).</p>

</body>
</html>

""")

bot.polling()
