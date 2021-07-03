import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input github user:')
url = 'https://www.github.com/{}/'.format(github_user)
r= requests.get(url)
soup = bs(r.content,'html.parser')
print(soup.prettify)
profile_image = soup.find('img',{'alt' : 'Avatar'})['src']
print(profile_image)