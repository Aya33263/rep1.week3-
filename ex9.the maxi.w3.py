#define a function that returns the maximum of two number


def max_of_two(y,z):
    #check if x is greater than y
    if y > z :
        return y
    else:
        return z
#define a function that return the maxime of three number

def max_of_three(x,y,z) :
    #call max_of_two function to find the maximum of y and z
    #then compare it with x to find thr over all maximum

    return max_of_two (x,max_of_two(y,z))
x=int(input("enter first number : "))
y=int(input("enter sec number : "))
z=int(input("enter third number : "))

print(max_of_three(x,y,z))

