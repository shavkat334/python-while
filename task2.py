from time import sleep

secret = "1234"

tries = 3
while True:
    password = input("Parolni kiriting: ")


    if password == secret:
        print("Parol to'g'ri, xush kelibsiz!")
        break

    tries -= 1

    if tries == 0:
        print('10 sekuntdan keyin yana urinib ko\'ring!')
        sleep(10)
        tries = 3