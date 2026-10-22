# Lab 02 — Dataset: IMDB Top 1000 Movies

## Descrierea domeniului

Dataset-ul conține cele mai bine cotate **1000 de filme** conform IMDB (Internet Movie Database). Acoperă o gamă largă de genuri cinematografice (dramă, comedie, thriller, acțiune etc.) și perioade istorice, de la filme clasice din anii '20 până la producții recente.

**Sursă:** [Kaggle — IMDB Dataset of Top 1000 Movies and TV Shows](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)

**Fișier CSV:** `imdb_top_1000.csv`  
**Număr de intrări:** ~1000 filme

---

## Proprietăți înregistrate în Recombee

| Proprietate | Coloană CSV | Tip de date | Descriere |
|---|---|---|---|
| `title` | `Series_Title` | `string` | Titlul filmului |
| `released_year` | `Released_Year` | `int` | Anul lansării filmului |
| `imdb_rating` | `IMDB_Rating` | `double` | Scorul IMDB (0.0 – 10.0) |
| `genre` | `Genre` | `string` | Genul/genurile filmului (ex: "Drama, Crime") |
| `director` | `Director` | `string` | Regizorul filmului |
| `runtime_minutes` | `Runtime` | `int` | Durata filmului în minute |

---

## Cum se rulează scriptul

```bash
pip install recombee-api-client pandas
python recombee_properties.py
```

> **Notă:** Înainte de rulare, completați `DB_NAME` și `PRIVATE_TOKEN` din contul vostru Recombee  
> (*Admin UI → Settings → API Logins*)
