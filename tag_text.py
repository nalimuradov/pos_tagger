from flask import Flask, request, render_template
import nltk
from gensim.models import Word2Vec

app = Flask(__name__)


# tags input string by corresponding part-of-speech
def tag_text(text):
    tokens = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokens)
    return tags


# removes stopwords ('a', 'the', ...) from given string
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    return filtered_sentence


# test word vectorizer
def run_word2vec():
    with open('data.txt') as json_file:
        data = json.load(json_file)

    sentences = []
    for video in data:
        sentences.append(data[video][0])

    # print(sentences)
    word2vec = Word2Vec(sentences)
    vocabulary = word2vec.wv.vocab
    print(word2vec.wv['artificial'])


# default route, shown on load
@app.route('/')
def home():
    return render_template('index.html')


# shown on form submission
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


