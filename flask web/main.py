from datetime import datetime
import markdown  # <-- Tambahkan import ini
from flask import Flask, render_template, request
from groq import Groq

app = Flask(__name__)

AI_KEY = ""
client = Groq(api_key=AI_KEY)


def ai_call(year):
  try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": (
                    "berikan saya satu fakta menarik seputar teknologi pada"
                    f" tahun {year}"
                ),
            }
        ],
        model="qwen/qwen3.8-27b",  # <-- Ubah menjadi model ini
        stream=False,
    )
    ai_output = chat_completion.choices[0].message.content
    html_output = markdown.markdown(ai_output)
    return html_output
  except Exception as e:
    return f"Maaf fitur AI saat ini tidak bisa digunakan. (Error: {e})"

@app.route("/")
def main():
  return render_template("index.html")


@app.route("/usia", methods=["GET", "POST"])
def cek_usia():
  if request.method == "POST":
    tahun_lahir = int(request.form["tahun_lahir"])
    tahun_sekarang = datetime.now().year
    usia = tahun_sekarang - tahun_lahir

    ai_output = ai_call(tahun_lahir)

    return render_template(
        "cek_usia.html",
        usia=usia,
        tahun_lahir=tahun_lahir,
        ai_output=ai_output,
    )
  return render_template("cek_usia.html", usia=None)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=2008)