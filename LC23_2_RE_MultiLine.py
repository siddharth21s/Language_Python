#!/usr/bin/python
import re
def main():
    fd = open("test1.txt")
    data = fd.read()
    print (data)
    for x in re.finditer("^a", data, re.MULTILINE | re.IGNORECASE):
        print (x.start(), x.end(), data[x.start():x.end()])
if __name__ == "__main__":
    main()
