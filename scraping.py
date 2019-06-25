
from random import choice
from bs4 import BeautifulSoup
from csv import writer
import requests

def print_quote():
    global author, random_quote, link
    link = "http://quotes.toscrape.com"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")
    all_data = []
    for quote in quotes:
        all_data.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
             })
    random_quote = choice(all_data)
    author = random_quote["author"]
    print(random_quote["text"])
    with open("quote.csv","w") as file:
        csv_writer = writer(file)
        csv_writer.writerow(random_quote)
        csv_writer.writerow(random_quote["text"])
    user_input(4)

def generate_hints(no_of_guesses):
    if no_of_guesses == 3:
        bio_details = requests.get(link + random_quote["bio-link"])
        bio_soup = BeautifulSoup(bio_details.text, "html.parser")
        born_date = bio_soup.find(class_="author-born-date").get_text()
        born_place = bio_soup.find(class_="author-born-location").get_text()
        print(f"Here's a hint :- The Author was born on {born_date} {born_place} ")
        user_input(no_of_guesses)
    elif no_of_guesses == 2:
        auth_first_letter = random_quote["author"][0]
        print(f"Author's first letter in name is {auth_first_letter}")
        user_input(no_of_guesses)
    elif no_of_guesses == 1:
        auth_last_letter = random_quote["author"][-1]
        print(f"Author's last letter in name is {auth_last_letter}")
        user_input(no_of_guesses)
    else:
        print("You failed ")
        global play_again
        play_again = input("Do u want to play again? (Y/N)")
        if play_again == "Y":
            #generate new quote
            print_quote()
        print("Thanks for Playing..Bye!!!")

def user_input(no_of_guesses):
    user_ans = input("guess who has said this!!!!")
    # validate user answer with quote author name
    if user_ans == author:
        print("You guessed correctly!!!")
    else:
        no_of_guesses -= 1
        print(f"guess remaining {no_of_guesses}")
        generate_hints(no_of_guesses)
#print quote when u want to play
play_again = None
if play_again != "N" :
    print_quote()











