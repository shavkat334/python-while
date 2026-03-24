while True:

    son1 = float(input("Birinchi sonni kiriting: "))
    son2 = float(input("Ikkinchi sonni kiriting: "))
    
    amal = input("Amalni tanlang (+, -, *, /): ")
    
    if amal == "+":
        print(f"Natija: {son1 + son2}")
    elif amal == "-":
        print(f"Natija: {son1 - son2}")
    elif amal == "*":
        print(f"Natija: {son1 * son2}")
    elif amal == "/":
        if son2 != 0:
            print(f"Natija: {son1 / son2}")
        else:
            print("Xato! Nolga bo'lish mumkin emas.")
    else:
        print("Noto'g'ri amal kiritildi!")

    savol = input("Davom etasizmi? (ha/yo'q): ").lower()
    if savol == "yo'q":
        print("Dastur tugadi. Xayr!")
        break