import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def main():
    #page, client to request download of page, parse that page in its entirety to a var, close client
    my_url = 'https://www.newegg.com/DailyDeal.aspx?name=DailyDeal&IsNodeId=1&N=700000003'
    uClient = uReq(my_url)
    raw_html = uClient.read()
    uClient.close()

    #parse html, establish 'container' we want information out of from the site.
    souped_page = soup(raw_html, "html.parser")
    containers = souped_page.findAll("div",{"class":"item-container"})

    filename = "NewEgg_Daily_Deals.csv"
    f = open(filename, "w")
    headers = "brand, prod_title, shipping\n"
    f.write(headers)

    #our loop to obtain/store/format 3 desired fields from within the container
    for container in containers:
        brand = container.div.div.a.img["title"]

        title_container = container.findAll("a", {"class":"item-title"})

        prod_title = title_container[0].text

        shipping_container = container.findAll("li", {"class":"price-ship"})

        shipping = shipping_container[0].text.strip()

        f.write(brand + "," + prod_title.replace(",","|")+","+shipping+"\n")

    f.close()

main()
