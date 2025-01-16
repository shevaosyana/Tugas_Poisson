from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Fungsi untuk menghitung distribusi Poisson
def poisson_probability(lmbda, k):
    return (math.exp(-lmbda) * lmbda**k) / math.factorial(k)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Mengambil data dari form
    arrival_rate = float(request.form['arrival_rate'])  # rata-rata kedatangan pelanggan per jam
    service_rate = float(request.form['service_rate'])  # rata-rata layanan per jam
    time_period = int(request.form['time_period'])  # periode waktu untuk perhitungan

    # Menghitung probabilitas kedatangan menggunakan Poisson
    arrival_probabilities = [poisson_probability(arrival_rate, i) for i in range(time_period + 1)]

    # Menghitung probabilitas sistem bebas dan penuh (pembacaan antrian)
    system_empty_prob = poisson_probability(arrival_rate, 0)  # sistem kosong
    system_full_prob = poisson_probability(service_rate, time_period)  # sistem penuh

    # Hasil
    results = {
        'arrival_probabilities': [round(prob, 4) for prob in arrival_probabilities],
        'system_empty_prob': round(system_empty_prob, 4),
        'system_full_prob': round(system_full_prob, 4),
    }

    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
