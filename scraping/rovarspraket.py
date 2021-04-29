#!/usr/bin/env python3 
# Lägg ett o efter varje konsonant och sedan samma konsonant igen
# t.ex. Karl = Kokarorlol
# input: a string 
# --------------
# output: a modified string 

def rovarSpraket(aName):
    vowels = ['a', 'o', 'u', 'å', 'e', 'i', 'y', 'ä', 'ö']
    rovarName = ''

    for char in aName:
        if char in vowels:
            rovarName += char
        else:
            rovarName = rovarName + char + 'o' + char.lower()

    return rovarName

def main():
    rovarNamn = rovarSpraket('Karl')
    print(rovarNamn)


if __name__ == "__main__":
    main()