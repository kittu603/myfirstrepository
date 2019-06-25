from random import choice
from bs4 import BeautifulSoup
import csv
import requests

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




def ask_user(random_quote):
    no_of_guesses = 4
    print(random_quote["text"])

    print(f"guess remaining {no_of_guesses}")
    user_answer = input("guess who has said this!!!!")

    if user_answer:
        no_of_guesses-=1

    if user_answer == random_quote["author"]:
            print("Yayyyy")
    else:
        if no_of_guesses == 3:
            bio_details = requests.get(link + random_quote["bio-link"])
            bio_soup = BeautifulSoup(bio_details.text, "html.parser")
            born_date = bio_soup.find(class_="author-born-date").get_text()
            born_place = bio_soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint :- The Author was born on {born_date} {born_place} ")
            print(f"guess remaining {no_of_guesses}")
            user_answer = input("guess who has said this!!!!")
            if user_answer:
                no_of_guesses -= 1
            if user_answer == random_quote["author"]:
                print("Yayy")
            else:
                print(f"guess remaining {no_of_guesses}")
                auth_first_letter = random_quote["author"][0]
                auth_last_letter = random_quote["author"][-1]
                print(f"Author's first letter in name is {auth_first_letter}")
                user_answer = input("guess who has said this!!!!")
                no_of_guesses-=1
                if user_answer == random_quote["author"]:
                    print("Yayy")
                else:
                    print(f"guess remaining {no_of_guesses}")
                    print(f"Author's last letter in name is {auth_last_letter}")
                    user_answer = input("guess who has said this!!!!")
                    if user_answer == random_quote["author"]:
                        print("Yayy")
                    else:

                       print("failed")

        else:
            print("You failed")







if __name__ == "__main__":
    ask_user(random_quote)








