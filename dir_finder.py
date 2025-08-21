import requests as req
from urllib.parse import urlparse
from time import sleep
from rich import print

URL = input("Please Enter a URL: ")
FILE_DEST = input("Enter Your Wordslist File Destination: ")
WORDS_LIST = []

def find_dir(word: str) -> None:
  try:
    res = req.get(f'{URL}/{word.strip()}')
    
    if res.status_code >= 400:
      print(f'[red]Error. Directory Not Found -> [bold]/{word.strip()}[/][/]')
    else:
      print(f'[green]New Directory Found! -> [bold]/{word.strip()}[/][/]')
      sleep(0.5)
  except:
    print("[yellow]There was an Error. Please Try Again.[/]")

if __name__ == '__main__':
  try:
    result = urlparse(URL)
    if not all([result.scheme, result.netloc]):
      raise TypeError
    
    with open(file=FILE_DEST, mode="r", encoding="utf-8") as file:
      WORDS_LIST = file.readlines()

    for word in WORDS_LIST:
      find_dir(word)
  except:
    print("Please enter a valid URL.")
