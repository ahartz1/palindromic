from re import sub


def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    if len(sentence) <= 1:
        return True, "is a palindrome"
    elif sentence[0] == sentence[-1]:
         return is_palindrome(sentence[1:-1])
    else:
        return False, "is not a palindrome"


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
