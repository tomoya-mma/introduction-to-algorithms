def select_items(weights, prices, limit):
    price_of_unit = {}

    for i, (w, p) in enumerate(zip(weights, prices)):
        price_of_unit[i] = p / w

    price_of_unit_items = price_of_unit.items()
    sorted_price_of_unit_items = sorted(
        price_of_unit_items, key=lambda k: k[1], reverse=True)

    rest = limit
    items = {}
    for idx, value in sorted_price_of_unit_items:
        weight_to_load = weights[idx] if rest > limit - \
            weights[idx] else rest

        items[idx] = weight_to_load

        rest -= weight_to_load
        if rest == 0:
            break

    return items


if __name__ == '__main__':
    weights = [20, 30, 10]
    prices = [100, 120, 60]

    print("  i |", end='')
    for i in range(len(weights)):
        print(f"{i:^3}|", end='')
    print('')
    print("w[i]|", end='')
    for _w in weights:
        print(f"{_w:>3}|", end='')
    print('')
    print("p[i]|", end='')
    for _p in prices:
        print(f"{_p:>3}|", end='')
    print('')

    items = select_items(weights, prices, 50)
    print("--- result ---")
    total_price = 0.0
    for idx, weight in items.items():
        price = prices[idx] / weights[idx] * weight
        print(f"item: {idx}, weight: {weight}, price = {price}")

        total_price += price
    print(f"total price = {total_price}")
