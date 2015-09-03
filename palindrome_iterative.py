def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    palendrome = []
    for index in range(len(sentence)//2):
        if sentence[index] == sentence[::-index-1]:
            palendrome.append(True)
        else:
            palendrome.append(False)

    if palendrome.count(False) > 0:
        return False, "is not a palindrome"
    else:
        return True, "is a palindrome"


def main():
    # TODO: put your input/output code here
    sentence = input("Please enter your text.\n> ").lower().strip()
    output_sentence = sub(r'[^A-Za-z]','',sentence)
    if len(output_sentence) > 0:
        is_palindrome(list(output_sentence))
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
