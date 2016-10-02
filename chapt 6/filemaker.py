from sys import argv

def main():
    target = open('friends.txt', 'w')
    while True:
        name = raw_input('Enter first name of friend or Enter to quit ')
        if name == '':
            break
        target.write('{}\n'.format(name))
        age = input('Enter age (integer) of this friend ')
        target.write('{}\n'.format(age))
    target.close()

main()