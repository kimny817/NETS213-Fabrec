
import pandas as pd
import csv

def process(mturk_res):
    target_items = mturk_res['Input.target_item']
    target_items = list(dict.fromkeys(target_items))
    output = []
    inner = []
    result = []

    for i in range (0, 10):
        inner.append(('Answer.link'+ str(i), 0))

    for k in range(len(target_items)):
        output.append(inner)
        for index, hit in mturk_res[mturk_res['Input.target_item'] == target_items[k]].iterrows():
            for i in range(1, 10):
                if (output[k][i][1] != -1):
                    if hit['Answer.link' + str(i)]  == 'Wrong':
                        output[k][i] = ('Answer.link' + str(i), -1)
                    else:
                        output[k][i] = ('Answer.link' + str(i), output[k][i][1] + int(hit['Answer.link' + str(i)]))
        output[k].sort(key=lambda tup: tup[1], reverse=True)
        rank1, rank2, rank3 = output[k][0][0], output[k][1][0], output[k][2][0]
        if (output[k][0][1] == -1): rank1 = 'N/A'
        if (output[k][1][1] == -1): rank2 = 'N/A'
        if (output[k][2][1] == -1): rank3 = 'N/A'
        result.append((target_items[k], rank1, rank2, rank3))

    return result 


# Your main function

def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res = pd.read_csv('HIT3 Sample Output.csv')

    ranks = process(mturk_res)

    df = pd.DataFrame(ranks, columns = ['target_item', 'choice 1', 'choice 2', 'choice 3'])
    df.to_csv('HIT3Result.csv', index=False)

if __name__ == '__main__':
    main()
