import random
import matplotlib.pyplot as plt


ANALYTICAL_PROBABILITIES = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}


def monte_carlo_simulation(num_rolls):
    counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        counts[total] += 1

    probabilities = {s: count / num_rolls for s, count in counts.items()}

    return counts, probabilities


def print_comparison_table(mc_probs, num_rolls):
    print(f"\n{'=' * 70}")
    print(f"РЕЗУЛЬТАТИ СИМУЛЯЦІЇ МОНТЕ-КАРЛО ({num_rolls:,} кидків)")
    print('=' * 70)
    print(f"{'Сума':<8} {'Монте-Карло':<18} {'Аналітична':<18} {'Різниця':<12}")
    print('-' * 70)

    total_diff = 0
    for s in range(2, 13):
        mc = mc_probs[s] * 100
        analytical = ANALYTICAL_PROBABILITIES[s] * 100
        diff = abs(mc - analytical)
        total_diff += diff

        ways = int(ANALYTICAL_PROBABILITIES[s] * 36)
        print(f"{s:<8} {mc:>6.2f}%{'':<10} {analytical:>6.2f}% ({ways}/36){'':<4} {diff:>6.3f}%")

    print('-' * 70)
    print(f"Середня абсолютна похибка: {total_diff / 11:.4f}%")


def plot_results(mc_probs, num_rolls):
    sums = list(range(2, 13))
    mc_values = [mc_probs[s] * 100 for s in sums]
    analytical_values = [ANALYTICAL_PROBABILITIES[s] * 100 for s in sums]

    x = range(len(sums))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))

    bars1 = ax.bar([i - width/2 for i in x], mc_values, width, label='Монте-Карло', color='steelblue')
    bars2 = ax.bar([i + width/2 for i in x], analytical_values, width, label='Аналітична', color='coral')

    ax.set_xlabel('Сума на кубиках', fontsize=12)
    ax.set_ylabel('Ймовірність (%)', fontsize=12)
    ax.set_title(f'Порівняння ймовірностей: Монте-Карло ({num_rolls:,} кидків) vs Аналітичні', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    for bar, val in zip(bars1, mc_values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                f'{val:.1f}', ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.savefig('monte_carlo_results.png', dpi=150)
    plt.show()


def convergence_analysis():
    print("\n" + "=" * 70)
    print("АНАЛІЗ ЗБІЖНОСТІ")
    print("=" * 70)
    print(f"{'Кількість кидків':<20} {'Середня похибка':<20} {'Макс похибка':<15}")
    print('-' * 70)

    for n in [100, 1000, 10000, 100000, 1000000]:
        _, probs = monte_carlo_simulation(n)
        errors = [abs(probs[s] - ANALYTICAL_PROBABILITIES[s]) * 100 for s in range(2, 13)]
        avg_err = sum(errors) / len(errors)
        max_err = max(errors)
        print(f"{n:<20,} {avg_err:<20.4f}% {max_err:<15.4f}%")


if __name__ == "__main__":
    random.seed(42)

    print("МЕТОД МОНТЕ-КАРЛО: СИМУЛЯЦІЯ КИДАННЯ ДВОХ КУБИКІВ")
    print("=" * 70)

    print("\nАналітичні ймовірності (теоретичні):")
    print("-" * 40)
    for s in range(2, 13):
        ways = int(ANALYTICAL_PROBABILITIES[s] * 36)
        prob = ANALYTICAL_PROBABILITIES[s] * 100
        print(f"Сума {s:>2}: {prob:>6.2f}% ({ways}/36)")

    NUM_ROLLS = 1000000

    counts, mc_probs = monte_carlo_simulation(NUM_ROLLS)

    print_comparison_table(mc_probs, NUM_ROLLS)

    convergence_analysis()

    print("\n" + "=" * 70)
    print("ВИСНОВКИ")
    print("=" * 70)
    print("1. Метод Монте-Карло дає результати, близькі до аналітичних")
    print("2. Точність зростає зі збільшенням кількості симуляцій")
    print("3. При 1,000,000 кидків похибка < 0.1%")
    print("4. Розподіл симетричний відносно суми 7 (найбільш ймовірна)")

    plot_results(mc_probs, NUM_ROLLS)
