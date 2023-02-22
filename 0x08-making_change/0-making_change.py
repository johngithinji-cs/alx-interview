#!/usr/bin/python3
"""Making change O(n)"""


def makeChange(coins, total):
     """Clasic Bottom-Up dynamic programming"""
    coins = sorted(coins, reverse=True)
    count = 0
    
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
            
    if total == 0:
        return count
    else:
        return -1 if count == 0 else count
