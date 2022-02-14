testDictionary = {'a': 1, 'b': 2, 'c': 3}

# Checks if entry is in dictionary


def inDictionary(entry, dictionary):
    if entry in dictionary:
        return True
    else:
        return False


# Prints single entry of dictionary


def printDictionaryEntry(entry, dictionary):
    print(entry + ": " + str(dictionary[entry]))

# Prints all entries of dictionary


def printDictionary(dictionary):
    for entry in dictionary:
        printDictionaryEntry(entry, dictionary)

# Stores a single entry in dictionary


def storeDictionaryEntry(entry, value, dictionary):
    dictionary[entry] = value

# Deletes a single entry from dictionary


def deleteDictionaryEntry(entry, dictionary):
    del dictionary[entry]

# Deletes all entries from dictionary


def deleteDictionary(dictionary):
    dictionary.clear()

# Returns the length of the dictionary


def getDictionaryLength(dictionary):
    return len(dictionary)


# Test dictionary functions
print(inDictionary('a', testDictionary))
print(inDictionary('d', testDictionary))
print("-" * 20)

printDictionaryEntry('a', testDictionary)
storeDictionaryEntry('d', 4, testDictionary)
printDictionaryEntry('d', testDictionary)
printDictionary(testDictionary)
print("-" * 20)
deleteDictionaryEntry('d', testDictionary)
printDictionary(testDictionary)
print("-" * 20)
print(getDictionaryLength(testDictionary))
deleteDictionary(testDictionary)
print(getDictionaryLength(testDictionary))

print("-" * 20)
