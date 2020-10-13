def fire(pc_element):
    if pc_element < 9 and pc_element > 4:
        print('\n\n', "Вы выиграли!")
        if pc_element == 5:
            print("Компьютер выбрал бумагу")
            print("Бумага сгорела")
        elif pc_element == 6:
            print("Компьютер выбрал губку")
            print("Губка сгорела")
        elif pc_element == 7:
            print("Компьютер выбрал человека :)")
            print("Человек сгорел")
        else:
            print("Компьютер выбрал ножницы")
            print("Ножницы расплавились")
    elif pc_element < 5:
        print('\n\n', "Вы проиграли :(")
        if pc_element == 1:
            print("Компьютер выбрал камень")
            print("Камень потушил ваш огонь")
        elif pc_element == 2:
            print("Компьютер выбрал пистолет")
            print("Пистолет сильнее огня")
        elif pc_element == 3:
            print("Компьютер выбрал вода")
            print("Вода потушила ваш огонь")
        else:
            print("Компьютер выбрал воздух")
            print("Воздух сильнее огня")
    else:
        print('\n\n', "Ничья")
        print("Компьютер тоже выбрал огонь")
