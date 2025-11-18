from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html', active_tab='home')

@app.route('/books')
def books():
    return render_template('books.html', active_tab='books')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', active_tab='portfolio')

if __name__ == '__main__':
    app.run(debug=True)
