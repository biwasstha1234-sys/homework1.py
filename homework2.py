def arithmetic(x, y):
  
    if isinstance(x, str):
        if isinstance(y, str):
            return x + y
        else:  # y is a float
            return x * int(y)
    else:  # x is a float
        if isinstance(y, str):
            return str(x) + y
        else:  # y is a float
            return x * y
