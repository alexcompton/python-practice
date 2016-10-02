from sys import argv

def main():
    target = open('friends.txt')
    dump = target.read()
    dump = dump.split('\n')
    zipped = zip(dump[::2],dump[1::2])
    sum = 0.0
    for item in zipped:
        print('My friend {} is {}'.format(item[0], item[1]))
        sum += float(item[1])
    print('Average age of friends is {:0.1f}'.format(sum/len(zipped)))
    target.close()

main()