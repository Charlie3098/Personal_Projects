import operator

print('Enter 2 Numbers\n')

#Input
number_1 = float(input('Number 1: ')) #casts the inputs as floats/ints to be treated like numbers instead of strings
number_2 = float(input('Number 2: '))

#Calculation
def calculation():
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    operator_var = input('Enter an operator (+, -, *, /):\n ')

    operator_funct = ops[operator_var]
    answer = operator_funct(number_1, number_2)
    print(answer)

calculation()

input("Press enter to exit the program: ")
