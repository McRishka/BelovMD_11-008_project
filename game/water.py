def water(pc_element):
    if pc_element == 1 or pc_element == 2 or pc_element > 7:
        print('\n\n', "Вы выиграли!")
        if pc_element == 1:
            print("Компьютер выбрал камень")
            print("Камень утонул в воде")
        elif pc_element == 2:
            print("Компьютер выбрал пистолет")
            print("Пистолет заржавел от воды")
        elif pc_element == 8:
            print("Компьютер выбрал ножницы")
            print("Ножницы заржавели от воды")
        else:
            print("Компьютер выбрал огонь")
            print("Вы потушили огонь водой")
    elif pc_element > 3 and pc_element < 8:
        print('\n\n', "Вы проиграли :(")
        if pc_element == 4:
            print("Компьютер выбрал воздух")
            print("Воздух сильнее воды")
        elif pc_element == 5:
            print("Компьютер выбрал бумагу")
            print("Бумага сильнее воды")
        elif pc_element == 6:
            print("Компьютер выбрал губку")
            print("Губка впитала воду")
        else:
            print("Компьютер выбрал человека :)")
            print("Человек выпил воду")
    else:
        print('\n\n', "Ничья")
        print("Компьютер тоже выбрал воду")
