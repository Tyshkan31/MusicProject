import pygame

music = ['ЛП.mp3', 'Фенибут.mp3', 'Почему ты еще не фанат.mp3', 'По необъятной.mp3', 'Аскорбинка.mp3', 'Кора рора.mp3']
s1 = 0
s2 = 0
s3 = 0

def game_test():
    global s1, s2, s3

    for i in range(0, len(music)):

        filename = music[i]
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        p1 = input('Первый игрок введите песню ')
        p2 = input('Второй игрок введите песню ')
        p3 = input('Третий игрок введите песню ')
        y = ('.mp3')
        z1 = (p1 + y)
        z2 = (p2 + y)
        z3 = (p3 + y)
        if z1 == filename:
            print('Первый игрок ответил верно')
            s1 = s1 + 1
            print(s1)
        else:
            print('Первый игрок ответил неверно')
            s1 = s1 - 1
            print(s1)

        if z2 == filename:
            print('Второй игрок ответил верно')
            s2 = s2 + 1
            print(s2)
        else:
            print('Второй игрок ответил неверно')
            s2 = s2 - 1
            print(s2)

        if z3 == filename:
            print('Третий игрок ответил верно')
            s3 = s3 + 1
            print(s3)
        else:
            print('Третий игрок ответил неверно')
            s3 = s3 - 1
            print(s3)

        if s1 == 6:
            print('Первый игрок набрал максимум баллов')
        if s2 == 6:
            print('Второй игрок набрал максимум баллов')
        if s3 == 6:
            print('Третий игрок набрал максимум баллов')
        if i == 5:
            print("Песни закончились")
            print("Счет первого игрока: ", s1, "Счет второго игрока: ", s2, "Счет третьего игрока: ", s3)




