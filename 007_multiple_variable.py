""" 
1. *args    -> apply multiple variable
2. *kwargs  -> apply multiple key-value varibale

"""

# Ex *awgs
def multiply(*argv):
    result = 1
    for number in argv:
        result *= number
    return result

result = multiply(1,2,3,4)
print(result)

check2 = [1,2,3,4]
print(multiply(*check2))

# Ex *kwargs
def show_score(**kwargs):
    for name, score in kwargs.items():
        print(f"{(name)}: {score}")

score_result = {'A':100, 'B':200}
show_score(**score_result)

#! When send the list of argument to the function have to use * or ** 