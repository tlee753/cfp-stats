import csv

stats = []

statFile = open("apStats.csv", "a+")

with open("apPoll.csv") as csvFile:
    csvReader = csv.reader(csvFile)
    next(csvReader) # skip csv header
    
    for i in range(1998,2019):
        wins = []
        losses = []
        points = []
        for j in range(25):
            row = next(csvReader)
            if (j < 16):
                wins.append(int(row[4]))
                losses.append(int(row[5]))
                points.append(int(row[6]))

        avgWins = []
        avgLosses = []
        avgPoints = []

        for k in range(2,18,2):
            avgWins.append(round(sum(wins[:k])/k, 2))
            avgLosses.append(round(sum(losses[:k])/k, 2))
            avgPoints.append(round(sum(points[:k])/k, 2))

        statFile.write(str(i) + ",")
        statFile.write(','.join(map(str, avgPoints)))
        statFile.write('\n')

statFile.close()