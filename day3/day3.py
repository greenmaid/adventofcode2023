#!/usr/bin/env python3

import os
from typing import List, Dict, Tuple

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_inputinto_table(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        lines = f.read().splitlines()
    map = []
    for line in lines:
        map.append([s for s in line])
    return map


def getCardCoord(x: int, y: int, card: List[List[str]]):
    max_x = len(card[0])
    max_y = len(card)
    if x < 0 or x >= max_x or y < 0 or y >= max_y:
        return "."
    return card[y][x]


def parse_card1(card: List[List[str]]) -> List[int]:
    max_x = len(card[0])
    max_y = len(card)
    numbers = []
    buffer = ""
    isPart = False
    for y in range(max_y):
        for x in range(max_x + 1):
            val = getCardCoord(x, y, card)
            if val in "0123456789":
                buffer += val
                if val not in "0123456789.":
                    isPart = True
                if (
                    getCardCoord(x - 1, y, card) not in "0123456789."
                    or getCardCoord(x + 1, y, card) not in "0123456789."
                ):
                    isPart = True
                if (
                    getCardCoord(x, y + 1, card) != "."
                    or getCardCoord(x, y - 1, card) != "."
                ):
                    isPart = True
                if (
                    getCardCoord(x - 1, y + 1, card) != "."
                    or getCardCoord(x - 1, y - 1, card) != "."
                ):
                    isPart = True
                if (
                    getCardCoord(x + 1, y + 1, card) != "."
                    or getCardCoord(x + 1, y - 1, card) != "."
                ):
                    isPart = True
            else:
                if buffer and isPart:
                    numbers.append(int(buffer))
                buffer = ""
                isPart = False
    return numbers


card = read_inputinto_table(INPUT)
numbers = parse_card1(card)
print("Result1 = ", sum(numbers))

# =======================================================


def parse_card2(card: List[List[str]]) -> Dict[Tuple[int, int], List[int]]:
    max_x = len(card[0])
    max_y = len(card)
    stars: Dict[Tuple[int, int], List[int]] = dict()
    buffer = ""
    current_star = None
    for y in range(max_y):
        for x in range(max_x + 1):
            val = getCardCoord(x, y, card)
            if val in "0123456789":
                buffer += val
                if getCardCoord(x + 1, y, card) == "*":
                    current_star = (x + 1, y)
                if getCardCoord(x - 1, y, card) == "*":
                    current_star = (x - 1, y)
                if getCardCoord(x, y + 1, card) == "*":
                    current_star = (x, y + 1)
                if getCardCoord(x, y - 1, card) == "*":
                    current_star = (x, y - 1)
                if getCardCoord(x + 1, y + 1, card) == "*":
                    current_star = (x + 1, y + 1)
                if getCardCoord(x - 1, y - 1, card) == "*":
                    current_star = (x - 1, y - 1)
                if getCardCoord(x + 1, y - 1, card) == "*":
                    current_star = (x + 1, y - 1)
                if getCardCoord(x - 1, y + 1, card) == "*":
                    current_star = (x - 1, y + 1)
            else:
                if buffer and current_star:
                    if current_star in stars:
                        stars[current_star].append(int(buffer))
                    else:
                        stars[current_star] = [int(buffer)]
                buffer = ""
                current_star = None
    return stars


def compute_gear_ratio(stars: Dict[Tuple[int, int], List[int]]) -> int:
    result = 0
    for star, numbers in stars.items():
        if len(numbers) == 2:
            result += numbers[0] * numbers[1]
    return result


card = read_inputinto_table(INPUT)
stars = parse_card2(card)
print("Result2 = ", compute_gear_ratio(stars))
