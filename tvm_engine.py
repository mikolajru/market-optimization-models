def present_value_of_perpetuity_payments_in_advance (pmt: float, k: float) -> float:
    """
    Calculate the present value of perpetuity.
    :param pmt (float): payment
    :param k (float): discount rate

    Returns:
        Present value of perpetuity in case of payment in advance.

    Raises:
        None
    """
    # Payment in advance
    pvp = pmt/ k * (1 + k)
    return pvp


def present_value_of_perpetuity_payments_in_arrears (pmt: float, k: float) -> float:
    """
        Calculate the present value of perpetuity.
        :param pmt (float): payment
        :param k (float): discount rate

        Returns:
            Present value of perpetuity in case of payment in arrears.

        Raises:
            None
    """

    # Payment in arrears
    pvpa = pmt / k
    return pvpa


def optimal_payment_amount (pva: float, r: float, n: float) -> float:
    """
          Calculate the optimal price of payment in case of fixed interest rate.
          :param pva (float): Present value of annuity
          :param r (float): interest rate
          :param n (float): number of periods

          Returns:
              Present value of perpetuity in case of payment in arrears.

          Raises:
              None
      """

    pmt = pva * (r / (1 - (1 + r) ** (-n)))
    return pmt


if __name__ == "__main__":
    loan_amount = 20000
    monthly_rate = 0.12 / 12
    total_months = 5 * 12

    calculated_pmt = optimal_payment_amount(loan_amount, monthly_rate, total_months)


    print(f"The optimal loan payment amount is: {calculated_pmt:.2f} PLN")