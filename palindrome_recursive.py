from re import sub


def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    output_sentence = sub(r'[^a-z]','',sentence)
    if len(output_sentence) <= 1:
        return True
    elif output_sentence[0] == output_sentence[-1]:
         return is_palindrome(output_sentence[1:-1])
    else:
        return False


def main():
    # TODO: put your input/output code here
    sentence = input("Please enter your text.\n> ").lower().strip()
    if len(sentence) > 0:
        if is_palindrome(sentence):
            print("{} is a palindrome!".format(sentence))
        else:
            print("{} is not a palindrome.".format(sentence))
    else:
        print("Your input did not contain any letters!")
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
