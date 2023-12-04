#!/usr/bin/env python3

import os
import re
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse_games(lines: List[str]) -> List[int]:
    result = []
    for line in lines:
        impossible = False
        match = re.search(r'Game (\d+):(.+)', line)
        if not match:
            raise Exception("Boom")
        id = int(match.group(1))
        game = match.group(2)
        game_draws = game.split(";")
        for draw in game_draws:
            match_red = re.search(r'(\d+) red', draw)
            if match_red and int(match_red.group(1)) > 12:
                impossible = True
                break
            match_green = re.search(r'(\d+) green', draw)
            if match_green and int(match_green.group(1)) > 13:
                impossible = True
                break
            match_blue = re.search(r'(\d+) blue', draw)
            if match_blue and int(match_blue.group(1)) > 14:
                impossible = True
                break
        if not impossible:
            result.append(id)
    return result


games = read_input(INPUT)
possibles = parse_games(games)
print("Result1 = ", sum(possibles))

# ========================================


def parse_games2(lines: List[str]) -> List[int]:
    result = []
    for line in lines:
        match = re.search(r'Game (\d+):(.+)', line)
        if not match:
            raise Exception("Boom")
        game = match.group(2)
        game_draws = game.split(";")
        min_red = 0
        min_green = 0
        min_blue = 0
        for draw in game_draws:
            match_red = re.search(r'(\d+) red', draw)
            if match_red and int(match_red.group(1)) > min_red:
                min_red = int(match_red.group(1))
            match_green = re.search(r'(\d+) green', draw)
            if match_green and int(match_green.group(1)) > min_green:
                min_green = int(match_green.group(1))
            match_blue = re.search(r'(\d+) blue', draw)
            if match_blue and int(match_blue.group(1)) > min_blue:
                min_blue = int(match_blue.group(1))
        result.append(min_red * min_green * min_blue)
    return result


games = read_input(INPUT)
powers = parse_games2(games)
print("Result2 = ", sum(powers))
