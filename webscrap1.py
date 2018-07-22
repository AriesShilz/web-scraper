import requests
import webbrowser
from bs4 import BeautifulSoup

query=input("Enter the URL: ")
search="http://www.google.de"
url="http://www.google.co.in/search?q="+(str(query))

response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")

for item in soup.select(".r a"):
   print(item.text)


for next_page in soup.select(".fl"):
   res=requests.get(search+next_page.get('href'))
   
   soup=BeautifulSoup(response.text,"lxml")
   
   for item in soup.select(".r a"):
      print(item.text)