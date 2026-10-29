def f(x):
     if x == 0:
         return "zero" # True
     elif x > 0:
         return "positive" # True
     else:
         return "" # False


def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie

chocolate = cake()
more_chocolate, more_cake = chocolate(), cake

def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y

d = lambda f: f(4)  # They can have functions as arguments as well.
def square(x):
    return x * x


higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x


