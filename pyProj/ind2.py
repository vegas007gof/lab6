#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = str(input("Put some text: "))
    len = len(s)
    m = int(input("Put number of first letter you want to swap: "))
    n = int(input("Put number of second letter you want to swap: "))
    s1 = s[0:m]
    l1 = s[m]
    s2 = s[(m + 1):n]
    l2 = s[n]
    s = s1 + l2 + s2 + l1
    print(s)