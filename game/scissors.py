def scissors(pc_element):
    if pc_element < 8 and pc_element > 3:
        print('\n\n', "Вы выиграли!")
        if pc_element == 4:
            print("Компьютер выбрал воздух")
            print("Ножницы сильнее воздуха")
        elif pc_element == 5:
            print("Компьютер выбрал бумагу")
            print("Вы разрезали бумагу ножницами")
        elif pc_element == 6:
            print("Компьютер выбрал губку")
            print("Вы разрезали губку ножницами")
        else:
            print("Компьютер выбрал человека :)")
            print("Вы убили человека ножницами")
    elif pc_element < 4 or pc_element == 9:
        print('\n\n', "Вы проиграли :(")
        if pc_element == 1:
            print("Компьютер выбрал камень")
            print("Компьютер сломал ножницы камнем")
        elif pc_element == 2:
            print("Компьютер выбрал пистолет")
            print("Пистолет сильнее ножниц")
        elif pc_element == 3:
            print("Компьютер выбрал вода")
            print("Ножницы заржавели в воде")
        else:
            print("Компьютер выбрал огонь")
            print("Ножницы расплавились")
    else:
        print('\n\n', "Ничья")
        print("Компьютер тоже выбрал ножницы")
