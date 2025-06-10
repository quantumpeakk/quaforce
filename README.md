# QUA FORCE - Gelişmiş Brute Force Aracı

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Lisans](https://img.shields.io/badge/Lisans-MIT-green)
![GitHub Yıldız](https://img.shields.io/github/stars/kullaniciadiniz/quaforce?style=social)

QUA FORCE, etik penetrasyon testleri ve güvenlik araştırmaları için tasarlanmış gelişmiş bir brute force aracıdır.

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
git clone https://github.com/kullaniciadiniz/quaforce.git
cd quaforce
pip install -r requirements.txt

### Toolu başlatma
```bash
python quaforce.py
