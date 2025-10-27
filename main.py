import random
import csv

def get_random_quote(filename="quotes.csv"):
    quotes = []
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                quotes.append({"quote": row[0], "author": row[1]})
    return random.choice(quotes)

def main():
    print("-----------------------------------------")
    print("     🌟 AI-Powered Quote Generator 🌟")
    print("-----------------------------------------\n")

    quote_data = get_random_quote()
    print(f'"{quote_data["quote"]}"\n   — {quote_data["author"]}\n')

if __name__ == "__main__":
    main()
