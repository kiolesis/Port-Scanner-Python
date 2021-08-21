# Wykryj łatwo otwarte i nieaktywne porty sieciowe
import socket

ports = input("Wpisz adresy portów od 1-1000 :")
#   1-1000

start,end = ports.split('-')
start = int(start)
end = int(end)

for i in range(start,end+1):

    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        s.connect(('192.168.0.101',i))
        print("Port {} jest otwarty".format(i))
        s.close()

    except:
        pass
        print("Port {} jest zamknięty".format(i))
