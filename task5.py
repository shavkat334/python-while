# Hisoblagichni noldan boshlaymiz
count = 0

print("Matn kiriting (to'xtatish uchun 'stop' deb yozing):")

while True:
    matn = input(">>> ")
    
    # Agar foydalanuvchi "stop" deb yozsa, loop tugaydi
    if matn.lower() == "stop":
        break
    
    # Aks holda, har bir kiritilgan matn uchun hisoblagichni 1 taga oshiramiz
    count += 1

print(f"Dastur tugadi. Siz jami {count} marta matn kiritdingiz.")