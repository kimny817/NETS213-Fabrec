import pandas as pd
import csv

def process(mturk_res):
    input_items = mturk_res['Input.user_input']
    input_items = list(dict.fromkeys(input_items))

    result = []

    for i in input_items:
        t = ()
        t += (i,)
        for index, hit in mturk_res[mturk_res['Input.user_input'] == i].iterrows():
            for j in range(1, 4):
                t += (hit['Answer.link' + str(j)],)
        result.append(t)

    return result 


# Your main function

def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res = pd.read_csv('HIT2 Sample Output.csv')

    result = process(mturk_res)
    
    df = pd.DataFrame(result, columns = ['user_input', 'link1', 'link2', 'link3', 'link4', 'link5', 'link6', 'link7', 'link8', 'link9'])
    df.to_csv('HIT2Result.csv', index=False)

if __name__ == '__main__':
    main()
