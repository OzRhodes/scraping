from urllib.request import urlopen

content = urlopen('http://sailingeclipse.com')

print(content.read())

