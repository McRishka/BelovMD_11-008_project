def air(pc_element):
    if pc_element < 4 or pc_element == 9:
        print('\n\n', "Вы выиграли!")
        if pc_element == 1:
            print("Компьютер выбрал камень")
            print("Воздух сильнее камня")
        elif pc_element == 2:
            print("Компьютер выбрал пистолет")
            print("Воздух сильнее пистолета")
        elif pc_element == 3:
            print("Компьютер выбрал воду")
            print("Воздух сильнее воды")
        else:
            print("Компьютер выбрал огонь")
            print("Вы потушили огонь")
    elif pc_element > 4 and pc_element < 9:
        print('\n\n', "Вы проиграли :(")
        if pc_element == 5:
            print("Компьютер выбрал бумагу")
            print("Бумага сильнее воздуха")
        elif pc_element == 6:
            print("Компьютер выбрал губку")
            print("Губка сильнее воздуха")
        elif pc_element == 7:
            print("Компьютер выбрал человека :)")
            print("Человек сильнее воздуха")
        else:
            print("Компьютер выбрал ножницы")
            print("Ножницы сильнее воздуха")
    else:
        print('\n\n', "Ничья")
        print("Компьютер тоже выбрал воздух")
