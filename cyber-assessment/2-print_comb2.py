#!/usr/bin/python3
for i in range(100):
    print(i // 10, i % 10, sep='', end=', ' if i < 99 else '\n')
