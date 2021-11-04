<<<<<<< HEAD
class calculate():
    def getdata(self, data):
        self.data = data
    def raid(self):
        data = self.data
        matrix = [[-1] for _ in range(len(data))]*len(data)
        lenth = [-1]*len(data)

        for i in range(len(data)):

            for j in range(i+1,len(data)):
                distance = pow((pow(data[i][0]-data[j][0],2)+pow(data[i][1]-data[j][1],2)),0.5)
                if distance+data[i][2] < data[j][2]:
                    lenth[i] = 0
                    break
                elif:


=======
class calculate():
    def getdata(self, data):
        self.data = data
    def raid(self):
        data = self.data
        matrix = [[-1] for _ in range(len(data))]*len(data)
        lenth = [-1]*len(data)

        for i in range(len(data)):

            for j in range(i+1,len(data)):
                distance = pow((pow(data[i][0]-data[j][0],2)+pow(data[i][1]-data[j][1],2)),0.5)
                if distance+data[i][2] < data[j][2]:
                    lenth[i] = 0
                    break
                elif:


>>>>>>> f0d27928e20afecd1453ff6c377fa43eadf1f97f
