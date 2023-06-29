# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

def find_items_backpack(items, max_weight):
    backpack_items = []
    total_weight = 0

    for item in items:
        item_name = item[0]
        item_weight = item[1]

        if total_weight + item_weight <= max_weight:
            backpack_items.append(item_name)
            total_weight += item_weight

    return backpack_items


items = {
    "дрова": 5,
    "спальный мешок": 3,
    "котелок": 2,
    "еда": 2,
    "вода": 1,
    "палатка": 4,
    "фонарик": 1
}

max_weight = 10

result = find_items_backpack(items.items(), max_weight)
print("Вещи, которые поместятся в рюкзак:")
for item in result:
    print(item)