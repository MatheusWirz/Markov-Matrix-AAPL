import pandas as pd
import numpy as np
import yfinance as yf

#-#
# Principal function
def markov(ticker):
    # Download data
    df = yf.download(ticker, period="5y", auto_adjust=True)
    df['Returns'] = df['Close'].pct_change()

    # Checks if the signal is positive or negative
    df['State'] = np.sign(df['Returns'])
    df['State'] = df['State'].replace({1: 'Positive', -1: 'Negative', 0: 'Neutral'})
    df = df[df['State'] != 'Neutral']

    # New column with the state of the day before
    df['Last_State'] = df['State'].shift(1)
    df.dropna(inplace=True)

    # Create a matrix of counts
    count_matrix = pd.crosstab(df['Last_State'], df['State'])

    # Create a matrix of probabilities
    prob_matrix = count_matrix.div(count_matrix.sum(axis=1), axis=0).map(lambda x: f"{x:.2%}")
    
    print('Matrix of Counts: \n', count_matrix)
    print('\n\nMatrix of Probabilities: \n' ,prob_matrix)

markov("AAPL")

