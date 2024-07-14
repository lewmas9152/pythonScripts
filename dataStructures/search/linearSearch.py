def locate_card(cards, query):
    for i, card in enumerate(cards):
        if card == query:
            return i
    return -1



# Function to run through all the test cases
def run_tests():
    tests = []

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

    testCases = [test1, test2, test3, test4, test5, test6, test7, test8]

    all_tests_passed = True

    for i, test in enumerate(testCases):
        result = locate_card(test["inputs"]["cards"], test["inputs"]["query"])
        if result != test["output"]:
            print(f"Test {i + 1} failed: expected {test['output']} but got {result}")
            all_tests_passed = False
        else:
            print(f"Test {i + 1} passed")

    if all_tests_passed:
        print("All tests passed!")
    else:
        print("Some tests failed.")

# Run the tests
run_tests()
