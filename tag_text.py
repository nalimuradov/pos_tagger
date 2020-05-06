from flask import Flask, request, render_template
import nltk


app = Flask(__name__)


def tag_text(text):
    tokens = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokens)
    return tags


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def display():
    data = request.form.get("my_text_area")
    tagged = tag_text(data)

    words = []
    tags = []
    for i in tagged:
        words.append(i[0])
        tags.append(i[1])

    return render_template('index.html', tagged=tagged)


if __name__ == "__main__":
    app.run(debug=True)
