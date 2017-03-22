from finviz import getLeftColData, getRightColData

class Manager():
#start off by initalizing by reading the current numbers and putting them into a data strcuture
    ##perferable a priority queue, the higher the change the hgigher the priorityt
    
    def __init__(self):
        print("starting system now")
        self.stock_list = getLeftColData()
        

    def __initalize(self):
        self.stock_list = getLeftColData()
        
    def start(self):
        #multithread the appkication to check for changes in change price
        #or trend and alert on notice
        
        leftData = getLeftColData()
        #returns an array of dictionary holding each stock
        #[ {idx, price, volume, signal}, {}]
        

test = Manager()
test.start()
