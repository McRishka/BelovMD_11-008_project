def human(pc_element):
    if pc_element < 7 and pc_element > 2:
        print('\n\n', "Вы выиграли!")
        if pc_element == 3:
            print("Компьютер выбрал воду")
            print("Человек выпил воду")
        elif pc_element == 4:
            print("Компьютер выбрал воздух")
            print("Человек сильнее воздуха")
        elif pc_element == 5:
            print("Компьютер выбрал бумагу")
            print("Человек сильнее бумаги")
        else:
            print("Компьютер выбрал губку")
            print("Человек сильнее губки")
    elif pc_element > 7 or pc_element < 3:
        print('\n\n', "Вы проиграли :(")
        if pc_element == 1:
            print("Компьютер выбрал камень")
            print("Компьютер убил человека камнем")
        elif pc_element == 2:
            print("Компьютер выбрал пистолет")
            print("Компьютер убил человека из пистолета")
        elif pc_element == 8:
            print("Компьютер выбрал ножницы")
            print("Компьютер убил человека ножницами")
        else:
            print("Компьютер выбрал огонь")
            print("Человек сгорел в огне")
    else:
        print('\n\n', "Ничья")
        print("Компьютер тоже выбрал человека :)")
