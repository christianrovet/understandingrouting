from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "dojo"

@app.route('/say/<word>')
def say(word):
    return "Hi " + word + "!"

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    arr = []
    for i in range(int(num)):
        arr.append(word)
    return ' '.join(map(str,arr))



if __name__ == "__main__":
    app.run(debug=True)
