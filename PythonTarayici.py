import socket
import requests  # Yeni yüklediğimiz web kütüphanesini çağırıyoruz

hedef_host = "www.youtube.com"
hedef_port = [21, 22, 23, 80, 443, 8080]

print(f"--- {hedef_host} Üzerinde Gelişmiş Tarama ve Web Keşfi Başlatıldı ---\n")

for port in hedef_port:
    soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soket.settimeout(2.0)
    
    sonuc = soket.connect_ex((hedef_host, port))
    
    if sonuc == 0:
        print(f"[+] Port {port} AÇIK")
        
        # Eğer port bir web portu DEĞİLSE (Örn: 22 SSH), eski yöntemle banner al
        if port not in [80, 443, 8080]:
            try:
                banner = soket.recv(1024).decode('utf-8', errors='ignore').strip()
                if banner:
                    print(f"    └─> Sistem Bilgisi: {banner}")
            except:
                pass
                
        # Eğer port bir WEB portuysa (80, 443, 8080), HTTP isteği göndererek keşif yap
        else:
            try:
                # Port 443 ise güvenli bağlantı (https), diğerleri ise (http) protokolünü kullanır
                protokol = "https" if port == 443 else "http"
                url = f"{protokol}://{hedef_host}"
                
                # Sitenin sadece üst bilgilerini (HEAD) istiyoruz, tüm sayfayı indirip vakit kaybetmiyoruz
                cevap = requests.head(url, timeout=2.0)
                
                # Yanıtın (headers) içinden "Server" bilgisini çekiyoruz
                web_sunucusu = cevap.headers.get("Server")
                
                if web_sunucusu:
                    print(f"    └─> Web Sunucu Yazılımı: {web_sunucusu}")
                else:
                    print(f"    └─> Web Sunucu Yazılımı: Tespit edilemedi (Gizlenmiş olabilir).")
            except:
                print(f"    └─> HTTP İsteği Başarısız Oldu.")
                
        soket.close()
    else:
        # Kapalı portları artık yazdırmıyoruz, ekranımız temiz kalsın!
        pass

print("\n--- Gelişmiş Tarama Tamamlandı ---")