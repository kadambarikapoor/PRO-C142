import csv

all_articles = []
liked_articles = []
unliked_articles = []

with open('articles.csv', encoding = "utf-8") as f:
    reader = csv.reader(f)
    articles = list(reader)
    all_articles = articles[1:]