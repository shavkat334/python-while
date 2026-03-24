
ball = 0

print("O'yin boshlandi! Ball yig'ish uchun '+' belgisini yozing.")
print("To'xtatish uchun 'stop' deb yozing.")

while True:
    buyruq = input("Belgi kiriting: ")
    
    if buyruq == "+":
        ball += 10
        print(f"Ball oshdi! Hozirgi ball: {ball}")
    
    elif buyruq == "stop":
        print(f"O'yin tugadi. Sizning umumiy ballingiz: {ball}")
        break 
        
    else:
        print("Faqat '+' yoki 'stop' yozing!")