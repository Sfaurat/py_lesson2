from farm import plants
import farm.livestock as lvst


def economy(current_day, order, ec_d):
    """Составление отчета."""
    ec_d['corns'] = plants.corn(current_day)
    ec_d['bunnies'] = lvst.bunnies(current_day)
    ec_d['berry'] = plants.berry(current_day)
    ec_d['milk'] = lvst.milk(current_day)

    report = 'There are\n {} corns\n {} bunnies\n {} berry\n {} milk.'. \
        format(ec_d['corns'],
               ec_d['bunnies'],
               ec_d['berry'],
               ec_d['milk'])
    return report


if __name__ == '__main__':
    """
    Модуль управления фермой.
    Выводит отчет о запасах на ферме в определенном интервале дней.
    """
    days = 60

    house_economy = {
        'corns': 0,
        'bunnies': 0,
        'berry': 0,
        'milk': 0}
    for day in range(0, days + 1):
        print("Day №", day)
        print(economy(day, day % 30, house_economy))
        print('---' * 10)



