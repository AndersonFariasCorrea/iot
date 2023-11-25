import socket
import telebot

CHAVE_API = "6680158518:AAG1bJvpEAvf69YJNZol4NrYezfz14e27_Y"

bot = telebot.TeleBot(CHAVE_API)


def get_response(query):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.3.101', 8080))
    client.send(query.encode())
    from_server = client.recv(4096)
    client.close()
    return str(from_server.decode())

@bot.message_handler(commands=["start"])
def opcao3(mensagem):
    board_return =  get_response("{\"action\": \"start_or_restart\"}")
    if board_return is None:
        board_return = 'Aconteceu um erro interno!'
    bot.send_message(mensagem.chat.id, board_return)


@bot.message_handler(commands=["status"])
def opcao3(mensagem):
    board_return =  get_response("{\"action\": \"status\"}")
    if board_return is None:
        board_return = 'Aconteceu um erro interno!'
    bot.send_message(mensagem.chat.id, board_return)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    start_message = """
    Escolha uma opção para continuar (Clique no item):
     /start - restart Inicia ou reinicia a lixeira (deve estar vazia)
     /status Consulta a situação da lixeira
Responder qualquer outra coisa não vai funcionar, clique ou digite uma das opções"""
    bot.reply_to(mensagem, start_message)

bot.polling()


# adicionar metodo de banco para salvar dados sobre a placa
