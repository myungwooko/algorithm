from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json
import time


def getMovieTitles(substr):
    url = "https://jsonmock.hackerrank.com/api/movies/search/?Title=" + substr

    titles = []
    page = 1
    ids = []

    while True:
        res = urlopen(url)
        html = res.read()
        page_data = json.loads(html)
        movies = page_data["data"]
        if not movies:
            break

        for movie in movies:
            if movie["imdbID"] in ids:
                break
            titles.append(movie["Title"])
            ids.append(movie["imdbID"])

        if page == 1:
            page += 1
            url += '&page=' + str(page)
        else:
            page += 1
            url = url[:-1]
            url += str(page)

    titles.sort()

    return titles


getMovieTitles('spiderman')


def funWithAnagrams(s):
    # Write your code here
    result = []
    indexs = []

    for i, v in enumerate(s):
        v = list(v)
        v.sort()
        sorted = ''.join(v)

        if not result:
            result.append(sorted)
            indexs.append(i)
        else:
            if sorted not in result:
                result.append(sorted)
                indexs.append(i)
    for i, v in enumerate(result):
        result[i] = s[i]
    return result


test = ['code', 'aaagmnrs', 'anagrams', 'doce']

test = funWithAnagrams(test)
print(1, test)
