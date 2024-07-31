# Iterate the elements of the menu
for dish, values in my_menu.items():
    # Print whether the dish must be served cold or hot
    print(f"{dish.title()} is best served {values['best_served']}.")
