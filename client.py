import socket
import telebot


CHAVE_API = "6680158518:AAG1bJvpEAvf69YJNZol4NrYezfz14e27_Y"

bot = telebot.TeleBot(CHAVE_API)


def get_status(query):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.3.101', 8080))
    client.send(query.encode())
    from_server = client.recv(4096)
    client.close()
    return str(from_server.decode())


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    board_return =  get_status("{\"action\": \"status\"}")
    if board_return is None:
        board_return = 'Aconteceu um erro interno!'
    bot.reply_to(mensagem, board_return)


bot.polling()


# adicionar metodo de banco para salvar dados sobre a placa
