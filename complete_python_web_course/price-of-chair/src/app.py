
import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.com/dp/B015TJD0Y4/ref=ods_gw_b_h1_ha_justask_white?\
pf_rd_r=H2BXX9PT1DKKK7K99P5Y&pf_rd_p=31caa380-aa91-4b5e-aa39-173070b043c0")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_ourprice", "class": "a-size-medium a-color-price"})
price = element.text.strip() # $49.99
price = price[1::] # Slice the price to remove the Dollar ($) Sign -> 49.99
price = float(price)
print("El precio actual es: ${}".format(price))
presupuesto = 49.99
if price < presupuesto:
    print("Ha bajado el precio!")
elif price == presupuesto:
    print("Se mantiene el precio")
else:
    print("Ha subido el precio!")

# Inspect Element - Web Browser
# <span id="priceblock_ourprice" class="a-size-medium a-color-price">$49.99</span>
