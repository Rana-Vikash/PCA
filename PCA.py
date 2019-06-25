# Import Library to read csv from Drive
from google.colab import drive 
drive.mount('/content/gdrive')

# Import Libraries
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as RMS
from sklearn.decomposition import PCA

# Read CSV 'NSEI'
df = pd.read_csv('gdrive/My Drive/Colab Notebooks/NSEI.csv')
df.columns

# Remove all the Null 
dt = df.dropna()
dt.drop('Date', axis=1, inplace=True)
dt.dtypes

dt.to_csv('gdrive/My Drive/Colab Notebooks/NSEI_1.csv', sep='\t', encoding='utf-8')
dt.isna().sum()

# Preprocessing
X = dt.drop('Close', 1)
Y = dt['Close']

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Normalization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
X_train = sc.fit_transform(X_train)  
X_test = sc.transform(X_test) 

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA()  
X_train = pca.fit_transform(X_train)  
X_test = pca.transform(X_test)

explained_variance = pca.explained_variance_ratio_  
explained_variance
