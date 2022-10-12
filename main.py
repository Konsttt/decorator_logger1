from trace_utils import logger


@logger
def plus_and_multiple(a, b, c):
    return (a + b) * c


if __name__ == '__main__':
    # Задание1
    plus_and_multiple(1, 13, 3)


