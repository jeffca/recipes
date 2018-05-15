from lxml import html
import requests
page = requests.get('http://espn.com')
tree = html.fromstring(page.content)

results = tree.xpath("//ul[@class='headlineStack__list']/li/a/text()")
print results
