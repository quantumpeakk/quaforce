# QUA FORCE - Gelişmiş Brute Force Aracı

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Lisans](https://img.shields.io/badge/Lisans-MIT-green)

QUA FORCE, etik penetrasyon testleri ve güvenlik araştırmaları için tasarlanmış gelişmiş bir brute force aracıdır.

## 😃 Kullanım Rehberi
- Bir txt dosyasi oluşturun içinde denenecek kullanici isimleri olsun
- Bir txt dosyasi daha oluşturun içinde denenecek şifreler olsun
- Kurulum adımlarını okuyup tool'u kurun
- Tool u çalıştırın
- Gerisini anlarsınız zaten
- anlayamayanin aminigotunusikim

## 🌟 Öne Çıkan Özellikler
- Çoklu kullanıcı adı/şifre denemesi
- Özel bekleme süresi (rate limiting önleme)
- Başarılı girişlerin `success.txt` dosyasına kaydı
- Özelleştirilebilir kullanıcı ajanı (User-Agent)
- Renkli konsol çıktısı
- Kolay kurulum ve kullanım

## 🛠️ Kurulum

### Gereksinimler
- Python
- `requests` ve `colorama` kütüphaneleri

### Kurulum Adımları
```bash
git clone https://github.com/quantumpeakk/quaforce.git
cd quaforce
pip install -r requirements.txt

```
### Tool u başlatma
```bash
python quaforce.py
