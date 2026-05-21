import socket
import requests
import threading  
import argparse   


acik_portlar_ve_servisler = []
liste_kilidi = threading.Lock() 

def tek_port_tara(hedef_host, port):
    
    soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soket.settimeout(1.5)
    
    sonuc = soket.connect_ex((hedef_host, port))
    
    if sonuc == 0:
        servis_bilgisi = "Bilinmiyor"
        
        if port in [80, 443, 8080]:
            try:
                protokol = "https" if port == 443 else "http"
                url = f"{protokol}://{hedef_host}"
                cevap = requests.head(url, timeout=1.5)
                servis_bilgisi = cevap.headers.get("Server", "Web Sunucusu (Gizli)")
            except:
                servis_bilgisi = "Web Sunucusu"
      
        else:
            try:
                banner = soket.recv(1024).decode('utf-8', errors='ignore').strip()
                if banner:
                    servis_bilgisi = banner
            except:
                servis_bilgisi = "Servis yanıt vermedi"
                
       
        with liste_kilidi:
            acik_portlar_ve_servisler.append({"port": port, "servis": servis_bilgisi})
            print(f"[+] Port {port} AÇIK -> {servis_bilgisi}")
            
    soket.close()

def main():
   
    parser = argparse.ArgumentParser(description="Gelişmiş Multi-threaded Zafiyet ve Port Tarayıcı")
    parser.add_argument("-t", "--target", required=True, help="Hedef IP veya Domain adresi (Örn: scanme.nmap.org)")
    args = parser.parse_args()
    
    hedef = args.target
    
    taranacak_portlar = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 8080, 8443]
    
    print(f"\n=== {hedef} için Gelişmiş Tarama Başlatıldı ===")
    print(f"[*] Hızlandırma Modu: Aktif (Multi-threading)\n")
    
    thread_havuzu = []
    
    for port in taranacak_portlar:
        t = threading.Thread(target=tek_port_tara, args=(hedef, port))
        thread_havuzu.append(t)
        t.start() 
        
    
    for t in thread_havuzu:
        t.join()
        
    print("\n=== Tarama Tamamlandı ===")
    print(f"[i] Toplam {len(acik_portlar_ve_servisler)} açık port bulundu.")

if __name__ == "__main__":
    main()