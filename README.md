# Translator Application

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/github/license/BossDever/TranslatorApplication?color=yellow)

แอปพลิเคชันแปลภาษาจากภาษาอังกฤษเป็นภาษาไทย โดยใช้ Google Translate ผ่านไลบรารี deep-translator พร้อมส่วนติดต่อผู้ใช้แบบกราฟิก (GUI) ที่พัฒนาโดย Tkinter รองรับการตั้งค่า DPI สำหรับหน้าจอความละเอียดสูง

## ฟีเจอร์

- 🌐 แปลข้อความจากภาษาอังกฤษเป็นภาษาไทย
- 🖥️ ใช้งานง่ายด้วย GUI ที่ใช้งานได้ทันที
- 🔄 ปุ่มเคลียร์เพื่อล้างข้อความ
- 📱 รองรับ DPI scaling สำหรับหน้าจอความละเอียดสูง
- ⚡ ทำงานได้ทันทีโดยไม่ต้องติดตั้งซอฟต์แวร์เพิ่มเติมนอกเหนือจาก Python และแพ็กเกจที่กำหนด

## ข้อกำหนดระบบ

- Python 3.6 หรือใหม่กว่า
- ระบบปฏิบัติการ: Windows, macOS, หรือ Linux
- การเชื่อมต่ออินเทอร์เน็ต (สำหรับการแปลภาษา)

## การติดตั้ง

1) Clone โปรเจกต์
```bash
git clone <repository-url>
cd TranslatorApplication
```

2) ติดตั้ง dependencies
```bash
pip install -r requirements.txt
```
หมายเหตุเกี่ยวกับ Tkinter:
- Tkinter มากับ Python มาตรฐานอยู่แล้วใน Windows/macOS ส่วนใหญ่
- บน Linux อาจต้องติดตั้งแพ็กเกจระบบเพิ่ม:
  - Debian/Ubuntu: `sudo apt-get install python3-tk`
  - Fedora: `sudo dnf install python3-tkinter`
  - Arch: `sudo pacman -S tk`
- หากสภาพแวดล้อมของคุณต้องการติดตั้งผ่าน pip ให้ลอง `pip install tk` (อาจไม่รองรับทุกแพลตฟอร์ม)

## การใช้งาน

1) รันแอปพลิเคชัน
```bash
python app.py
```

2) วิธีการใช้งาน
- พิมพ์ข้อความภาษาอังกฤษในช่องด้านซ้าย
- คลิกปุ่ม "แปลภาษา" เพื่อแปลเป็นภาษาไทย
- ผลลัพธ์จะแสดงในช่องด้านขวา
- คลิกปุ่ม "เคลียร์" เพื่อล้างข้อความทั้งหมด

## โครงสร้างโปรเจกต์

```
TranslatorApplication/
├── app.py          # ไฟล์หลักของแอปพลิเคชัน
├── dpi_set.py      # โมดูลจัดการการตั้งค่า DPI/Scaling (สำหรับ Windows เป็นหลัก)
├── requirements.txt
└── README.md
```

## รายละเอียดไฟล์

### app.py
- ฟังก์ชัน `translate()`: แปลข้อความจากภาษาอังกฤษเป็นไทยด้วย deep-translator
- ฟังก์ชัน `reset()`: ล้างค่าข้อความในช่องกรอก
- สร้างและจัดวางองค์ประกอบ GUI ด้วย Tkinter
- ปรับ DPI scaling เพื่อให้ UI แสดงผลชัดเจน

### dpi_set.py
- กำหนด Windows DPI awareness และ scaling
- ช่วยให้ UI แสดงผลคมชัดและมีสัดส่วนเหมาะสมบนหน้าจอที่มี DPI แตกต่างกัน

## Dependencies

- deep-translator: ใช้เรียก Google Translate API (ผ่าน library) เพื่อแปลภาษา
- tkinter: มาพร้อมกับ Python (stdlib) ใช้สร้าง GUI
- ctypes: มาพร้อมกับ Python (stdlib) ใช้งาน Windows API ที่เกี่ยวข้องกับ DPI

## การแก้ไขปัญหาพบบ่อย

### GUI ไม่แสดงหรือ Error เกี่ยวกับ Tkinter
- ตรวจสอบว่าได้ติดตั้ง Tkinter สำหรับระบบปฏิบัติการของคุณแล้ว (เช่น `sudo apt-get install python3-tk` บน Ubuntu)
- หากรันใน virtual environment ที่เบา (minimal) ให้ลอง `pip install tk`

### แปลภาษาไม่ทำงาน
- ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต
- ตรวจสอบว่าแพ็กเกจ deep-translator ติดตั้งเรียบร้อย (`pip show deep-translator`)
- ลองอัปเดตแพ็กเกจ: `pip install -U deep-translator`

## Roadmap (แนวทางพัฒนาต่อ)
- รองรับการแปลหลายภาษา
- เพิ่มการแปลแบบ real-time
- รองรับการอ่านออกเสียง (text-to-speech)
- ปรับแต่งธีมและรูปแบบฟอนต์ของ UI

## License
โปรเจกต์นี้เป็นโอเพนซอร์ส ดูรายละเอียดสัญญาอนุญาตได้ในไฟล์ LICENSE ของโปรเจกต์