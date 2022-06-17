def look_for_key(main_box):# оголошуємо функцію з назвою look_for_key та
    # аргументом main_box
    pile=main_box.make_a_pile_to_look_through # pile - куча.
    while pile is not empty: # Оголошуємо цикл (поки куча не пуста)
        box = pile.grab_a_box()# Коробка- означає взяти коробку з кучі
        for item in box: # Запускаємо цикл фор для елементів у коробці
            if item.is_a_box(): # якщо елемент - це коробка
                pile.append(item) # викинути коробку назад до кучі
            elif item.is_a_key(): # якщо елемент це ключ
                print("found the key!") # тоді друкуємо цей запис.
print("Hello World")
print("sow hear we go agein")
