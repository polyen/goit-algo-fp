import random
import matplotlib.pyplot as plt

def is_inside(x, y):
    return y <= x ** 3


def monte_carlo_simulation(num_experiments):
    out = {i: 0 for i in range(2, 13)}
    for _ in range(num_experiments):
        step = random.randint(1, 6) + random.randint(1, 6)
        out[step] += 1

    for i in range(2, 13):
        out[i] /= num_experiments

    return out


if __name__ == "__main__":
    simulated_probs = monte_carlo_simulation(1000000)

    theoretical_probabilities = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36
    }

    # Порівняння результатів симуляції з аналітичними розрахунками
    sums = list(range(2, 13))

    print("|{:^10}|{:^30}|{:^30}|".format("Сума","Імовірність (Монте-Карло)","Імовірність (Аналітична)"))
    for sum_value in sums:
        print(
            "|{:^10}|{:^30}|{:^30}|".format(f"{sum_value}",f"{simulated_probs[sum_value] * 100:.2f}%",f"{theoretical_probabilities[sum_value] * 100:.2f}%"))

    fig, ax = plt.subplots()
    ax.bar(sums, simulated_probs.values(), alpha=0.6, label='Монте-Карло')
    ax.plot(sums, [theoretical_probabilities[sum] for sum in sums], color='red', marker='o', linestyle='dashed',
            linewidth=2, markersize=6, label='Аналітичні')
    ax.set_xlabel('Сума')
    ax.set_ylabel('Ймовірність')
    ax.set_title('Ймовірність суми чисел при киданні двох кубиків')
    ax.legend()

    plt.show()

