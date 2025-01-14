from flask import Flask, render_template, request
import math

app = Flask(__name__)

def poisson_probability(lmbda, k):
    return (lmbda ** k * math.exp(-lmbda)) / math.factorial(k)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            home_expectation = float(request.form['home_expectation'])
            away_expectation = float(request.form['away_expectation'])
            home_win = poisson_probability(home_expectation, int(away_expectation))
            away_win = poisson_probability(away_expectation, int(home_expectation))
            draw = poisson_probability(home_expectation, int(home_expectation))
            result = {
                'home_win': round(home_win * 100, 2),
                'away_win': round(away_win * 100, 2),
                'draw': round(draw * 100, 2)
            }
        except ValueError:
            result = {'error': 'Masukkan angka yang valid.'}
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
