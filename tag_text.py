from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/', methods=['POST'])
def display():
    data = [x for x in request.form.values()]
    print(data)

    return render_template('index.html', return_text='nariman')


if __name__ == "__main__":
    app.run(debug=True)
