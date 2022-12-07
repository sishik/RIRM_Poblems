import requests
import re
from bs4 import BeautifulSoup
url = "https://ful.io/"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.findall('a',class_="flex"))
anchors = soup.find_all('a')
lst=[]
Contact=[]
Social_links=[]
Email=[]
re_email='([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
re_phone= '^tel:(\+?\d{0,2}\-?\s?)?\(?\d{3,4}\)?[\s.-]?\d{3}[\s.-]?\d{3,4}$'
for i in anchors:
  lst.append(i['href'])
#print(lst)
for ele in lst:
  if re.search(re_phone, ele):
    Contact.append(ele)
  if ele.startswith('https://www.facebook') or ele.startswith('https://www.linkedin'):
    Social_links.append(ele)
  if re.search(re_email,ele):
    Email.append(ele)

print('Social Links-',end='\n')
for ele in Social_links:
  print(ele)
print('Email',end='\n')
for ele in Email:
  print(ele)
print('Contact',end='\n')
for ele in Contact:
  print(ele)

#print(soup.prettify())	# to print html in tree structure