import string, time, sys

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would', '']


#Print String Slowly
def printslow(theString):
    theString = str(theString)
    for i in list(theString):
        print(i, end="")
        sys.stdout.flush()
        time.sleep(0.003)
    print("\n")


def filter_words(words, filter):
    i = 0
    while i < len(words):
        currentword = words[i]
        if currentword in filter:
            words.remove(currentword)
        else:
            i += 1

    return words


def remove_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct


def normalise_input(user_input):
    # Remove punctuation and convert to lower case
    text = remove_punct(user_input).lower()

    ## REMOVES WHITE SPACES
    while True:
        if len(text) == 0:
            break
        elif text[0] == " ":
            text = text[1:len(text)]
        else:
            break
    while True:
        if len(text) == 0:
            break
        elif text[len(text) - 1] == " ":
            text = text[0:len(text) - 1]
        else:
            break
    text = text.split(" ")
    text = filter_words(text, skip_words)
    if len(text) == 3:
        text = [text[0], text[1] + text[2]]
    if len(text) < 2:
        return ["placeholder", "placeholder"]

    return text
    
