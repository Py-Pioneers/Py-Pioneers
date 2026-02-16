#Team name : Py-Pioneers
def count_inventory(fruit_list):
    inventory = {}
    for fruit in fruit_list:
        if fruit in inventory:
            inventory[fruit] += 1
        else:
            inventory[fruit] = 1
    return inventory
