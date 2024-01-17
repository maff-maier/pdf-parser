from typing import Any, List, Literal
from json import JSONEncoder


class DistanseTime:
    distance: str
    sum_time: str
    time: str

    def __repr__(self) -> str:
        return f'dist: {self.distance} sum: {self.sum_time} time: {self.time}'

    def __str__(self) -> str:
        return self.__repr__()


class Person:
    initials: str
    distanses: List[DistanseTime]

    def __repr__(self) -> str:
        return f'{self.initials} {self.distanses}'

    def __str__(self) -> str:
        return self.__repr__()


class Ages:
    range_name: str
    ages: List[Person]

    def __repr__(self) -> str:
        return f'{self.range_name} {self.ages}'

    def __str__(self) -> str:
        return self.__repr__()


class ChampInfo:
    champ_type: Literal['Final'] | Literal['Prepatory']
    distance: 'str'
    sex: Literal['M'] | Literal['F']
    participants: List[Ages]

    def __str__(self) -> str:
        return f'{self.champ_type} distance {self.distance}, sex {self.sex}, parts: {self.participants}'


class Encoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__
