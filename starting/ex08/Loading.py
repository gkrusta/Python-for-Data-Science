def ft_tqdm(lst: range) -> None:
    """
    A simplified tqdm progress bar using the yield operator.
    """
    total = len(lst)
    bar_len = 138
    progress = 0
    percentage = 0

    for i, elem in enumerate(lst, start=1):
        progress = i / total
        filled_bar = int(bar_len * progress)
        bar = "=" * filled_bar + ">" + " " * (bar_len - filled_bar)
        percentage = int(progress * 100)

        print(f"\r{percentage}%|[{bar}]| {i}/{total}", end="", flush=True)
        yield elem


def main():
    """
    Main function to test the ft_tqdm.
    """
    try:
        for elem in ft_tqdm(range(333)):
            pass
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
