import requests, re
from bs4 import BeautifulSoup

def getMainColumnData(column):
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
        req = requests.get('http://finviz.com/')
        #brew the soup >:)
        soup  = BeautifulSoup(req.text,'html5lib')
        #find the repsective elements we are looking for
        #this will return a result set object for docs: look at website
        #returns all matching elements
        searchResult = soup.findAll('table',{'class':'t-home-table'})
        # we just want the first and second matches
        return searchResult[column]

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

def displayRightCol():
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

def __parseText__(text):
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
        

        
def test():
        print("hello world")
        getMainLeftColumn()

test()
if "__name__" == "__main__":
	test()
