import pandas as pd

COLOR_INDEX_ANS = ['Answer.color1.on', 'Answer.color2.on', 'Answer.color3.on', 
'Answer.color4.on', 'Answer.color5.on', 'Answer.color6.on', 'Answer.color7.on', 'Answer.color8.on',
'Answer.color9.on','Answer.color10.on', 'Answer.color11.on', 'Answer.color12.on', 'Answer.color13.on', 'Answer.color14.on',
'Answer.color15.on', 'Answer.color16.on', 'Answer.color17.on']

COLOR_INDEX_IN = ['Input.color1','Input.color2', 'Input.color3', 'Input.color4', 'Input.color5', 'Input.color6', 'Input.color7', 
'Input.color8', 'Input.color9', 'Input.color10', 'Input.color11', 'Input.color12', 'Input.color13', 'Input.color14', 'Input.color15', 'Input.color16', 
'Input.color17']

def color_matching_aggregation(color_matching_output):

    all_input_colors = set()
    color_matching_score = dict()
    top_three_matching = []

    # get all input colors
    for input_color in color_matching_output['Input.target-color']:
        all_input_colors.add(input_color)

    for color in all_input_colors:
        matchings = dict()
        for incolor in all_input_colors:
            matchings[incolor] = 0

        v = color_matching_output[color_matching_output['Input.target-color'] == color]

        for i in range (0, 17):
            if True in v[COLOR_INDEX_ANS[i]].value_counts() :
 
                color2 = v[COLOR_INDEX_IN[i]]
                count = v[COLOR_INDEX_ANS[i]].value_counts()[True]
                matchings[color2.iloc[0]] = count
        sorted_x = sorted(matchings.items(), key=lambda kv: -kv[1])
        top_three_matching.append((color, sorted_x[0][0], sorted_x[1][0], sorted_x[2][0]))


    return top_three_matching


def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res = pd.read_csv('HIT1-1Result.csv')

    result = color_matching_aggregation(mturk_res)
    
    df = pd.DataFrame(result, columns = ['color', 'match1', 'match2', 'match3'])
    df.to_csv('HIT1-1Processed.csv', index=False)

if __name__ == '__main__':
    main()

