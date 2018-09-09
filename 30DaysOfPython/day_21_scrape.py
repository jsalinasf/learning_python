import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_loc="
loc = "Newport+Beach,+CA"
current_page = 0

while current_page < 21:
  url = base_url + loc + "&start=" + str(current_page)
  yelp_r = requests.get(url)
  yelp_soup = BeautifulSoup(yelp_r.text, "html.parser")
  file_path = "yelp-2-{loc}.txt".format(loc=loc)
  with open(file_path, "a") as textfile:
    businesses = yelp_soup.findAll("div", {"class": "biz-listing-large"})  
    for biz in businesses:
      title = biz.findAll("a", {"class": "biz-name"})[0].text
      first_line=""
      second_line=""
      try:
        address = biz.findAll("address")[0].contents
        print(address)
        first_line = address[0].strip(" \n\t\r")
        second_line = address[2].strip(" \n\t\r")
        # for item in address:
        #   if "br" in str(item):
        #     second_line += item.getText()
        #   else:
        #     first_line += item.strip(" \n\t\r")
        print(first_line)
        print(second_line)
      except:
        pass
      try:
        phone = biz.findAll("span", {"class": "biz-phone"})[0].text.strip(" \n\t\r")
      except:
        phone = None
      page_line = "{title}\n{address_1}\n{address_2}\n{phone}\n\n".format(
        title=title, 
        address_1=first_line, 
        address_2=second_line, 
        phone=phone)
      textfile.write(page_line)
  
  current_page += 10

# print(yelp_soup.prettify())

# print(yelp_soup.findAll("a"))

# for link in yelp_soup.findAll("a"):
#   print(link)

# print (yelp_soup.findAll("a", {"class": "biz-name"}))

# for name in (yelp_soup.findAll("a", {"class": "biz-name"})):
#   print(name.text)
