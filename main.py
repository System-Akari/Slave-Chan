import os
import pymongo
import telebot
from telebot import types
import time
from libro import libro
import funtions
bot_token = os.environ['TOKEN']
#bot_token='5134352310:AAEqyKKUfWNqt7_DAIHkOrigvvoDBOPi7cI'
bot= telebot.TeleBot(token=bot_token)

varDB=[]

db=funtions.getDB()

AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/notas - Generas los Botones. \nEl resto de comandos están restringidos para usuarios sin permiso:c.\n Firma:Slave-Chan\n'
inicio='Bienvenido honorable miembro de Akari System! Mi nombre es Slave-chan\n y puedo proporcionarte los apuntes de las materias\n que necesites!Utiliza /help para ver los comandos.\n'
infoempel='''Angelo Rafael Velasquez Lara(201923300409\nDany Jose Valdez Escalante(20202300197)\nErick Eduardo Mendoza Tercero(20202300164)\nMary Elizabeth Euceda Molina(20202300170)
\nNestor Dario Aguilera Padilla(20192300030)
'''
@bot.message_handler(commands=['help']) 
def command_ayuda(m): 
 
    cid = m.chat.id 
 
    bot.send_chat_action(cid, 'typing') 
 
    time.sleep(1) 
 
    bot.send_message( cid, AYUDA) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    cid = message.chat.id
    bot.send_message(cid, inicio)

@bot.message_handler(commands=['infoSubEscalvos'])
def info(message):
    cid = message.chat.id
    bot.send_message(cid, infoempel)

@bot.message_handler(commands=['notas'])
def Notas(message):
    markup=types.ReplyKeyboardMarkup(row_width=2)
    btn1=types.KeyboardButton("/BasesDeDatos")
    btn2=types.KeyboardButton("/CircuitosElectrico")
    btn3=types.KeyboardButton("/SistemasOperativos")
    btn4=types.KeyboardButton("/LenguajesDeProgramacion") #el resto los agregare despues 
    #btn5=types.KeyboardButton("/close")
    markup.add(btn1,btn2,btn3,btn4)
    bot.send_message(chat_id=message.chat.id, text="Que Notas Quieres", reply_markup=markup)
    
@bot.message_handler(commands=['LenguajesDeProgramacion'])
def pca_papers4(message):
    cid = message.chat.id
    db=funtions.getDB()
    allOf=db.LP.find()
    time.sleep(1) 
    for i in allOf:
        text=i["fecha"]
        text1=i["link"]
        text=str(text)
        text1=str(text1)
        bot.send_message(cid, text)  
        bot.send_document(message.chat.id, text1)    
    
@bot.message_handler(commands=['CircuitosElectrico'])
def pca_papers3(message):
    cid = message.chat.id
    db=funtions.getDB()
    allOf=db.CE.find()
    time.sleep(1) 
    for i in allOf:
        text=i["fecha"]
        text1=i["link"]
        text=str(text)
        text1=str(text1)
        bot.send_message(cid, text)  
        bot.send_document(message.chat.id, text1)

@bot.message_handler(commands=['BasesDeDatos'])
def pca_papers(message):
    cid = message.chat.id
    db=funtions.getDB()
    allOf=db.DB.find()
    time.sleep(1) 
    for i in allOf:
        bot.send_chat_action(cid, 'typing') 
        text=i["fecha"]
        text1=i["link"]
        text=str(text)
        text1=str(text1)
        bot.send_message(cid, text)  
        bot.send_document(message.chat.id, text1)
           
@bot.message_handler(commands=['SistemasOperativos'])
def pca_papers1(message):
    """cid = message.chat.id 
    bot.send_chat_action(cid, 'typing') 
    time.sleep(1)
    bot.send_document(message.chat.id, varDB[-1])"""
    cid = message.chat.id
    db=funtions.getDB()
    allOf=db.SO.find()
    for i in allOf: 
        text=i["fecha"]
        text1=i["link"]
        text=str(text)
        text1=str(text1)
        bot.send_message(cid, text)  
        bot.send_document(message.chat.id, text1)

@bot.message_handler(commands=['close'])
def close(message):
    markup=types.ReplyKeyboardRemove(selective=False)
    bot.send_message(chat_id=message.chat.id, text="Cerrando", reply_markup=markup)
    
@bot.message_handler(commands=['newAR'])
def send_text(message):
    arr = message.text.split(' ')
    cid = message.chat.id 
    try:
        for i in range(len(arr)):
            if arr[i] == "DB":
                
                varD=arr[i+1]
                varD2=arr[i+2]
                varD=str(varD)
                varD2=str(varD2)
                Nota=libro(varD,varD2)
                funtions.insertNoteDB(Nota.toCollection())
                bot.send_message(cid,"agregado exitosamente")
            elif arr[i]=="SO": 
                varD=arr[i+1]
                varD2=arr[i+2]
                varD=str(varD)
                varD2=str(varD2)
                Nota=libro(varD,varD2)
                funtions.insertNoteSO(Nota.toCollection())
                bot.send_message(cid,"agregado exitosamente")
            elif arr[i]=="CE": 
                varD=arr[i+1]
                varD2=arr[i+2]
                varD=str(varD)
                varD2=str(varD2)
                Nota=libro(varD,varD2)
                funtions.insertNoteCE(Nota.toCollection())
                bot.send_message(cid,"agregado exitosamente")
            elif arr[i]=="LP": 
                varD=arr[i+1]
                varD2=arr[i+2]
                varD=str(varD)
                varD2=str(varD2)
                Nota=libro(varD,varD2)
                funtions.insertNoteLP(Nota.toCollection())
                bot.send_message(cid,"agregado exitosamente")
    except:
        bot.send_message(cid,"Algo fallo")
    finally:
        print("Hubo un fallo")
        
bot.polling()
