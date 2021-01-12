def Curr_Price(stock_name,threshold):
    import requests
    from bs4 import BeautifulSoup
    import datetime
    import winsound
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    
    stock_symbol = stock_name
    stock_url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=" + stock_symbol
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                             'like Gecko) '
                             'Chrome/80.0.3987.149 Safari/537.36',
               'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    
    session = requests.Session()
    request = session.get(stock_url, headers=headers, timeout=5)
    cookies = dict(request.cookies)
    response = session.get(stock_url, headers=headers, timeout=5, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id = 'responseDiv').get_text().strip().split(':')
    
    for item in data_array:
        if 'lastPrice' in item:
            index = data_array.index(item)+1
            latest_price = float(data_array[index].split('"')[1].replace(',',''))
            print(datetime.datetime.now(),"-",latest_price)
            while(latest_price < threshold):
                Curr_Price(stock_name,threshold)
                                
            winsound.Beep(frequency, duration)
            return(str(latest_price))
