def gun(pc_element):
    if pc_element == 1 and pc_element != 2 or pc_element > 6:
        print('\n\n', "Вы выиграли!")
        if pc_element == 1:
            print("Компьютер выбрал камень")
            print("Вы разрушили камень пистолетом")
        elif pc_element == 7:
            print("Компьютер выбрал человека :)")
            print("Вы убили человека")
        elif pc_element == 8:
            print("Компьютер выбрал ножницы")
            print("Вы сломали ножницы")
        else:
            print("Компьютер выбрал огонь")
            print("Пистолет сильнее огня")
    elif pc_element > 2 and pc_element < 7:
        print('\n\n', "Вы проиграли :(")
        if pc_element == 3:
            print("Компьютер выбрал воду")
            print("Ваш пистолет заржавел в воде")
        elif pc_element == 4:
            print("Компьютер выбрал воздух")
            print("Воздух сильнее пистолета")
        elif pc_element == 5:
            print("Компьютер выбрал бумагу")
            print("Бумага сильнее пистолета")
        else:
            print("Компьютер выбрал губку")
            print("Губка сильнее пистолет")
    else:
        print('\n\n', "Ничья")
        print("Компьютер тоже выбрал пистолет")
