from bs4 import BeautifulSoup
import requests,openpyxl
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title='IMDB Top 250'
sheet.append(['Rank','Movie Name','Year','iMDB Rating'])

source=requests.get('https://www.imdb.com/chart/top/')
#In order to capture error, whether the website is exists or not, we use raise for status inside a try and except block
try:
    source=requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()
    soup=BeautifulSoup(source.text,'html.parser')
    #Takes the html content of the webpage and parse it using parser and return a beautifulsoup object
    #print(soup) will print the html content in terminal
    movies=soup.find('tbody',class_='lister-list').find_all('tr')
    #tbody is the tag for the table body, class_ is for the class of the tag, i.e. lister-list
    for movie in movies:
        name=movie.find('td',class_='titleColumn').a.text 
        #a is for anchor tag, text is for the text inside the anchor tag, i.e. the name of the movie
        
        year=movie.find('td',class_="titleColumn").span.text
        #span is for the year of the movie, text is for the text inside the span tag, i.e. the year of the movie
        
        rank=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        #get_text(strip=True) will remove the extra spaces and split will split the string at the given character and return a list
        
        rating=movie.find('td',class_="ratingColumn imdbRating").strong.text
        #strong is for the strong tag, i.e. the rating of the movie
        print(rank,name,year,rating)
        sheet.append([rank,name,year,rating])
except Exception as e:
    print(e)
path='' #Give Path where your project is located, so that the excel file will also get saved there.
excel.save(path)

