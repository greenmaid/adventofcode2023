#!/usr/bin/env python3

import os
import re
from typing import List, Dict

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_input(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = f.read().splitlines()
    return lines


def run1(lines) -> int:
    result = 0
    for line in lines:
        match = re.search(r"^Card (\s*\d+): (.+) \| (.+)$", line)
        if not match:
            raise Exception("Boom")
        winning_numbers = [int(s) for s in match.group(2).split()]
        own_numbers = [int(s) for s in match.group(3).split()]
        count = 0
        for num in own_numbers:
            if num in winning_numbers:
                count += 1
        if count:
            result += 2 ** (count - 1)
    return result


data = read_input(INPUT)
result1 = run1(data)
print("Result1 = ", result1)

# =========================================


def create_deck(lines: List[str]) -> Dict[int, List[int]]:
    cards: Dict[int, List[int]] = dict()
    for line in lines:
        match = re.search(r"^Card (\s*\d+): (.+) \| (.+)$", line)
        if not match:
            raise Exception("Boom")
        id = int(match.group(1))
        winning_numbers = [int(s) for s in match.group(2).split()]
        own_numbers = [int(s) for s in match.group(3).split()]
        cards[id] = []
        count = 0
        for num in own_numbers:
            if num in winning_numbers:
                count += 1
                cards[id].append(id + count)
    return cards


def add_card_deck(deck: Dict[int, int], cards: Dict[int, List[int]], added_card: int) -> Dict[int, int]:
    deck[added_card] += 1
    for new_card in cards[added_card]:
        deck = add_card_deck(deck, cards, new_card)
    return deck


def run2(lines: List[str]) -> int:
    cards = create_deck(lines)
    deck = {i: 1 for i in cards.keys()}
    for card_id, won_cards in cards.items():
        for new_card in won_cards:
            deck = add_card_deck(deck, cards, new_card)
    return sum(deck.values())


data = read_input(INPUT)
result2 = run2(data)
print("Result2 = ", result2)
