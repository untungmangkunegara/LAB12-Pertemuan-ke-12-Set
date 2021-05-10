# MATERI : SET
# REFERENSI : UG KELAS A, SOAL B, NOMOR 2

# Unchy dan Dorry adalah teman sejati. Unchy gabut dan ingin membandingkan game-game yang dimainkan olehnya dan Dorry, 
# lalu Unchy akan mencari game apa saja yang berbeda dari dirinya dan Dorry. Karena gabut dan ingin uang, cobalah bantu kegabutan Unchy 
# agar kamu tidak jadi gabut. Cobalah buat sebuah program yang dapat menampilkan game apa saja yang dimainkan oleh Unchy dan Dorry, dan 
# tampilkan perbedaannya.

# Input
# Game Unchy: ............
# Game Dorry: ............

# Output
# Game Unchy: ............
# Game Dorry: ............
# Perbedaan : ............ 

GameUnchy=[]
GameDorry=[]

a= int(input("Masukkan jumlah game yang dimainkan oleh Unchy: "))
b= int(input("Masukkan jumlah game yang dimainkan oleh Dorry: "))

print("Masukkan Game yang dimainkan Unchy")
for i in range (a):
    gameUn=str(input("Game: "))
    GameUnchy.append(gameUn)
# print(GameUnchy)

print("Masukkan Game yang dimainkan Dorry")
for j in range (b):
    gameDor=str(input("Game: "))
    GameDorry.append(gameDor)
# print(GameDorry)

setUnchy=set(GameUnchy)
setdDorry=set(GameDorry)

# Output
print("Game yang dimainkan Unchy adalah")
print(GameUnchy)

print("Game yang dimainkan Dorry adalah")
print(GameDorry)

print("Game yang berbeda adalah :")
beda=setUnchy.symmetric_difference(setdDorry)
print(beda)