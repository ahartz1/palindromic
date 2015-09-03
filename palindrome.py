def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    if sentence == sentence[::-1]:
        return True, "is a palindrome"
    else:
        return False, "is not a palindrome"


def main():
    # TODO: put your input/output code here
    sentence = list(input("Please enter your text.\n> "))
    sentence_list = []
    for char in sentence:
        if str(char).lower() in "abcdefghijklmnopqrstuvwxyz":
            sentence_list.append(char)

    if len(sentence_list) > 0:
        is_palindrome(''.join(sentence_list))
    else:
        return False, "is not a palindrome"


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
