import os

while True:
    search = input("google serch: ")
    os.startfile("https://www.google.com/search?q=" + search)
    print("")