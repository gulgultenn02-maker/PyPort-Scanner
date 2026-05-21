# PortPulse: Multi-Threaded Network Reconnaissance and Banner Grabber

PortPulse, hedef sunucular veya IP adresleri üzerinde saniyeler içinde derinlemesine ağ keşfi yapabilen, multi-threaded (eşzamanlı) mimariyle optimize edilmiş yüksek hızlı bir siber güvenlik ve bilgi toplama (reconnaissance) aracıdır. 

Sadece portların açık olup olmadığını kontrol etmekle kalmaz; açık portların arkasında çalışan servislerin versiyon bilgilerini (Banner Grabbing) sızdırır ve web portlarında (80, 443, 8080) derinlemesine HTTP başlığı analizi yaparak kullanılan sunucu yazılımlarını (Nginx, Apache, Cloudflare vb.) tespit eder.

---

## Öne Çıkan Özellikler

* **Üstün Hız (Multi-Threading):** Portları tek tek sırayla taramak yerine, her port için eşzamanlı iş parçacıkları (threads) oluşturarak tarama süresini minimuma indirir.
* **Gelişmiş Banner Grabbing:** Açık olan servis portlarından (SSH, FTP vb.) gelen ham soket verilerini yakalayarak hedef sistemin işletim sistemi ve yazılım versiyonlarını açığa çıkarır.
* **Akıllı Web Keşfi (Web Recon):** requests kütüphanesini entegre bir şekilde kullanarak HTTP/HTTPS protokolleri üzerinden web sunucularının kimliklerini (Server Headers) deşifre eder.
* **Profesyonel CLI (Komut Satırı Arayüzü):** argparse altyapısı sayesinde kodun içine müdahale etmeden, terminal parametreleriyle dinamik yönetim sağlar.
* **Kararlı Hata Yönetimi:** Zaman aşımı (timeout) kontrolü ve ağ kesintilerine karşı geliştirilmiş try-except blokları sayesinde çökme yaşamadan taramayı tamamlar.

---

## Mimari ve Çalışma Mantığı

Araç iki temel katmandan oluşur:
1. **L4 Katmanı Keşfi (socket):** Doğrudan TCP handshake istekleri gönderilerek kapının durumu analiz edilir.
2. **L7 Katmanı Analizi (requests):** Eğer kapı bir web servisine aitse, tüm web sayfasını indirip vakit kaybetmeden sadece HEAD isteği göndererek sunucu başlık bilgisini ayıklar.

---

## Kurulum ve Gereksinimler

Proje standart Python kütüphanelerinin yanı sıra gelişmiş web analizi için requests modülünü kullanır.

### 1. Depoyu Klonlayın veya İndirin
```bash
git clone [https://github.com/kullanici_adiniz/PortPulse.git](https://github.com/kullanici_adiniz/PortPulse.git)
cd PortPulse
2. Sanal Ortamı Aktif Edin (Önerilen)
Bash
python3 -m venv .venv
source .venv/bin/activate
3. Gerekli Bağımlılıkları Yükleyin
Bash
pip install -r requirements.txt
Kullanım Kılavuzu
Sanal ortamınız aktifken aracı terminal üzerinden hem Domain Adları (Web Siteleri) hem de doğrudan IP Adresleri ile çalıştırabilirsiniz.
Domain Üzerinden Tarama:
Bash
python scanner.py -t [www.youtube.com](https://www.youtube.com)
IP Adresi Üzerinden Tarama:
Bash
python scanner.py -t 45.33.32.156
Yardım Menüsünü Görüntüleme:
Bash
python scanner.py --help
Örnek Terminal Çıktısı
Plaintext
=== [www.youtube.com](https://www.youtube.com) için Gelişmiş Tarama Başlatıldı ===
[*] Hızlandırma Modu: Aktif (Multi-threading)

[+] Port 22 AÇIK -> SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.14
[+] Port 80 AÇIK -> nginx
[+] Port 443 AÇIK -> nginx
[+] Port 8080 AÇIK -> Web Sunucusu (Gizli)

=== Tarama Tamamlandı ===
[i] Toplam 4 açık port bulundu.
Proje Klasör Yapısı
Plaintext
PortPulse/
│
├── .gitignore          # GitHub'a yüklenmeyecek dosyalar (.venv vb.)
├── README.md           # Proje vitrini ve dokümantasyon
├── requirements.txt    # Gerekli dış kütüphanelerin listesi
└── scanner.py          # Çoklu iş parçacıklı ana tarayıcı kaynak kodu
Yasal Uyarı (Disclaimer)
Bu araç tamamen eğitim, siber güvenlik farkındalığı ve beyaz şapkalı sızma testleri amacıyla geliştirilmiştir. İzniniz olmayan hedef sistemlere yönelik agresif taramalar yapmak yasal sorumluluklar doğurabilir. Kullanıcılar, aracın kullanımından doğacak yasal sonuçlardan kendileri sorumludur.