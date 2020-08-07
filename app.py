import nltk
from nltk import FreqDist
from nltk.corpus import gutenberg
from flask import Flask
app = Flask(__name__)

nltk.download('gutenberg')
@app.route("/")
def count_words():
        tokens = gutenberg.words('austen-sense.txt')
        tokens = [word.lower() for word in tokens if word.isalpha()]
        fdist = FreqDist(tokens)
        common = fdist.most_common(500)
        words = []
        for word, frequency in common:
                words.append(word)
        words.sort()
        highCount = common[0][1]
        html = "<html><head><title>Bens Test</title></head><body><h1>WELCOME</h1>"

        for word in words:
                size = str(int(15 + fdist[word] / float(highCount) * 150))
                colour = str(hex(int(0.8 * fdist[word] / float(highCount) * 256**3)))
                colour = colour[-(len(colour) - 2):]
                while len(colour) < 6:
                        colour = "0" + colour
                html = html + "<span style=\"font-size: %s; color: #%s\">%s</span> " % ( size, colour, word)
        html = html + "</body></html>"
        return html

if __name__ == "__main__":
        app.run()