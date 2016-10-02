import random

def main():
    array = list()
    for i in range(12):
        array.append(random.randint(50, 100))
    print("Here is the list of random integers...")
    for i in array:
        print("{}".format(i)),
    print("\nThe 4th element in the list is {}".format(array[3]))
    print("The element at index 9 is {}".format(array[9]))
    print("The smallest element in the list is {}".format(min(array)))
    array = change_list(array)
    print("change_list returned this sorted list...")
    for i in array:
        print("{}".format(i)),

def change_list(array): 
    array = sorted(array[3:9:1])
    print("The size of the list is now {}".format(len(array)))
    return array

main()