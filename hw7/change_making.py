
# minimum amount of coinss
# landon ward

def change_making(d, n):
    min_coins = {0: 0}

    for amount in range(1, n + 1):
        min_coins[amount] = float('inf') # big value
        for coin in d:
            if amount >= coin:
                min_coins[amount] = min(min_coins[amount], 1 + min_coins[amount - coin])

    return min_coins[n] if min_coins[n] != float('inf') else -1





if __name__ == "__main__":
    d=[1,3,4,5,6]
    n=10
    print(change_making(d,n))
    
    d=[1,2,4,6,8,10,22,23]
    n=40
    print(change_making(d,n))

    d=[1,2,10,11,12,15,19,30]
    n=1900
    print(change_making(d,n))

