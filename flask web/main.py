from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    web_title = "Halaman Utama"
    return render_template('home.html', web_title=web_title)

@app.route("/about")
def about():
    web_title = "Halaman About"
    return render_template('about.html', web_title=web_title)

@app.route("/usia", methods=['GET', 'POST'])
def cek_usia():
    if request.method == 'POST':
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - tahun_lahir
        return render_template('cek_usia.html', usia=usia)
    return render_template('cek_usia.html', usia=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2000)