def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    index = 0
    palendrome = []
    for index in range(len(sentence)//2):
        if list[index] == list[-index - 1]:
            palendrome.append(True)
        else:
            palendrom.append(False)

    if palendrome.count(False) > 0:
        return False
    else:
        return True


def main():
    # TODO: put your input/output code here
    sentence = input("Please enter your text.\n> ").lower()
    # I am looking to strip all extraneous characters; make sure has characters
    sentence_list = []
    for char in sentence:
        if char in "abcdefghijklmnopqrstuvwxyz":
            sentence_list.append(char)

    if len(sentence_list) > 0:
        is_palindrome(''.join(sentence_list))
    else:
        print("You did not enter any alphabetical characters.")
        main()

if __name__ == '__main__':
    main()


'''
Recursive idea:
1. Lowercase and take only letters before recursive loop
2. Base case: if len is 1 or 0, return "is a palendrome"
3. Take the outer letters off; if they are equal, recurse.

Iterative idea:
1. Lowercase and take only letters

'''
