import bs4
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup 

definistionUrl = "https://www.webopedia.com/TERM/A/added_value.html"
difinition_html = uReq(definistionUrl).read()
uReq(definistionUrl).close()
parsedDifinition = soup(difinition_html,"html.parser")
difinition = parsedDifinition.find("div",{"class":"article_related_items"})
# print(difinition)
textReq = ""
for tag in difinition.next_siblings:
	if tag.name == "p":
	    break
	else:
	    textReq = textReq + unicode(tag)
beautifulText = str(soup(textReq, "html.parser").get_text())
withoutSpaces = beautifulText.replace(r","," ")
elemnts = withoutSpaces.splitlines()
print("array: ",elemnts)
print(elemnts[0], elemnts[1])
term_difinition = ""
for elemnt in elemnts:
	print("element: ",elemnt)
	if elemnt != "":
		term_difinition = term_difinition + elemnt
print("result: ",term_difinition)