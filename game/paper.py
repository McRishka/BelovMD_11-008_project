def paper(pc_element):
    if pc_element < 5:
        print('\n\n', "Вы выиграли!")
        if pc_element == 1:
            print("Компьютер выбрал камень")
            print("Бумага сильнее камня")
        elif pc_element == 2:
            print("Компьютер выбрал пистолет")
            print("Бумага сильнее пистолета")
        elif pc_element == 3:
            print("Компьютер выбрал воду")
            print("Бумага сильнее воды")
        else:
            print("Компьютер выбрал воздух")
            print("Бумага сильнее воздуха")
    elif pc_element > 5:
        print('\n\n', "Вы проиграли :(")
        if pc_element == 6:
            print("Компьютер выбрал губку")
            print("Губка сильнее бумаги")
        elif pc_element == 7:
            print("Компьютер выбрал человека :)")
            print("Человек сильнее бумаги")
        elif pc_element == 8:
            print("Компьютер выбрал ножницы")
            print("Ножницы разрезали бумагу")
        else:
            print("Компьютер выбрал огонь")
            print("Ваша бумага сгорела")
    else:
        print('\n\n', "Ничья")
        print("Компьютер тоже выбрал бумагу")
