# YOLO Nesne Tespiti Uygulaması

[English](README_EN.md) | Türkçe

Bu proje, YOLO (You Only Look Once) modelini kullanarak gerçek zamanlı nesne tespiti yapan bir Python uygulamasıdır. İnsan, araç ve hayvan tespiti yapabilmektedir.

## Özellikler

- Gerçek zamanlı nesne tespiti
- Webcam ve video dosyası desteği
- FPS (Frame Per Second) gösterimi
- Tespit edilen nesne sayısı takibi
- Ekran görüntüsü alma
- Video kaydetme
- Ayarlanabilir tespit hassasiyeti

## Gereksinimler

```bash
pip install -r requirements.txt
```

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/Semihkulekcioglu/person_animal_car_detection_system.git
cd person_animal_car_detection_system
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Programı çalıştırın:
```bash
python object_detection_yolo.py
```

## Kullanım

Program başlatıldığında varsayılan olarak webcam kullanılır. Video dosyası kullanmak için `object_detection_yolo.py` dosyasında `source` değişkenini video dosyasının yoluna ayarlayın.

### Kontroller

- 'q': Programdan çıkış
- 's': Ekran görüntüsü alma
- '+': Güven eşiğini artırma
- '-': Güven eşiğini azaltma

## Klasör Yapısı

```
.
├── object_detection_yolo.py    # Ana program
├── best.pt                     # YOLO model dosyası
├── requirements.txt            # Gerekli paketler
├── README.md                   # Türkçe dokümantasyon
├── README_EN.md               # İngilizce dokümantasyon
└── detections/                 # Çıktı klasörü
    ├── screenshots/            # Ekran görüntüleri
    └── videos/                # Video kayıtları
```

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: Açıklama'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.