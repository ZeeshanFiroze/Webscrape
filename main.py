import httpx
from selectolax.parser import HTMLParser
url = "https://www.rei.com/c/camping-and-hiking/f/scd-deals"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0"
}
def extract_html(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None

resp=httpx.get(url, headers=headers)
print(resp)
html=HTMLParser(resp.text)
products=html.css("li.VcGDfKKy_dvNbxUqm29K")
for product in products:
    item = {
        "name": extract_html(product, ".Xpx0MUGhB7jSm5UvK2EY"),
        "price": extract_html(product, "span[data-ui=sale-price]"),
    }
    print(item)