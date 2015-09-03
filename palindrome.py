from re import sub


def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    cleaned_sentence = sub(r'[^a-z]','',sentence.lower().strip())
    sentence_list = list(cleaned_sentence)
    palindrome = []
    for _ in range(len(sentence_list)//2-1):
        if len(sentence_list) >= 2:
            left = sentence_list.pop(0)
            right = sentence_list.pop(-1)
            if left == right or len(sentence_list) == 0:
                palindrome.append(True)
            else:
                palindrome.append(False)
        elif len(sentence_list) == 1:
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


if __name__ == '__main__':
    main()
