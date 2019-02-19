# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# Line 4 is importing a scraper wiki for importing webpages
import scraperwiki
import lxml.html
#
print('hello')
# created a variable called html
html = scraperwiki.scrape("http://foo.com")
print(html)
#
# # Find something on the page using css selectors - root is creating a new variable - root is arbitary (html) is the variable just created. 
# #lexml.html is a library created earlier converts webpages to a stucture that can be drilled down best read right to left. 
# #fromstring converts a string of characters into something that can be drilled. You dont need to remember all these details
# # divalign left is looking for a match. we wont see the results unless we add a list
# # the printed lists always produce a list either though there are matches
root = lxml.html.fromstring(html)
print(root.cssselect("div#footer"))
print(root)
listofmatches=root.cssselect('a')
record=()
for match in listofmatches:
  print(match)
  print(lxml.html.tostring(match))
  record['link']=lxml.html.tostring(match)
  print(record)
  scraperwiki.sql.save(unique_keys=['link'], data=record)
# # div is a HTML tag, a is the tag a for anchor, href is an attribute they have values, align is attribute
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
