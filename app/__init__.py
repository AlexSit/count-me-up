from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    votesCount = 10000000
    scores = [5,10,20,25,40]

    result = ""

    i = 1
    for score in scores:
        result += "candidate {}: {}\n".format(i, votesCount / 100 * score)
        i += 1
    return result

if __name__ == '__main__':
    app.run()