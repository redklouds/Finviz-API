import requests, re
from bs4 import BeautifulSoup

##############################################################
# File Name: finviz.pu
# Author: Danny Ly | RedKlouds
# Created: 3/20/2017
##############################################################
#
#   Description: This is a program used
#   to get the data from the website finfiz.com
#   PRECONDITIONS:
#       -> Call to the object's methods
#           ->getLeftColumn, which has daily trends of
#               ->Top Gainers | New High | Overbought
#               | Unusual Volumn | Upgrades | Earnings Before
#               | Insider Buying
#           ->getRigthColumn, which has a daily red of:
#               -> Top Losers | New Low | Oversold |
#               Most Volatile | Most Active | Downgrades
#               | Earnings After | Insider Selling
#        -> USEAGE:
#            -> calling getTrends(), returns a dictionary with 
#              {'left_column','right_column'} data trends 
#   POSTCONDITIONS:
#       -> Returns a dicitonary with the above mentioned keys
#   ASSUMPTIONS:
#       -> Requests has been updated and installed
#       -> BeautifulSoup4 has been installed
#
##############################################################
class FinViz:

    def __init__(self):
        """
        Function Name: Default Constructor
        PRECONDITIONS: None
        POSTCONDITIONS: 
            ->Initializes the object data at the current time
        ASSUMPTIONS: None
        """
        #make the request
        request = requests.get('http://finviz.com/')
        #maxe the soup
        soup = BeautifulSoup(request.text,'html5lib')
        #soup has been brewed
        self._html = soup
        #self._html = BeautifulSoup(requests.get('http://finviz.com/').text,'html5lib')
        self._data = list()


    def refresh(self):
        """
            Function Name: refresh
            Descriptions:
                -> Polls the webservice for new/updated data
            PRECONDITIONS: None
            POSTCONDITIONS: 
                -> Object reinitialized with new data
            ASSUMPTIONS: None
        """        
        self.__reinitalize__()
    
    def _reinitialize(self):
        """
            Function Name: (Helper) _reinitialize 
            Description:
                -> calls another get requsests to poll refreshed data manually
            PRECONDITIONS: None
            POSTCONDITIONS: 
                -> Refreshes data
            ASSUMPTIONS: None
        """        
        r = requests.get('http://finviz.com')
        self._html = BeautifulSoup(r.text)

    def _parseColumnData(self, data):
        """
            Function Name: 
            PRECONDITIONS:
            POSTCONDITIONS:
            ASSUMPTIONS:
        """        
        ret_data = data.findChild()
        ret_data = list(ret_data.children)
        result = list()
        for idx in ret_data:
            try:
                #parse the given data, into 
                result.append(self._parseText(idx.getText()))                
            except:
                #None Type, scrapping None Object, skip.
                pass
        return result  

    def _parseText(self, text):
        """
            Function Name: 
            PRECONDITIONS:
            POSTCONDITIONS:
            ASSUMPTIONS:
        """        
        #use regex for faster parsing of text, searching
        #for numbers and words, better and faster.

        #define regEx pattern
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
        resultSet = {
                     'index':listText[0],
                     'price':listDigit[0],
                     'change':listDigit[1],
                     'volume':listDigit[2],
                     'signal':listText[1]
                     }
        #return the resulting dictionary
        return resultSet
    
    def getLeftColumn(self):
        """
            Function Name: getLeftColumn
            Description:
                -> get get's the raw data in the left column of the website
            PRECONDITIONS: None
            POSTCONDITIONS:
                ->returns a dictionary containing all the parsed data
                -> in the form:
                    Stock Index
                    Current Price
                    Percent Change
                    Volume
                    Signal
            ASSUMPTIONS: None
        """        
        data = self._getMainColumnData(0)
        a = self._parseColumnData(data)
        return a
        
    def getRightColumn(self):
        """
            Function Name: getLeftColumn
            Description:
                -> get get's the raw data in the right column of the website
            PRECONDITIONS: None
            POSTCONDITIONS:
                ->returns a dictionary containing all the parsed data
                -> in the form:
                    Earnings before
                    Stock Index
                    Current Price
                    Percent Change
                    Volume Signal
            ASSUMPTIONS: None
        """  
        data = self._getMainColumnData(1)
        a = self._parseColumnData(data)
        return a

    def _getMainColumnData(self,column):
        """
            Function Name: _getMainColumnData
            Description:
               -> our switch helper function depending on which 
               parameter we get, this function returns the respective data set
               pertaining to that column
               
            PRECONDITIONS: Integer 1 or 0( left will be 0, 1 will be right)
            POSTCONDITIONS:
                Left:
                Top Gainers
                New high
                Overbought
                Unusual Volume
                Upgrades
                Earnings Before
        
                The column on the right are:
                Top Losers
                New Low
                Oversold
                Most Volitile
                Most Active
                Downgrades
                Earnings After
                Insider Selling
            ASSUMPTIONS: None
        """        
        #scrape the specific elements
        searchResult = self._html.findAll('table', {'class':'t-home-table'})
        
        # we just want the first or second matches
        return searchResult[column]
        
    def marketStatus():
        """
            TODO: get Market status |Positive|Negative
            Function Name: 
            PRECONDITIONS:
            POSTCONDITIONS:
            ASSUMPTIONS:
        """        
        
    def getTrends(self):
        left_col = self.getLeftColumn()
        right_col = self.getRightColumn()
        
        combined_dict = list()
  
        for i in left_col:
            combined_dict.append(i)
        for i in right_col:
            combined_dict.append(i)
            
        #print(combined_dict)
        #return_dict = {"right_column": right_col, "left_column":left_col}
        return combined_dict


   
def test():
    print("testing now")
    testObject = FinViz()

    data = testObject.getTrends()
    for i in data:
        print(i)
    

if __name__ == "__main__":
    test()
