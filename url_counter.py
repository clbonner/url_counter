# Given a list of URLs it will return in ascending order a count for each url in the given list.

import re, sys

# a list of URLs to be excluded from the counting process - will match anywhere in the URL
EXCLUSIONS = [
    "google.com",
    "bing.com",
]

# regular expressions for matching urls
EXPRESSIONS = [
    "https://[^,]*",
    "http://[^,]*",
]

COUNT = []

def alreadyCounted(url):
    for item in COUNT:
        if item['url'] == url: return True
    return False

def incrementCount(url):
    for item in COUNT:
        if item['url'] == url: item['count'] = item['count'] + 1
    return

def urlExcluded(url):
    for string in EXCLUSIONS:
        if url.find(string) > 0: return True
    return False

def count_urls():
    # column headers
    outputFile.write("Count,URL\n")

    for regex in EXPRESSIONS:
        URL = re.compile(regex)
        for line in inputFile:
            match = URL.search(line)
            if match:
                if urlExcluded(match.group(0)): continue
                elif alreadyCounted(match.group(0)): incrementCount(match.group(0))
                else: COUNT.append({'url': match.group(0), 'count': 1})

    COUNT.sort(key=lambda item: item['count'])
    for item in COUNT:
        outputFile.write(f"{item['count']},{item['url']}\n")


if (len(sys.argv) != 3):
    print("Usage: url_counter {input file} {output file}")
else:
    input = sys.argv[1]
    output = sys.argv[2]

    try:
        inputFile = open(input)
        outputFile = open(output, "w")
    except:
        print("Error: cannot open file.")
    
    count_urls()
