test1 = {
    "inputs":{
        "cards":[56,37,78,93,28,90,74],
        "query":78
    },
    "output":2

}

# ordering the cards in descending order to facilitate binary search

cards = test1["inputs"]["cards"]

cards.sort(reverse=True)


query =test1["inputs"]["query"]
output = test1["output"]

# print(cards)


def locate_card():
        f = 0
        l = len(cards)-1
        
        while f<=l:
            mid = (l+f)//2
            midnumber = cards[mid]
            if midnumber == query:
                return mid
            elif midnumber > query:
                 f = mid+1
            elif midnumber < query:
                 l = mid-1
        return -1
            


result = locate_card()
print(result == output)



