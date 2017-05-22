# Finviz-API
Finviz API implmented using BeautifulSoup, web scrapping.

Feature | Description|
------- | -----------
Trending Tickers | Polls for the current trending stocks

## example code/Usage

```python
 from finviz import Finviz
 finviz_object = Finviz()
 
 finviz_trending = finviz_Object.getTrends()
 
```
after execution above returns a Dictionary of the trending stocks
here are the keys you can access
 ```
     #look at he first element in out trending data
     data = finviz_trending[0]
     #{'index': 'QHC', 'change': '38.19', 'signal': 'Top Gainers', 'volume': '3593933', 'price': '3.98'}
     #get the signal
     data['signal']
     # Top Gainers
 ```
 Output
 ```
 >>>
 SBGL  5.51  -32.23  10678009 Top Losers
FL  58.72  -16.65  16888155 Top Losers
JMU  1.83  -14.08  21538 Top Losers
HPJ  4.45  -10.10  940151 Top Losers
DFFN  2.88  -9.97  106158 Top Losers
RCON  1.12  -9.68  112929 Top Losers
SBGL  5.51  -32.23  10678009 New Low
MARA  0.27  -10.00  1529647 New Low
JMU  1.83  -14.08  21538 New Low
PMTS  2.25  -6.25  634617 New Low
FENX  0.76  -4.08  124238 Oversold
ASH  65.01  1.39  1496191 Oversold
INSG  1.14  10.68  1364408 Most Volatile
QHC  3.98  38.19  3593933 Most Volatile
VXX  14.64  -6.99  114458174 Most Active
SPY  238.31  0.65  111672408 Most Active
BLMN  20.12  -2.28  1809280 Downgrades
BKJ  16.25  -0.20  6052 Earnings After
AWK  75.86  0.81  561206 Insider Selling
 ```

