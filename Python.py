import turtle
import time

# Pencere oluşturma
pencere = turtle.Screen()
pencere.title("Telefon Animasyonu")
pencere.bgcolor("#f0f0f0")
pencere.setup(width=600, height=600)

# Metnin animasyonunu ve çizginin animasyonunu başlat
def animasyon():
    # Telefonu kaldırma animasyonu
    for i in range(25):
        telefon.clear()
        ciz_telefon(-160, -260 + i*10, 320, 520)
        time.sleep(0.05)
    # "hard.shelby" yazısını ve çizgiyi gösterme
    yaz_metin(0, 0, "hard.shelby")
    ciz_cizgi(-100, -50)

# Telefon gövdesini çizme
def ciz_telefon(x, y, uzunluk, genislik):
    telefon.penup()
    telefon.goto(x, y)
    telefon.pendown()
    for _ in range(2):
        telefon.forward(uzunluk)
        telefon.right(90)
        telefon.forward(genislik)
        telefon.right(90)

# Çizgiyi çizme
def ciz_cizgi(x, y):
    cizgi.penup()
    cizgi.goto(x, y)
    cizgi.pendown()
    cizgi.forward(200)

# Metni yazma fonksiyonu
def yaz_metin(x, y, metin):
    ekran.penup()
    ekran.goto(x, y)
    ekran.pendown()
    ekran.write(metin, align="center", font=("Arial", 20, "normal"))

# Telefon gövdesi
telefon = turtle.Turtle()
telefon.speed(0)
telefon.color("#333333")
telefon.width(3)

# Ekran
ekran = turtle.Turtle()
ekran.speed(0)
ekran.color("#333333")
ekran.width(3)

# Çizgi
cizgi = turtle.Turtle()
cizgi.speed(0)
cizgi.color("blue")
cizgi.width(3)

# Animasyonu başlat
animasyon()

# Kapanış
pencere.mainloop()
