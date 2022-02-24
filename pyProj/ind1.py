#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = str(input("Put some text: "))
    c = 0

    if (s[0] == ' ') and (s[len(s) - 1] == ' '):
        for i in s:
            if i == ' ':
                c += 1
        print (f"Количество слов в строке = {c - 1}")
    else:
        for i in s:
            if i == ' ':
                c += 1
        print(f"Количество слов в строке = {c + 1}")