import sys
import time
import datetime
import dt.user
import dt.excel
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

addin = dt.excel.Addin('AddinPCA', 'This is a simple Excel addin that uses sklearn.decomposition.PCA()')

@addin.expose(description='PCA', help='Give a matrix to the function')
def pca(matrix: list, n_comp=3) -> list:
    pca = PCA(n_components=n_comp)
    pca.fit(matrix)
    return pca.transform(matrix).tolist()

@addin.expose(description='Generate random data', help='Give number of rows and columns to the function')
def generate_df(n=1000, m=3) -> pd.DataFrame:
    return pd.DataFrame(np.random.randn(n, m))

@addin.expose(description='PCA on random data', help='Give number of rows, columns, and components to the function. It will generate a matrix and compute PCA on it (just for fun))')
def pca_random(n=1000, m=3, n_comp=3) -> list:
    pca = PCA(n_components=n_comp)
    matrix = np.random.randn(n, m)
    pca.fit(matrix)
    return pca.transform(matrix).tolist()

def __excel_main__(port, debug=False):
     addin.run(port=port)

if __name__ == '__main__':
    __excel_main__(int(sys.argv[1]))
