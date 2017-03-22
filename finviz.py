import requests, re
from bs4 import BeautifulSoup

class FinViz():

    def __init__(self):
        #make the request
        request = requests.get('http://finviz.com/')
        #make the soup
        soup = BeautifulSoup(request.text,'html5lib')
        #soup has been brewed
        self._html = soup
        #self._html = BeautifulSoup(requests.get('http://finviz.com/').text,'html5lib')
        self._data = list()
        
    def refresh(self):
        """
        This Method is called to make another poll to finviz to
        update the current objects data, also called (reinitalize)
        -Precondition: None
        -Postcondition:Object's scraped data is refreshed as of currently called
        """
        self.__reinitalize__()
    def __reinitalize__(self):
        #this gets the objects reinitze with new data
        self._html = BeautifulSoup(requests.get('http://finviz.com/').text,'html5lib')
    
    def getLeftColumn(self):
        """ Gets the left column displaying Top gainers, New highes, OverBought, Unusual Volume Upgrades,
        Earnings before, and insider buying signals as well as their respective stock indexes 
        Stock Index
        Current Price
        Percent Change
        Volume
        Signal"""
        data = self.__getMainColumnData__(0)
        data = data.findChild()
        data = list(data.children)
        result = list()
        for idx in data:
            try:
                #print(item.getText())
                #populate the dictionary with respective data
                result.append(__parseText__(idx.getText()))

            except:
                pass

        return result        
    def getRightColumn(self):
        """ Gets the left column displaying Top gainers, New highes, OverBought, Unusual Volume Upgrades,
        Earnings before, and insider buying signals as well as their respective stock indexes 
        Stock Index
        Current Price
        Percent Change
        Volume
        Signal"""
        data = self.__getMainColumnData__(1)
        data = data.findChild()
        data = list(data.children)
        result = list()
        for idx in data:
            try:
                #print(item.getText())
                #populate the dictionary with respective data
                result.append(self.__parseText__(idx.getText()))

            except:
                pass

        return result        
   

    def __getMainColumnData__(self,column):
        """
        Parameters : Takes Left or Right
            Left will be 0 right will be 1

        This methid get's the two main left and right columns
        from finviz.com, the columns shown on the left are:
        Top Gainers
        New high
        Overbought
        Unusual Volume
        Upgrades
        Earnings Before

        The column on the right are
        Top Losers
        New Low
        Oversold
        Most Volitile
        Most Active
        Downgrades
        Earnings After
        Insider Selling
        """
        #make the https requests
        #req = requests.get('http://finviz.com/')
        #brew the soup >:)
        #soup  = BeautifulSoup(req.text,'html5lib')
        #find the repsective elements we are looking for
        #this will return a result set object for docs: look at website
        #returns all matching elements
        #searchResult = soup.findAll('table',{'class':'t-home-table'})
        searchResult = self._html.findAll('table', {'class':'t-home-table'})
        
        # we just want the first and second matches

        return searchResult[column]


    def getRightColData():
        """
        Postcondition:
            Returns a Object of type Dictionary
            with price, index, volume and signal respectivly
        """
        data = getMainColumnData(1)
        data = data.findChild()
        data = list(data.children)
        result = list()
        for idx in data:
            try:

                #populate the dictionary with respective data
                result = __parseText__(idx.getText())
                #need exection for stringObject

            except:
                pass
        return result
    def getLeftColData():
        """
        Postcondition:
            Returns a Object of type Dictionary
            with price, index, volume and signal respectivly
        """
        data = getMainColumnData(0)
        data = data.findChild()
        data = list(data.children)
        result = list()
        for idx in data:
            try:
                #print(item.getText())
                #populate the dictionary with respective data
                result.append(__parseText__(idx.getText()))

            except:
                pass

        return result

    def marketStatus():
        """

        This Method check wether the market is up or down.
        Precondition: None
        Postcondition: Returns String 'Up' or 'Down' for the current requested
        time.

        """


    def getMainLeftColumn():
        q = requests.get('http://finviz.com/')
        #make the soup
        soup = BeautifulSoup(q.text,'html5lib')
        #get the left column table element
        q = soup.find('table',{'class':'t-home-table'})
        q = q.findChild()
        p = list(q.children)

        for item in p:
            try:
                #print(item.getText())
                #populate the dictionary with respective data
                result = __parseText__(item.getText())
                print("%s %s %s %s %s" %(result['index'],
                                         result['price'],
                                         result['change'],
                                         result['signal'],
                                         result['volume'])
                      )

            except:
                pass

    def __parseText__(self, text):
        #resultSet = dict()
        #idx = text[:4]
        #use regex for faster parsing of text, searching
        #for numbers and words, better and faster.

        ##define regEx pattern
        #"find all alpha upper and lower words
        #+ one and unlimited timees
        #match words who may or may not have spcaes betweent hem and
        #are mixed caes zero to unliited times
        regExText = '[A-Z a-z]+'
        #match a number with at least 1 to unlimited length
        ##the number must have a period and 1 through 2 numbers after it
        #match fully if there is a '+' OR '-' ZERO or 1 times
        regExDigit = '(\+|-?\d+.\d{1,2})'
        #regExDigit = '(\d+.\d{1,2})'
        listText = re.findall(regExText, text)
        listDigit = re.findall(regExDigit, text)
        resultSet = {'index':listText[0],
                     'price':listDigit[0],
                     'change':listDigit[1],
                     'volume':listDigit[2],
                     'signal':listText[1]}
        ##return the resulting dictionary
        return resultSet
    
    #Testing functions
    def displayRightCol():
        #returns a tag element object
        data = getMainColumnData(1)
        data = data.findChild()
        data = list(data.children)

        for idx in data:
            try:
                #print(item.getText())
                #populate the dictionary with respective data
                result = __parseText__(idx.getText())
                print("%s %s %s %s %s" %(result['index'],
                                         result['price'],
                                         result['change'],
                                         result['signal'],
                                         result['volume'])
                      )

            except:
                pass
    def displayLeftCol():
        #returns a tag element object
        data = getMainColumnData(0)
        data = data.findChild()
        data = list(data.children)

        for idx in data:
            try:
                #print(item.getText())
                #populate the dictionary with respective data
                result = __parseText__(idx.getText())
                print("%s %s %s %s %s" %(result['index'],
                                         result['price'],
                                         result['change'],
                                         result['signal'],
                                         result['volume'])
                      )

            except:
                pass
    



def test():
    print("testing now")
    testObject = FinViz()
    x = testObject.getRightColumn()
    print(len(x))
    for i in x:
        print("%s  %s  %s  %s" % (i['index'],i['price'],i['change'], i['volume']))
        


    #print("get left column")
    #displayLeftCol()
    #print('display rigfht')
    #displayRightCol()


test()
if "__name__" == "__main__":
    test()
