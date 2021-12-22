from lib.utils.Layers import Layers
from lib.utils.System import System

class Menu:
    def select_generation_order(current_order):
        categories = Layers.get_categories()
        
        selection = 1
        choices = []
        for category in categories:
            if category not in current_order:
                print(f"{selection}. {category}")
                choices.append(category)
                selection += 1

        choice = int(input("Select generation layer order: ")) - 1

        return choices[choice]

    def select_base_index(generation_order):
        Menu.ordered_display(generation_order)
        choice = int(input("Select the layer to insert base: "))
        generation_order.insert(choice -1, "base")

        return generation_order

    def ordered_display(list):
        n = 1
        for item in list:
            print(f'{n}. {item}')
            n += 1