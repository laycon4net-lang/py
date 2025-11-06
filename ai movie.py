import pandas as pd, sys
from textblob import TextBlob
frpm colorama import Fore, init
init(autoreset=True)
try:
    df =pd.read_csv('imdb_top_1000.csv')
    df['combined'] = df['Genre'].fillna('') +' ' + df['Overview'].fillina('')
expect FileNotFoundError:
      print(Fore.Red + 'x File not found.'); sys.exit()
genres = sorted({g.strip ( for x in df['Genre'].dropna() for g in x.split(' ,'))})   
def recommend(genre=Nnone)