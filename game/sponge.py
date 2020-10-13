def sponge(pc_element):
    if pc_element < 6 and pc_element > 1:
        print('\n\n', "Вы выиграли!")
        if pc_element == 2:
            print("Компьютер выбрал пистолет")
            print("Губка сильнее пистолета")
        elif pc_element == 3:
            print("Компьютер выбрал воду")
            print("Губка впитала воду")
        elif pc_element == 4:
            print("Компьютер выбрал воздух")
            print("Губка сильнее воздуха")
        else:
            print("Компьютер выбрал бумагу")
            print("Губка сильнее бумаги")
    elif pc_element > 6 or pc_element == 1:
        print('\n\n', "Вы проиграли :(")
        if pc_element == 1:
            print("Компьютер выбрал камень")
            print("Камень раздавил губку")
        elif pc_element == 7:
            print("Компьютер выбрал человека :)")
            print("Человек сильнее губки")
        elif pc_element == 8:
            print("Компьютер выбрал ножницы")
            print("Ножницы разрезали губку")
        else:
            print("Компьютер выбрал огонь")
            print("Ваша губка сгорела")
    else:
        print('\n\n', "Ничья")
        print("Компьютер тоже выбрал губку")
