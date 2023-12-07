import pandas as pd
import numpy as np


class LogisticRegression:
    def __init__(self):
        self.weight_ = None

    def fit(self, x, y):
        pass

    def predict(self, x, y) -> np.ndarray:
        pass



if __name__ == '__main__':
    # prepare for data set.
    data_path = 'dataset/'

    # train model
    clf = LogisticRegression()
    clf.fit()

    # predict
    clf.predict()
