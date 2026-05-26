# Question 2

def clean_text(text):
    # convert to lowercase and remove punctuations
    text = text.lower()
    punctuation = ".,!?;:'\"()-"
    cleaned = ""

    for char in text:
        if char not in punctuation:
            cleaned += char

    return cleaned


# test sentences
sentence1 = "I am VERY happy today!"
sentence2 = "Wow... this is stressful."
sentence3 = "Python is FUN!!!"
sentence4 = "Hello Everyone!"
print("\n->checking for Q2<-")
print(clean_text(sentence1))
print(clean_text(sentence2))
print(clean_text(sentence3))
print(clean_text(sentence4))


# QUESTION 3

def count_words(text):

    # clean the text and split it
    text = clean_text(text)
    words = text.split()
    wordcount = {}

    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    return wordcount


# testing count_words()
print("\n->Checking for Q3<-")

text = "Happy happy sad excited happy funny hello sad"
print(count_words(text))


# QUESTION 4 - Mood Words


mood_words = ["happy", "nervous", "sad", "stressed", "hyped", "calm", "excited", "angry", "tired", "worried"]


def find_mood_words(text):

    # clean text and split it
    text = clean_text(text)
    words = text.split()

    found = []

    for word in words:
        if word in mood_words:
            found.append(word)

    return found


# testing mood words
print("\n->checking for Q4<-")

test = "I am happy but also stressed and nervous."
print(find_mood_words(test))


# QUESTION 5


def top_5_words(text):

    frequencies = count_words(text)
    word_list = list(frequencies.items())

    # sort by frequency (highest first)
    word_list.sort(key=lambda x: x[1], reverse=True)

    top_five = word_list[:5]

    return top_five


# testing top_5_words()
print("\n->Checking for Q5<-")

top_test = """ happy sad happy happy sad excited excited python hello python fun fun fun """

print(top_5_words(top_test))


# QUESTION 6 - Read from .txt file

print("\n Reading sentences.txt")

# open the text file
with open("sentences.txt", "r") as file:

    # read all lines
    sentences = file.readlines()

    # analyze each sentence
    for number, sentence in enumerate(sentences, start=1):

        print("\nSentence", number)

        # original sentence
        print("Original:", sentence.strip())

        # cleaned sentence
        cleaned = clean_text(sentence)
        print("Cleaned:", cleaned)

        # mood words found
        moods = find_mood_words(sentence)
        print("Mood Words Found:", moods)

        # top 5 words
        top_words = top_5_words(sentence)
        print("Top 5 Words:", top_words)