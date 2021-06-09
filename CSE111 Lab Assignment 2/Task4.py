def FoodPanda(Food,place = 'Mohakhali'):
    menu = {"BBQ Chicken Cheese Burger": 250, "Beef Burger": 170, "Naga Drums": 200}
    total = 0

    for i in menu.keys():
        if i == Food:
            total += menu.get(i)
        tax = total*(8/100)

    if place == "Mohakhali":
        total += tax + 40
    else:
        total += tax + 60

    return total

print(FoodPanda('Beef Burger','Dhanmondi'))