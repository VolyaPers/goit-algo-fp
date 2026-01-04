items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    ratios = []
    for name, info in items.items():
        ratio = info["calories"] / info["cost"]
        ratios.append((name, ratio, info["cost"], info["calories"]))

    ratios.sort(key=lambda x: x[1], reverse=True)

    selected = []
    total_cost = 0
    total_calories = 0

    for name, ratio, cost, calories in ratios:
        if total_cost + cost <= budget:
            selected.append(name)
            total_cost += cost
            total_calories += calories

    return selected, total_cost, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - costs[i - 1]] + calories[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(names[i - 1])
            w -= costs[i - 1]

    selected.reverse()
    total_cost = sum(items[name]["cost"] for name in selected)
    total_calories = dp[n][budget]

    return selected, total_cost, total_calories


def print_results(title, selected, total_cost, total_calories, items):
    print(f"\n{'=' * 50}")
    print(f"{title}")
    print('=' * 50)
    print(f"{'Страва':<15} {'Вартість':<10} {'Калорії':<10}")
    print('-' * 50)
    for name in selected:
        print(f"{name:<15} {items[name]['cost']:<10} {items[name]['calories']:<10}")
    print('-' * 50)
    print(f"{'ВСЬОГО:':<15} {total_cost:<10} {total_calories:<10}")


if __name__ == "__main__":
    print("Доступні страви:")
    print(f"{'Страва':<15} {'Вартість':<10} {'Калорії':<10} {'Калорії/Вартість':<15}")
    print('-' * 55)
    for name, info in items.items():
        ratio = info["calories"] / info["cost"]
        print(f"{name:<15} {info['cost']:<10} {info['calories']:<10} {ratio:<15.2f}")

    budget = 100

    print(f"\n>>> Бюджет: {budget} грн")

    greedy_result = greedy_algorithm(items, budget)
    print_results("ЖАДІБНИЙ АЛГОРИТМ", *greedy_result, items)

    dp_result = dynamic_programming(items, budget)
    print_results("ДИНАМІЧНЕ ПРОГРАМУВАННЯ", *dp_result, items)

    print(f"\n{'=' * 50}")
    print("ПОРІВНЯННЯ АЛГОРИТМІВ")
    print('=' * 50)
    print(f"{'Метод':<30} {'Калорії':<10} {'Вартість':<10}")
    print('-' * 50)
    print(f"{'Жадібний':<30} {greedy_result[2]:<10} {greedy_result[1]:<10}")
    print(f"{'Динамічне програмування':<30} {dp_result[2]:<10} {dp_result[1]:<10}")

    if dp_result[2] > greedy_result[2]:
        diff = dp_result[2] - greedy_result[2]
        print(f"\nДП краще на {diff} калорій")
    elif dp_result[2] == greedy_result[2]:
        print(f"\nОбидва алгоритми дали однаковий результат")
    else:
        print(f"\nЖадібний краще (рідкісний випадок)")

    print(f"\n{'=' * 50}")
    print("ТЕСТУВАННЯ З РІЗНИМИ БЮДЖЕТАМИ")
    print('=' * 50)

    for test_budget in [50, 75, 100, 150]:
        g = greedy_algorithm(items, test_budget)
        d = dynamic_programming(items, test_budget)
        status = "✓" if g[2] == d[2] else "≠"
        print(f"Бюджет {test_budget:>3}: Жадібний={g[2]:>4} кал, ДП={d[2]:>4} кал {status}")
