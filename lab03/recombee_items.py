import pandas as pd
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import SetItemValues, Batch
from recombee_api_client.exceptions import APIException

DB_NAME = 'corbeanu-daniel-george-dev'
PRIVATE_TOKEN = 'cIVNgGDUI0e6D4fiAX34jB5EldTlIF8UWisupm8FRyynyQLX5EfTRnZs93VfOShf'
REGION = Region.EU_WEST

client = RecombeeClient(DB_NAME, PRIVATE_TOKEN, region=REGION)

PATH_DATASET = '../lab02/imdb_top_1000.csv'


def parse_runtime(runtime_str):
    try:
        return int(str(runtime_str).replace(' min', '').strip())
    except (ValueError, AttributeError):
        return 0


def parse_year(year_val):
    try:
        return int(year_val)
    except (ValueError, TypeError):
        return 0


def send_items():
    """Functie care citeste dataset-ul si trimite item-urile in Recombee"""
    df = pd.read_csv(PATH_DATASET)
    print(f"Se trimit {len(df)} item-uri in Recombee...")

    requests = []

    for index, row in df.iterrows():
        item_id = str(index)

        properties = {
            "title":           str(row['Series_Title']),
            "released_year":   parse_year(row['Released_Year']),
            "imdb_rating":     float(row['IMDB_Rating']),
            "genre":           str(row['Genre']),
            "director":        str(row['Director']),
            "runtime_minutes": parse_runtime(row['Runtime']),
        }

        # Adaugam request-ul de setare a valorilor pentru item
        # (SetItemValues creează automat item-ul dacă acesta nu există)
        requests.append(SetItemValues(item_id, properties, cascade_create=True))

        # Trimitem in loturi (batch) de cate 100 pentru eficienta
        if len(requests) == 100:
            client.send(Batch(requests))
            requests = []
            print("S-a trimis un lot de 100 item-uri...")

    # Trimitem si restul ramanase (daca numarul total nu e multiplu de 100)
    if requests:
        client.send(Batch(requests))
        print("S-a trimis ultimul lot de item-uri.")

    print("Toate item-urile au fost trimise cu succes!")


if __name__ == "__main__":
    send_items()
