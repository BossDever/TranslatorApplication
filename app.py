from dpi_set import *
from tkinter import *
from deep_translator import GoogleTranslator

def translate():
    message = text1.get('1.0', 'end-1c')
    if message.strip():  # ตรวจสอบว่ามีข้อความหรือไม่
        text2.delete(1.0, 'end')  # ล้างข้อความเก่าก่อน
        output = GoogleTranslator(source='en', target='th').translate(message)
        text2.insert('end', output)

def reset():
    text1.delete(1.0,'end')
    text2.delete(1.0,'end')


dpi = DpiManager()
dpi.enable_win_dpi_awareness(mode="system")  # หรือ "permonitor"

#ขนาดหน้าจอ
root = Tk()
root.title("Google Translate (EN-TH)")
root.geometry('530x300')
root.maxsize(530,300)
root.minsize(530,300)

# ตั้งค่าสเกลแบบคงที่เพื่อให้ UI เป็นระเบียบ
dpi.set_fixed_scaling(root, scaling=1.0)  # ใช้สเกลคงที่ 1.0
# dpi.bind_auto_update(root)   # ปิดการอัปเดตอัตโนมัติ


# Widgets - ใช้ grid layout เพื่อให้เป็นระเบียบ
# หัวข้อ
label = Label(root, text="English - Thai", font=('Arial', 24, 'bold'))
label.grid(row=0, column=0, columnspan=2, pady=10)

# ป้ายกำกับช่องข้อความ
label_en = Label(root, text="English", font=('Arial', 14, 'bold'))
label_en.grid(row=1, column=0, padx=10, pady=5, sticky='w')

label_th = Label(root, text="Thai", font=('Arial', 14, 'bold'))
label_th.grid(row=1, column=1, padx=10, pady=5, sticky='w')

# ช่องข้อความภาษาอังกฤษ
text1 = Text(root, width=25, height=8, font=('Arial', 12))
text1.grid(row=2, column=0, padx=10, pady=5, sticky='nsew')

# ช่องข้อความภาษาไทย
text2 = Text(root, width=25, height=8, font=('Arial', 12))
text2.grid(row=2, column=1, padx=10, pady=5, sticky='nsew')

# Frame สำหรับปุ่ม
button_frame = Frame(root)
button_frame.grid(row=3, column=0, columnspan=2, pady=15)

# ปุ่ม
translateBtn = Button(button_frame, text="แปลภาษา", command=translate, 
                     font=('Arial', 13, 'bold'), bg='#4CAF50', fg='white',
                     width=12, height=1)
translateBtn.pack(side=LEFT, padx=5)

clearBtn = Button(button_frame, text="เคลียร์", command=reset,
                 font=('Arial', 13, 'bold'), bg='#f44336', fg='white',
                 width=12, height=1)
clearBtn.pack(side=LEFT, padx=5)

# ตั้งค่า grid weights
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.mainloop()