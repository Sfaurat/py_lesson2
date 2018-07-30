from  datetime import datetime, timedelta
def fib(n):
    """Вычисления числа Фибоначчи."""
    a = 2
    b = 3
    for __ in range(n):
        a, b = b, a + b
    return a


def bunnies(day):
    """
    Подсчёт выводка кроликов.
    Кролики размножаются раз в 10 дней в соответствии с числами Фибоначчи.
    """
    how_many_times = day // 10
    return fib(how_many_times)

def milk(day):
    """
    Подсчет количества молока на текущий день.
    В первые 3 дня месяца получаем полную норму в 500мл молока.
    Каждые следующий третий день получаем на 50мл меньше.
    Т.к. в условии не говорилось что считать началом месяца - считается по календарному.
    """
    date = datetime.now()  # Получаем сегодняшнюю дату
    if day % 3 == 0:                          # В первый день (0 день - сегодня) получаем молоко, дальше каждые три дня
        nextDay = date + timedelta(days=day)  # получаем дату от текущего дня
        print('date', nextDay.strftime('%m/%d'))      # т.к. удой зависит от даты, то выведем ее
        cycle = nextDay.day//3
        count = 500-50*cycle
        return count
    return 0


