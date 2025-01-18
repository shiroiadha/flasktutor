from flask import Flask, render_template, request, redirect, url_for, flash
import json, os

app = Flask(__name__)
# app.secret_key = "Pakenanya"
app.secret_key = os.urandom(64)

# Halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Halaman profil
@app.route('/profile')
def profile():
    return render_template('profile/index.html')

# Fungsi untuk menyimpan data ke file JSON
def save_to_json(data, filename='data.json'):
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(data)

    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=4)

# Endpoint untuk menangani data POST
@app.route('/submit', methods=['POST'])
def handle_post():
    # Mengambil data dari form yang dikirim dengan method POST
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Membuat dictionary dengan data yang diterima
    new_data = {
        "name": name,
        "email": email,
        "message": message
    }
    
    # Memanggil fungsi save_to_json
    save_to_json(new_data)

    # Memunculkan popup dengan flash
    flash("Data successfully saved!", "success")
    
    # Redirect ke halaman utama setelah data berhasil disubmit
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)