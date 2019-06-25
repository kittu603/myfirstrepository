from bs4 import BeautifulSoup
from csv import writer
import requests
response = requests.get("https://www.rithmschool.com/blog")
#give data to soup

soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("article")

#creating CSV

with open("data3.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["Heading","link","date"])

    for article in articles:
        a_tag = article.find("a")
        names = a_tag.get_text()
        links = a_tag["href"]
        dates = article.find("time")["datetime"]
        csv_writer.writerow([names,links,dates])


















