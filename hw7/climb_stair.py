

# There are 
# n steps in a stair. You can either climb 1 or 2 steps each time.
#  Find how many different ways you can climb to the top?
# landon ward
def climb_stair(n):
    # Your code goes here:
    if n == 0 or n == 1:
        return 1
    
    f1 = 1
    f2 = 1

    # f(n)
    for i in range(2, n + 1):
        current = f1 + f2
        f2 = f1
        f1 = current
    
    return f1
    



if __name__ == "__main__":
    print(climb_stair(10))
    print(climb_stair(20))
    print(climb_stair(30))

