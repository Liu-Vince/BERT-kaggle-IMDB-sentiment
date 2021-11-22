import os
import pandas as pd


if __name__ == '__main__':
    path = "tmp/emotion_out/"
    pd_all = pd.read_csv(os.path.join(path, "test_results.tsv") ,sep='\t',header=None)

    data = pd.DataFrame(columns=['sentiment'])
    print(pd_all.shape)

    for index in pd_all.index:
        neutral_score = pd_all.loc[index].values[0]
        positive_score = pd_all.loc[index].values[1]

        if max(neutral_score, positive_score) == neutral_score:
            # data.append(pd.DataFrame([index, "neutral"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = [0]
        else:
            #data.append(pd.DataFrame([index, "negative"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = [1]
        #print(negative_score, positive_score, negative_score)

    data.to_csv(os.path.join(path, "pre_sample.tsv"),sep = '\t')
    #print(data)