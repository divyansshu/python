x = 10  # Global variable


def outer_function():
    x = 20  # Enclosing variable
    def inner_function():
        x = 30  # Local variable
        print("inner function ",x)  # Output: 30
    inner_function()
    print("outer function" ,x)  # Output: 20
outer_function()
print(x)  # Output: 10