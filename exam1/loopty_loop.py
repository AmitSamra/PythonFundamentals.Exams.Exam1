from typing import Callable, List


def generate_list(start: int, stop: int, step: int = 1) -> List[int]:
    """
    Generate a list of integers.

    :param start: Where to start the list (inclusive).
    :param stop: Where to stop the list (exclusive).
    :param step: How many digits apart each number is from the others around it.
    :return: A list of integers.
    """
    a = list(range(start, stop, step))
    return a


def generate_list_with_strategy(start: int, stop: int, step: int, strategy: Callable) -> List[int]:
    """
    Generate a list of integers.

    :param start: Where to start the list (inclusive).
    :param stop: Where to stop the list (exclusive).
    :param step: How many digits apart each number is from the others around it.
    :param strategy: A function to manipulate each digit .
    :return: A list of integers.
    """
    a = [strategy(x) for x in range(start, stop, step)]
    return a

# Exercise 4