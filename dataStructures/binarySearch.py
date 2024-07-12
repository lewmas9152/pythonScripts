test1 = {
        "inputs": {
            "cards": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            "query": 7
        },
        "output": 3
    }

test2 = {
    "inputs": {
        "cards": [10, 9, 7, 6, 5, 4, 3, 2, 1],
        "query": 7
    },
    "output": 2
}

test3 = {
    "inputs": {
        "cards": [10, 9, 7, 6, 5, 4, 3, 2, 1],
        "query": 2
    },
    "output": 7
}

test4 = {
    "inputs": {
        "cards": [10, 9, 7, 6, 5, 4, 3, 2, 1],
        "query": 10
    },
    "output": 0
}

test5 = {
    "inputs": {
        "cards": [10, 9, 7, 6, 5, 4, 3, 2, 1],
        "query": 1
    },
    "output": 8
}

test6 = {
    "inputs": {
        "cards": [10, 9, 7, 6, 5, 4, 3, 2, 1],
        "query": 8
    },
    "output": -1
}

test7 = {
    "inputs": {
        "cards": [10, 9, 7, 7, 6, 5, 4, 3, 2, 1],
        "query": 7
    },
    "output": 2
}

test8 = {
    "inputs": {
        "cards": [10],
        "query": 10
    },
    "output": 0
}

test9 = {
    "inputs": {
        "cards": [10,7,7,7,7,6,5,5,2],
        "query": 7
    },
    "output": 0
}


testCases = [test1, test2, test3, test4, test5, test6, test7, test8, test9]

def locate_card(cards,query):
    f = 0
    l = len(cards)-1

    print(f"Test:{i}")

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


for i, tests in enumerate(testCases):
    cards = tests["inputs"]["cards"]
    query = tests["inputs"]["query"]
    output = tests["output"]

  
    result = locate_card(cards,query)
    print(result == output)



