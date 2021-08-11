# -*- coding: utf-8 -*-#

# Name:   tem1.py
# Author: tangzhuang
# Date:   2021/7/11
# desc:         

import sys

for line in sys.stdin:

    X, Y = map(int, line.split())
    t = X // 26 ** Y
    z = 0
    while t//10 != 0:
        z += 1
        t = t//10


    if 10**z * 26 ** Y >= X:
        print(z)
    else:
        print(z + 1)