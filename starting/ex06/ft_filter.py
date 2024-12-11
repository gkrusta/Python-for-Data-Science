def even(X):
    """
    Test function to see if it is an even number.
    Returns True if even, False otherwise.
    """
    return X % 2 == 0


def ft_filter(f, L):
    """
    Replicates the original filter function.
    Applies `f` to each item in `L` and returns a list
    containing items where `f(item)` is True.
    """
    return [x for x in L if f(x)]


def main():
    """
    Main function to test the ft_filter function with a sample list.
    """
    L = [1, 2, 3, 4, 5]
    result = ft_filter(even, L)
    print(result)


if __name__ == "__main__":
    main()
