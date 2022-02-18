#!/usr/bin/env python3

import math

numbers = open('input.txt').read().strip().split('\n')

total = sum(math.floor(int(number) / 3) - 2 for number in numbers)
print(total)
