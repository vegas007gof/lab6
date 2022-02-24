#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    text = input("Put some text: ")
    result = ''
    for i in text.split():
        if text.count(i) == 1:
            result += i + ' '
    print(result)