import requests
from bs4 import BeautifulSoup as bs
import os

#providing the url
url = "https://www.pexels.com/search/parrots/"

#parsing the page
page = requests.get(url)
soup = bs(page.text,'html.parser')

#finding all image which is in <img> tag html
image_tags = soup.findAll('img')

#creating a folder
if not os.path.exists('parrots'):
    os.makedirs('parrots')
#entering the folder
os.chdir('parrots')

#keeping track of number of images
x=0

#getting the images
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('parrot-' + str(x) + '.jpg','wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
