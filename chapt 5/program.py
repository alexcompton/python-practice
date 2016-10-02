import random

def main():
    show_larger(random.randint(1, 5), random.randint(1, 5))

def show_larger(first, second):    
    diff = abs(first - second)    
    if diff == 0:
        print('The integers are equal, both are {}'.format(first))
    elif first > second:
        print("{} is larger than {} by {}".format(first,second,diff))
    else:
        print("{} is larger than {} by {}".format(second,first, diff))

main()