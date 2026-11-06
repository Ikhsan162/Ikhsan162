from datetime import datetime
import os
import markdown
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from groq import Groq
import requests

app = Flask(__name__)

# Mengambil API key secara aman dari Environment Variables Render
AI_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=AI_KEY) if AI_KEY else None


def ai_call(year):
  try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": (
                    f"Berikan tepat 1 fakta menarik seputar teknologi pada"
                    f" tahun {year}. Jawab dengan sangat singkat, padat, dan"
                    " langsung pada intinya dalam satu paragraf saja."
                ),
            }
        ],
        model="qwen/qwen3.8-27b",
        max_tokens=150,  # <-- Tambahkan pembatas token di sini agar tidak error 429
        stream=False,
    )

    ai_output = chat_completion.choices[0].message.content
    return markdown.markdown(ai_output)
  except Exception as e:
    return f"Maaf, AI tidak tersedia saat ini. (Error: {e})"


def scrape_news(name, url):
  try:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
    }
    response = requests.get(url, headers=headers, timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")

    if name == "kompas":
      # Mencari langsung tag h2 atau h3 pertama yang biasanya memuat headline utama Kompas
      headline_element = soup.find("h2", class_="article__title") or soup.find(
          "h3", class_="article__title"
      )
      if not headline_element:
        # Fallback cadangan jika kelas spesifik tidak ketemu
        headline_element = soup.find("h3")
    elif name == "detik":
      headline_element = soup.find("h2", class_="media__title")
    elif name == "tribun":
      headline_element = soup.find("div", class_="hltitle")
    else:
      headline_element = None

    if headline_element:
      return headline_element.text.strip()
    else:
      return "Headline tidak ditemukan (Struktur web mungkin berubah)"
  except Exception as e:
    return f"Gagal mengambil berita: {e}"


@app.route("/")
def main():
  kompas = scrape_news("kompas", "https://www.kompas.com/")
  detik = scrape_news("detik", "https://news.detik.com/")
  tribun = scrape_news("tribun", "https://www.tribunnews.com/")

  return render_template("index.html", news1=kompas, news2=detik, news3=tribun)


@app.route("/usia", methods=["GET", "POST"])
def cek_usia():
  if request.method == "POST":
    try:
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
    except ValueError:
      return render_template(
          "cek_usia.html", usia=None, error="Masukkan tahun yang valid!"
      )
  return render_template("cek_usia.html", usia=None)


if __name__ == "__main__":
  app.run(host="127.0.0.1", port=2008, debug=True)
