

def even(X):
    """
    Test function to see if it is even or odd number
    """
    if not X % 2:
        return True
    return False


def ft_filter(f, L):
    """
    Replicates the original filter function.
    Applies `f` to each item in `L` and returns an iterator
    containing items where `f(L)` is True
    """
    if not L[0]:
        return []
    result = [x for x in L if f(x)]
    return result
    #print(result)


if __name__ == "__main__":
    """
    Handle user input and check for Assertion error
    """
    L = [1, 2, 3, 4, 5]
    ft_filter(even, L)
