
number = 1
stores = ['a,', 'b', 'c', 'd', 'e']


stores = stores[number:]
last_store = stores[0]
def scrape(store):
    global last_store 
    last_store = store


for i, store in enumerate(stores):
    number = i
    print(last_store)
    scrape(store)
    print(last_store)




#https://www.yelp.com/biz/starbucks-sacramento-32?osq=starbucks&start=70