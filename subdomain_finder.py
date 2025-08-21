import requests as req
from urllib.parse import urlparse
from time import sleep
from rich import print

URL = input("Please Enter a URL: ")
FILE_DEST = input("Enter Your Wordslist File Destination: ")
WORDS_LIST = []

def find_subdomain(word: str) -> None:
  pass

if __name__ == '__main__':
  try:
    result = urlparse(URL)
    if not all([result.scheme, result.netloc]):
      raise TypeError
    
    with open(file=FILE_DEST, mode="r", encoding="utf-8") as file:
      WORDS_LIST = file.readlines()

    for word in WORDS_LIST:
      find_subdomain(word)
  except NameError as err:
    print("[yellow]Please enter a valid URL.[/]")
    print(err)
