from bs4 import BeautifulSoup
import requests
url = "https://towardsdatascience.com/the-data-science-climate-change-curriculum-e93b2ba1b969"
response = requests.get(url)
htmlcontent = response.content
# print(htmlcontent)

soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify())

# paras =(soup.findAll('p'))
# print(paras)

# title = soup.title.prettify()
# print(title)

anchors = soup.find_all('a')
# anchors = dict(anchors)


anchorsDict = {element:'Dummy' for element in anchors}
# print ("final list: ", anchorsDict)

# anchorsDict = dict.fromkeys(anchors, i)

# print(anchorsDict)


allLinks = list()

for key, value in anchorsDict.items():
    # allLinks.append ( key.get ( 'href' ) )
    # print(type(key.get('href')))
    if key.get('href')[6] == '/' and key.get('href')[7] == '/':
        allLinks.append(key.get('href'))
    else:

        allLinks.append('https://towardsdatascience.com' + key.get('href'))

for idx,value in enumerate(allLinks):

    print(idx+1,value)
    print()


# print(type(anchors))



