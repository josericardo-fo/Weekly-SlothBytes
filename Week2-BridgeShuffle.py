def bridge_shuffle(arr1, arr2):
    """
    Given two lists, arr1 and arr2, return a new list that is the result of shuffling the two lists together.
    The shuffle should be done by alternating elements from arr1 and arr2.
    If one list is longer than the other, the remaining elements should all be added to the end of the shuffled list.
    """
    result = []
    for i in range(max(len(arr1), len(arr2))):
        if i < len(arr1):
            result.append(arr1[i])
        if i < len(arr2):
            result.append(arr2[i])

    return result


test_case1 = (["A", "A", "A"], ["B", "B", "B"])
test_case2 = (["C", "C", "C", "C"], ["D"])
test_case3 = ([1, 3, 5, 7], [2, 4, 6])

test_cases = [test_case1, test_case2, test_case3]

for test in test_cases:
    result = bridge_shuffle(*test)
    print(result)
