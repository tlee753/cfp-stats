from lxml import html
import requests
import sys

year = sys.argv[1]
link = sys.argv[2]
# link = "http://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=821#.XdXT_ldKiUk"
page = requests.get(link)
tree = html.fromstring(page.text)

csvFile = open("apPoll.csv", "a+")

for i in range(2, 27):
    rankDOM = "//table[3]/tr[%d]/td[1]/strong/text()" % i
    rank = tree.xpath(rankDOM)

    teamDOM = "//table[3]/tr[%d]/td[3]/a/text()" % i
    team = tree.xpath(teamDOM)

    confDOM = "//table[3]/tr[%d]/td[4]/abbr/text()" % i
    conf = tree.xpath(confDOM)
    if len(conf) == 0:
        confDOM = "//table[3]/tr[%d]/td[4]/text()" % i
        conf = tree.xpath(confDOM)

    recordDOM = "//table[3]/tr[%d]/td[5]/text()" % i
    record = tree.xpath(recordDOM)
    wins, losses = record[0].split("-")

    pointsDOM = "//table[3]/tr[%d]/td[6]/text()" % i
    points = tree.xpath(pointsDOM)

    bcsDOM = "//table[3]/tr[%d]/td[9]/text()" % i
    bcs = tree.xpath(bcsDOM)
    # bcs = ["NR"]

    l = [year, rank[0], team[0], conf[0], wins, losses, points[0], bcs[0]]

    csvFile.write(','.join(l))
    csvFile.write('\n')

csvFile.close()