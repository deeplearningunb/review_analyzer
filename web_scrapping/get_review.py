from bs4 import BeautifulSoup
import requests
import csv

class ReviewScrapper:
    
    def get_page(self,url):
        aux = 1
        csv_data = []

        while(aux != 0):
            url_get = url +"/reviews/?page=" + str(aux)
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

    def create_csv(self, csv_data, url):
        url = url.replace("https://www.rottentomatoes.com/m/","")
        with open("movies/" + url + '.csv', 'w') as csvFile:
            writer = csv.writer(csvFile, delimiter='|')
            writer.writerows(csv_data)
            csvFile.close()

if __name__ == "__main__":
    url = 'https://www.rottentomatoes.com/m/captain_marvel'
    test = ReviewScrapper()
    test.get_page(url)
