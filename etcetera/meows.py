def meow(n) -> str:
    '''
    Meow n times.

    :param n: Number of times to meows
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str 
    '''
    return 'meow\n' * n 
    #for _ in range(n):
        #print(f'meow')

number= int(input("Number: "))
meows=meow(number)
print(meows.title(), end="")