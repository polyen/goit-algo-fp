items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(menu, budget):
    cart = {}
    calories = 0
    sorted_menu = dict(sorted(menu.items(), key=lambda x: x[1]['value'], reverse=True))
    min_cost = min(sorted_menu.items(), key=lambda x: x[1]['cost'])[1]['cost']

    while budget >= min_cost:
        for item in sorted_menu:
            if sorted_menu[item]['cost'] <= budget:
                cart[item] = cart.get(item, 0) + 1
                budget -= sorted_menu[item]['cost']
                calories += sorted_menu[item]['calories']

    return cart, budget, calories


def dynamic_programming(menu, budget):
    menu = [{'name': k, 'cost': v['cost'], 'value': v['value'], 'calories': v['calories']} for k, v in menu.items()]
    K = [[0 for _ in range(budget + 1)] for i in range(len(menu) + 1)]
    for i in range(len(menu) + 1):
        for j in range(budget + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif menu[i - 1]['cost'] <= j:
                K[i][j] = max(menu[i - 1]['value'] + K[i - 1][j - menu[i - 1]['cost']], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]

    cart = {}
    price = 0
    calories = 0
    i = len(menu)
    j = budget
    while i > 0 and j > 0:
        if K[i][j] != K[i - 1][j]:
            cart[menu[i - 1]['name']] = cart.get(menu[i - 1]['name'], 0) + 1
            j -= menu[i - 1]['cost']
            price += menu[i - 1]['cost']
            calories += menu[i - 1]['calories']
        i -= 1

    return cart, budget - price, calories


if __name__ == "__main__":
    try:
        budget = int(input('Введіть бюджет: '))
    except ValueError:
        print('Невірний ввід. Має бути натуральне число')
        exit(1)

    for item in items.values():
        item['value'] = int(item['calories'] / item['cost'])

    print("Оптимальний набір страв:")
    greedy_res, greedy_budget, greedy_cal = greedy_algorithm(items, budget)
    print(f'\tЖадібний алгоритм: {greedy_res} ({greedy_cal} кал.) залишок бюджету: {greedy_budget}')

    dp_res, dp_budget, dp_cal = dynamic_programming(items, budget)
    print(f'\tДинамічне програмування: {dp_res} ({dp_cal} кал.) залишок бюджету: {dp_budget}')
