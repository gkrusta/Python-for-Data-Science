#def ft_tqdm(lst: range) -> None:
from time import sleep
from tqdm import tqdm
def main():
    for elem in tqdm(range(200)):
        sleep(0.5)
        yield elem
 


if __name__ == "__main__":
    for value in main():
        pass