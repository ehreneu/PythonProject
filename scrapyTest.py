import requests

# Set the target webpage
url = 'http://172.18.58.238/multi'
r = requests.get(url)

# This will get the full page
print(r.text)

# This will get the status code the return code is 200= ok
print("Status code:")
print("\t*", r.status_code)

#This will just get the headers
h = requests.get(url)
print("Header:")
print("********")
#To print line by line
for x in h.headers:
    print("\t",x,":",h.headers[x])


#This will modify the headers user-agent
headers = {
    'User-Agent': 'Mobile'
}

#Test it on an external site
url2 = 'http://172.18.58.238/headers.php'
rh = requests.get(url2, headers=headers)
print("\t", rh.text)
print("********")



#Webcrawler
import scrapy

class MySpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.238/multi/']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }



