Ask the user to input some text. It can be a phrase, a sentence, or multiple
sentences. After it is entered, your program will let the user know if it is a
palindrome or not. Use "is a palindrome" and "is not a palindrome" in your output
in order for the tests to pass.

Letter casing and punctuation do not matter when testing a palindrome. All of
the following are valid palindromes:

stunt nuts
Lisa Bonet ate no basil.
A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!
Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.


Hard Mode
Make both an iterative and recursive version of your palindrome test function.

Notes
You may want to use the re.sub function to strip out punctuation and spaces.
A regular expression you can use to match all space and punctuation is r'[^A-Za-z]'.
