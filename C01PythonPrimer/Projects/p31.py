def make_change(price, paid, system):
    assert paid >= price, "You still have to rack, my dear friend."
    change = dict()
    money_back = paid - price
    for coin in sorted(system, reverse=True):
        change[coin] = money_back // coin
        money_back %= coin
    return change


if __name__ == "__main__":
    price = 42
    paid = 69
    system = [1, 2, 5]
    print(price, paid, system, make_change(price, paid, system))

    price = 42
    paid = 69
    system = [1, 10]
    print(price, paid, system, make_change(price, paid, system))

    try:
        price = 69
        paid = 42
        system = [1, 10]
        print(price, paid, system, make_change(price, paid, system))
    except Exception as e:
        print(e)
