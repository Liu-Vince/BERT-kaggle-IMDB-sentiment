import os
import pandas as pd
from sklearn.utils import shuffle


if __name__ == '__main__':
    path = "glue/"
    pd_all = pd.read_csv(os.path.join(path, "data.tsv"), sep='\t' )
    pd_all = shuffle(pd_all)


    dev_set = pd_all.iloc[0:int(pd_all.shape[0]/10)]
    train_set = pd_all.iloc[int(pd_all.shape[0]/10): int(pd_all.shape[0])]
    dev_set.to_csv("glue/dev.tsv", index=False,encoding= 'utf-8' ,sep='\t')
    train_set.to_csv("glue/train.tsv", index=False,encoding= 'utf-8' ,sep='\t')