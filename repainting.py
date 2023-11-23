nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5
BAGS_PRICE = 0.4

nylon += 2
paint += paint * 0.10  # += eяual to paint + paint + paint * 0.10

material_price = (nylon * NYLON_PRICE) + \
    (paint * PAINT_PRICE) + \
    (thinner * THINNER_PRICE) + \
    BAGS_PRICE

price_for_one_hour_of_work = material_price * 0.30
total_price = material_price + (price_for_one_hour_of_work * work_hours)

print(total_price)
