def stone(pc_element):
    if pc_element != 1 and pc_element > 5:
        print('\n\n', "Вы выиграли!")
        if pc_element == 6:
            print("Компьютер выбрал губку")
            print("Ваш камень раздавил губку")
        elif pc_element == 7:
            print("Компьютер выбрал человека :)")
            print("Вы убили человека камнем")
        elif pc_element == 8:
            print("Компьютер выбрал ножницы")
            print("Вы сломали ножницы камнем")
        else:
            print("Компьютер выбрал огонь")
            print("Вы потушили камнем огонь")
    elif pc_element > 1 and pc_element < 6:
        print('\n\n', "Вы проиграли :(")
        if pc_element == 2:
            print("Компьютер выбрал пистолет")
            print("Пистолет разрушил ваш камень")
        elif pc_element == 3:
            print("Компьютер выбрал воду")
            print("Ваш камень утонул в воде")
        elif pc_element == 4:
            print("Компьютер выбрал воздух")
            print("Ваш камень проиграл воздуху")
        else:
            print("Компьютер выбрал бумагу")
            print("Бумага завернула ваш камень")
    else:
        print('\n\n', "Ничья")
        print("Компьютер тоже выбрал камень")

