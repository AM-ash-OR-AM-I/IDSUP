# Read a lists named StringList1 containing strings from the key board. Generate a string MStringList1 that contains
# all items of StringList1 that are repeated twice or more number of times and print this list. By observing the
# outcome of MStringList1 perform the following tasks: a. Check wather an item of MStringList1 occurs even number of
# times or odd number of times in StringList1. b. Remove the i th (i ≥ 2) occurrence of a given word in a StringList1.


def main():
    string_list1 = input("Enter a list of strings: ").split()
    m_string_list1 = [
        string for string in set(string_list1) if string_list1.count(string) >= 2
    ]
    print(f"MStringList1: {m_string_list1}")

    for string in m_string_list1:
        index = string_list1.index(string)
        # Check if the string occurs more than once, remove i>=2 occurrence
        indexes_to_remove = []
        if string_list1.count(string) > 1:
            remove_index = string_list1.index(string, index + 1)
            indexes_to_remove.append(remove_index)

        for i in indexes_to_remove[::-1]:
            string_list1.pop(i)

    print(f"StringList1 after removing all duplicates of each word: {string_list1}")


main()
