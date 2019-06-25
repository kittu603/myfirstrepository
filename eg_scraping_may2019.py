import csv
import requests
from bs4 import  BeautifulSoup
url = "https://www.rithmschool.com/blog"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
# title, blog , date
articles = soup.find_all("article")
with open("may_csV_scrapping.csv" ,"w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Blog, title, Date"])
    for article in articles:
        a_tag = article.find("a")
        blog = a_tag["href"]
        title = a_tag.get_text()
        date = article.find("time")["datetime"]
        csv_writer.writerow([blog,title,date])
