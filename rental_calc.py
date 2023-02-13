def calc_rental_property(income, expenses, total_investment):
    return int(((income - expenses) * 12)/total_investment)


print(calc_rental_property(2000, 1600, 50000))