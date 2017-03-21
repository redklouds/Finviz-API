import requests, re
from bs4 import BeautifulSoup

def getMainPageData():
        """
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
        regExText = '[A-Za-z]+'
        #match a number with at least 1 to unlimited length
        ##the number must have a period and 1 through 2 numbers after it
        regExDigit = '(\d+.\d{1,2})'
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


if "__name__" == "__main__":
	test()
