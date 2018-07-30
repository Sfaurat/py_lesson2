import random


def sowing(grains):
    """
    Случайное засевание поля.
    0 - ничего не выросло, 1 - урожайная ячейка.
    """
    field = []
    for _ in range(grains):
        i = random.randint(0, 1)
        field.append(i)
    return field
    # return [random.randint(0, 1) for _ in range(grains)]


def corn(day):
    """Подсчёт початков кукурузы."""
    grains = (day + 1) * 2
    harvest = sowing(grains)
    counter = 0
    for corns in harvest:
        if corns == 1:
            counter += 1
    return counter


def berry(day):
    """Подсчет ягод."""
    cycle = day // 15  # Получаем коэффициент увеличения куста по времени

    minim = 15 ** cycle * 50
    maxim = 15 ** cycle * 100

    count = random.randint(minim, maxim)
    return count
