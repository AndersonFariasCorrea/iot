import socket
import re

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)

distancia = 1

def get_query(input):
  pattern = r'"([^"]*)"'
  result = re.findall(pattern, input)
  return result

while True:
  conn, addr = serv.accept()
  from_client = ''
  
  while True:
    data = conn.recv(4096)
    if not data: break
    from_client += data.decode('utf8')
    from_client = get_query(from_client)
    
    if from_client[0] == 'action':
      if from_client[1] == 'status':
        # pega distancia
        distancia += 1
    else:
      distancia = False
    print (from_client)
    conn.send(str(distancia).encode())

conn.close()

print ('client disconnected and shutdown')
