import bs4, requests, os, sys


class bcolors:
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'


def proxy_lister():
    global table
    pageLink = "https://free-proxy-list.net/"
    try:
        page = requests.get(pageLink)
        findsrc = bs4.BeautifulSoup(page.content, "html.parser")
        table = findsrc.find_all('table', attrs={'id': 'proxylisttable'}) and findsrc.table.find('tbody')
    except Exception as err:
        print("Proxies can't get free-proxylist. Try again.  ", err)

    data = []
    counter = 0
    for row in table:
        rows = row.find_all('td')
        rows = [x.text.strip() for x in rows]
        data.append([x for x in rows if x])
        del data[counter][2:8]
        data[counter] = ['{}:{}'.format(data[counter][0], data[counter][1])]
        counter += 1
    try:
        fileName = "proxy.txt"
        with open(fileName, "w+") as file:
            for i in data:
                i = ''.join(i)
                file.writelines(str(i) + "\n")
        print("{1}Proxies saved {3} {2}{0}{3}".format(fileName, bcolors.CVIOLET, bcolors.CBEIGE, bcolors.CRED))

    except Exception as err:
        print(err)
    return data


