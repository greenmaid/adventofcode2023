#!/usr/bin/env python3

import os
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def getCalibNumb1(line: str) -> int:
    first = ""
    for char in line:
        if char in "0123456789":
            first = char
            break
    last = ""
    for char in line[::-1]:
        if char in "0123456789":
            last = char
            break
    return int(f"{first}{last}")


def getSumOfCalibNum1(lines: List[str]) -> int:
    result = 0
    for line in lines:
        result += getCalibNumb1(line)
    return result

############


DIGIT_SPELL = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}


def getCalibNumb2(line: str) -> int:
    first = ""
    last = ""
    for i in range(len(line)):
        if line[i] in "0123456789":
            if first == "":
                first = line[i]
            last = line[i]
        if line[i:][0:3] in DIGIT_SPELL:
            if first == "":
                first = DIGIT_SPELL[line[i:][0:3]]
            last = DIGIT_SPELL[line[i:][0:3]]
        if line[i:][0:4] in DIGIT_SPELL:
            if first == "":
                first = DIGIT_SPELL[line[i:][0:4]]
            last = DIGIT_SPELL[line[i:][0:4]]
        if line[i:][0:5] in DIGIT_SPELL:
            if first == "":
                first = DIGIT_SPELL[line[i:][0:5]]
            last = DIGIT_SPELL[line[i:][0:5]]
    return int(f"{first}{last}")


def getSumOfCalibNum2(lines: List[str]) -> int:
    result = 0
    for line in lines:
        result += getCalibNumb2(line)
    return result


calibration_instructions = read_input(f"{SCRIPT_DIR}/input.txt")
result1 = getSumOfCalibNum1(calibration_instructions)
print("Result1 = ", result1)

result2 = getSumOfCalibNum2(calibration_instructions)
print("Result1 = ", result2)
