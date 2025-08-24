with open('story.txt','r') as f:
    story = f.read()

words = []
start_of_word = -1 # safe check

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i+1]
        words.append(word)
        start_of_word = -1

print(words)

# make a dictionary to save all the key value paris so that we can use them in our text

answers = {}

for word in words:
    ans = input("Enter a word for "+ word +" : ")
    answers[word]=ans

for word in words:
    story = story.replace(word,answers[word]) # replacing the angle bracket with the answee tht was given to us

print(story)