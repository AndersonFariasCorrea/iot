import telebot
import sched
import time

CHAVE_API = "6680158518:AAG1bJvpEAvf69YJNZol4NrYezfz14e27_Y"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["status"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Lixeira em x%")

@bot.message_handler(commands=["start"])
def hamburguer(mensagem):
    s = sched.scheduler(time.time, time.sleep)

    def periodic_task(sc):
        bot.send_message(mensagem.chat.id, "teste interval message")
        
        s.enter(15, 1, periodic_task, (sc,))
        
    s.enter(0, 1, periodic_task, (s,))
        
    s.run()


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /start Inicia um loop que retorna o status da lixeira a cada 15 segundos
     /status Retorna o status da lixeira uma vez
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()