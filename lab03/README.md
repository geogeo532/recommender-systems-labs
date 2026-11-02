# Laborator 3: Sistem de recomandare cu Recombee - trimitere items

## Dataset

**Nume:** IMDB Top 1000 Movies  
**Sursă:** [Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)  
**Fișier:** `../lab02/imdb_top_1000.csv`  
**Număr de înregistrări:** 1000 filme

## Proprietăți trimise în Recombee

| Proprietate | Tip | Coloană CSV |
|---|---|---|
| `title` | string | `Series_Title` |
| `released_year` | int | `Released_Year` |
| `imdb_rating` | double | `IMDB_Rating` |
| `genre` | string | `Genre` |
| `director` | string | `Director` |
| `runtime_minutes` | int | `Runtime` |

> `itemId` este generat din indexul rândului din CSV (0–999), deoarece dataset-ul nu conține o coloană de ID dedicată.

## Rulare script

```bash
pip install recombee-api-client pandas
python recombee_items.py
```
