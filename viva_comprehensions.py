from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    :param start:
    :param stop:
    :param parity:
    :return:
    """
    listed_numbers = []
    for i in range(start, stop):
        if parity == Parity.ODD and i % 2 != 0:
            listed_numbers.append(int(i))
        elif parity == Parity.EVEN and i % 2 == 0:
            listed_numbers.append(int(i))
    return listed_numbers


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    # dict_using_comp = {i: strategy(i) for  i in range(start, stop)}
    # return dict_using_comp


def gen_set(val_in: str) -> set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    set_using_comp = {x.upper() for x in val_in if x.islower()}
    return set_using_comp


