from re import sub


def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    output_sentence = sub(r'[^a-z]','',sentence.lower().strip())
    palindrome = []
    for index in range(len(output_sentence)//2):
        if output_sentence[index] == output_sentence[::-index-1]:
            palindrome.append(True)
        else:
            palindrome.append(False)

    if palindrome.count(False) > 0:
        return False
    else:
        return True


def main():
    # TODO: put your input/output code here
    sentence = input("Please enter your text.\n> ")
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
