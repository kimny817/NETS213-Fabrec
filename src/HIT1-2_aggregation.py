import pandas as pd
import csv

def process(mturk_res):
    inputData = mturk_res['Input.input']
    inputData = list(dict.fromkeys(target_items))

    count = {}
    result = []

    for i in inputData:
        count[1] = 0
        count[2] = 0
        count[3] = 0
        count[4] = 0
        count[5] = 0
        count[6] = 0
        count[7] = 0
        count[8] = 0
        for index, hit in mturk_res[mturk_res['Input.input'] == i].iterrows():
            for j in range(1, 9):
                column = 'Answer.link' + str(j) + '.on'
                if hit[column] == 'TRUE':
                    count[j] += 1
        s = sorted(count.iteritems(), key=lambda x:-x[1])[:3]
        t1 = 'Input.link' + s[0]
        t2 = 'Input.link' + s[1]
        t3 = 'Input.link' + s[2]
        result.append((i, hit[t1], hit[t2], hit[t3])

    return result 

# Your main function

def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res = pd.read_csv('HIT_Output.csv')

    ranks = process(mturk_res)

    df = pd.DataFrame(ranks, columns = ['input', 'top1', 'top2', 'top3'])
    df.to_csv('HIT_Result.csv', index=False)

if __name__ == '__main__':
    main()
