from bs4 import BeautifulSoup
import requests
import csv
import os
import sys

class ReviewScrapper:
    
    def get_page(self,url):
        aux = 1
        csv_data = []
        url_test = url.replace("https://www.rottentomatoes.com/m/", "")

        if os.path.isfile("movies/" + url_test + ".csv"):
            return 0

        while(aux != 0):
            url_get = url + "/reviews/?page=" + str(aux)
            print(url_get)
            html_doc = requests.get(url_get)
            soup = BeautifulSoup(html_doc.text, 'html.parser')
            another = soup.find_all("p", class_="center")
            
            if another:
                aux = 0
            else:
                aux = aux + 1

            print(soup.find_all('row review_table_row'))
            for review in soup.find_all("div", class_="row review_table_row"):
                review_text = review.find("div", class_="the_review")

                if review.find("div", class_="review_icon icon small fresh"):
                    result = "Fresh"
                if review.find("div", class_="review_icon icon small rotten"):
                    result = "Rotten"

                element = [review_text.text.lstrip().rstrip(), result]
                csv_data.append(element)
        self.create_csv(csv_data, url)
        return 0

    def create_csv(self, csv_data, url):
        url = url.replace("https://www.rottentomatoes.com/m/","")
        with open("movies/" + url + '.csv', 'w') as csvFile:
            writer = csv.writer(csvFile, delimiter='|')
            writer.writerows(csv_data)
            csvFile.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    f = open(filename, "r")
    for i in f:
        url = str(i.replace("\n", ""))
        reviews = ReviewScrapper()
        reviews.get_page(url)
