with open("voting.in.txt", "r") as votingIn: 
    lines = votingIn.readlines()

firstLineList = lines[0].replace(" ",",").split(",")
secondLineList = lines[1].replace(" ",",").split(",")

totalVoters = int(firstLineList[0])
candidates = int(firstLineList[1])
alreadyVoted = int(firstLineList[2])
yetToVote = totalVoters - alreadyVoted
votedList = [int(i) for i in secondLineList]

resultsList = []
for i in range(0,candidates):
    resultsList.append(0)
for i in votedList:
    resultsList[i-1] += 1

winnerList = []
for i in range(0,candidates):
    if resultsList[i-1] + yetToVote > max(resultsList):
        winnerList.append(1)

with open("voting.out.txt", "w") as votingOut:
    votingOut.write("0" if len(winnerList) == 0 else len(winnerList))