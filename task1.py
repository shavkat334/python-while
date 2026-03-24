from random import randint

random_number = randint(1, 20)
while True:
    user_guest = None

    while True:
        user_guest = int(input('1 dan 20 gacha son kiriting: '))
        if user_guest < random_number:
            print('kattaroq son')
        elif user_guest > random_number:
            print('kichikroq son')
        else:
            print('Tabriklaymiz, siz to\'g\'ri topdingiz!')
            break