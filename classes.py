from typing import Any, List, Literal
from json import JSONEncoder


class DistanceTime:
    distance: str
    time: str
    total: str

    def __init__(self) -> None:
        self.distance: str = ''
        self.time: str = ''
        self.total: str = ''

    def __repr__(self) -> str:
        return f'dist: {self.distance}, time: {self.time}, total: {self.total}\n'

    def __str__(self) -> str:
        return self.__repr__()


class Person:
    def __init__(self) -> None:
        self.initials: str = ''
        self.distances: List[DistanceTime] = []

    def __repr__(self) -> str:
        return f'{self.initials} {self.distances}'

    def __str__(self) -> str:
        return self.__repr__()


class ChampInfo:
    def __init__(self) -> None:
        self.distance: Literal['50m'] | Literal['100m'] | Literal['200m'] | Literal['400m'] = ''
        self.swimmers: List[Person] = []

    def __str__(self) -> str:
        return f'distance {self.distance}, swimmers: {self.swimmers}'


class Encoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__
