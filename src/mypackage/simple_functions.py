

def f(x):
    return x


def is_palindrome(x):
    x = x.lower().replace(" ", "").replace("?", "")
    return x == x[::-1]
