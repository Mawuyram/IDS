import pandas as pd

from model_pipeline.model import PacketAnalyzerIDS

path = '../lib/data/NSL-KDD.csv'

data = pd.read_csv(path)
data_svm = pd.read_csv(path)

model = PacketAnalyzerIDS()


def buildModel():
    model.RFC_model_pipeline(data)
    model.SVM_model_pipeline(data_svm)


if __name__ == "__main__":
    buildModel()
