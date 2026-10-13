import numpy as np
import matplotlib.pyplot as plt


def calculate_optimal_price(a: float, b: float, c: float) -> tuple[float, float]:
    """
    Calculates the optimal price and maximum profit using a quadratic demand model.
    Equation: f(x) = ax^2 + bx + c

    Args:
        a (float): The coefficient of the quadratic term (must be negative for a maximum).
        b (float): The coefficient of the linear term.
        c (float): The constant term (fixed costs/initial offset).

    Returns:
        tuple[float, float]: A tuple containing (optimal_price, max_profit).

    Raises:
        ValueError: If coefficient 'a' is >= 0, meaning no maximum profit exists.
    """
    if a >= 0:
        raise ValueError("Coefficient 'a' must be negative to find a maximum profit.")

    # Inżynieryjne wyliczenie wierzchołka paraboli (p i q)
    optimal_price = -b / (2 * a)
    max_profit = a * (optimal_price ** 2) + b * optimal_price + c

    return optimal_price, max_profit


def plot_profit_curve(a: float, b: float, c: float, opt_price: float, max_profit: float) -> None:
    """
    Generates and displays a business plot of the profit function.
    """
    # Generowanie 100 punktów cenowych od 0 do dwukrotności ceny optymalnej
    prices = np.linspace(0, opt_price * 2, 100)
    profits = a * (prices ** 2) + b * prices + c

    plt.figure(figsize=(10, 6))
    plt.plot(prices, profits, label='Profit Curve', color='#1f77b4', linewidth=2.5)

    # Zaznaczenie punktu optymalnego (wierzchołka)
    plt.scatter([opt_price], [max_profit], color='red', zorder=5, s=100)
    plt.annotate(f'Optimal Point\n({opt_price:.2f} PLN, {max_profit:.2f}k PLN)',
                 xy=(opt_price, max_profit),
                 xytext=(opt_price + 1, max_profit - 5),
                 arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
                 fontsize=11)

    # Formatowanie wykresu
    plt.title('Microeconomic Profit Maximization Model', fontsize=14, fontweight='bold')
    plt.xlabel('Price (PLN)', fontsize=12)
    plt.ylabel('Profit (in thousands PLN)', fontsize=12)
    plt.axhline(0, color='black', linewidth=1)  # Oś X
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()

    # Wyświetlenie
    plt.show()


if __name__ == "__main__":
    # Parametry dla naszej wczorajszej funkcji: f(x) = -2x^2 + 24x - 40
    A, B, C = -2, 24, -40

    try:
        print("Initializing Market Optimization Engine...")
        opt_price, max_prof = calculate_optimal_price(A, B, C)

        print("-" * 40)
        print(f"Optimal Product Price:      {opt_price:.2f} PLN")
        print(f"Maximum Expected Profit:    {max_prof:.2f}k PLN")
        print("-" * 40)

        # Uruchomienie wizualizacji
        plot_profit_curve(A, B, C, opt_price, max_prof)

    except ValueError as e:
        print(f"CRITICAL ERROR: {e}")