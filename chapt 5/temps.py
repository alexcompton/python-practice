import random

def main():
    temp = input("Enter a temperature ")
    conversion = raw_input("Was that input Fahrenheit or Celsius c/f? ")
    if conversion == "c":
        c_to_f(temp)
    else:
        print("{:0.3f}".format(f_to_c(temp)))

def c_to_f(temp):
    print("{:0.3f}".format(temp * 1.8 + 32))

def f_to_c(temp): 
    return (temp - 32) / 1.8

main()