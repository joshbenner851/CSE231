import urllib.request

x = urllib.request.urlopen('htpp://www.google.com')

print(x.read())
