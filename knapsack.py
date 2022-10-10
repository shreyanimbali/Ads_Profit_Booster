class Knapsack:
    def __init__(self):
        self.totDur = 0
        self.numAd = 0
        self.eachDur =  []
        self.eachProf = []
        self.grid = []
        self.id = []
        self.adsList = [[0,0,0]]
        self.maxProfit = 0
        self.answer = []

    def setTotalDuration(self,dur):
        self.totDur = dur

    def getTotalDuration(self):
        return self.totDur

    def listAdsDur(self,dur):
        self.eachDur.append(dur)

    def listAdsProf(self,profit):
        self.eachProf.append(profit)
        
    def addAd(self, num, dur, profit):
        self.id.append(num)
        self.eachDur.append(dur)
        self.eachProf.append(profit)
        self.adsList.append([dur,profit,num])
        self.numAd+=1  #incrementing the total number of ads by 1

    def makeGrid(self):
        for i in range(self.numAd+1):
            self.grid.append([])

        #sorting the dictionary in ascending order of ad duration
        self.adsList.sort()

        #filling in values
        for hor in range(0,self.totDur+1):
            self.grid[0].append(0)
        for vert in range(0,self.numAd+1):
            self.grid[vert].append(0)
        for i in range(1,self.numAd+1):
            for w in range(1,self.totDur+1):
                self.grid[i].append(max(self.grid[i-1][w], self.grid[i-1][w-self.adsList[i-1][0]] + self.adsList[i][1]))

        #obtaining max profit
        maxProfit = self.grid[self.numAd+1,self.totDur+1]
        return self.grid

    def zeroOne(self):
        pointer = self.makeGrid()
        i = self.numAd
        w = self.totDur
        while i>0 and w>0:
            pointerUp = self.grid[i-1][w]
            if pointerUp == pointer:
                i-=1
                pointer = pointerUp
            elif pointerUp!=pointer:
                self.answer.append(list.append[i-1][2])
                durLeft = pointer - self.adsList[i-1][0]
                w = durLeft
                i-=1
                pointer = [i][w]

        return self.answer

#testing for setting and getting total duration
obj = Knapsack()
obj.setTotalDuration(8)
print(obj.getTotalDuration())

#testing for adding ads, updating eachDur, eachProf, numAds and adsList
obj.addAd(123, 3, 2)
obj.addAd(767, 4, 3)
obj.addAd(923, 6, 1)
obj.addAd(553, 5, 4)

print(obj.adsList)
print(obj.numAd)
print(obj.eachDur)
print(obj.eachProf)

print(obj.makeGrid())













    

        



