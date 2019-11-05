#!/usr/bin/env python3

import operator


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}


def split_args(myarg):
    """
    split args splits the operans and the operations into a list

    myarg: non empty string
    """

    if len(myarg) == 0:
        return [];

    return



def calculate(myarg):
    stack = list()
    #TODO moe intelligent splittting
    #arg_list = split_arga(mayrg)
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            #handle [[
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
