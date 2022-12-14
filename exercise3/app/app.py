from nltk.corpus import gutenberg
from flask import Flask
from nltk.corpus import stopwords
import nltk
from nltk import FreqDist

nltk.download('gutenberg')

app = Flask(__name__)


@app.route("/")
def count_words():

    # Grab Sense and Sensibility; tokenize; filter stop words;
    # get frequency distributionpiopkl;,mkjoipi
    tokens = gutenberg.words('austen-sense.txt')
    tokens = [word.lower() for word in tokens if word.isalpha()]
    fdist = FreqDist(tokens)

    common = fdist.most_common(500)

    words = []
    for word, frequency in common:
        words.append(word)
    words.sort()

    highCount = common[0][1]
    html = "<html><head><title>CAB432_exercise_3</title></head><body style = word-wrap:break-word><h1>Exercise 3</h1>"

    for word in words:

        size = str(int(15 + fdist[word] / float(highCount) * 150))
        colour = str(hex(int(0.8 * fdist[word] / float(highCount) * 256**3)))
        colour = colour[-(len(colour) - 2):]
        while len(colour) < 6:
            colour = "0" + colour
        html = html + \
            "<span style=\"font-size: %s; color: #%s\">%s&nbsp</span>" % (
                size, colour, word)
    html = html + "</body></html>"
    return html


if __name__ == "__main__":
    app.run()
