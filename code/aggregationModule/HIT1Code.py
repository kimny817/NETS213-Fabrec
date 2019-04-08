import pandas as pd

COLOR_INDEX = ['Answer.color1', 'Answer.color2', 'Answer.color3', 'Answer.color4']


def color_matching_aggregation(csv_file_path):
    color_matching_output = pd.read_csv(csv_file_path)

    all_input_colors = set()
    color_matching_score = dict()
    top_three_matching = dict()

    # get all input colors
    for input_color in color_matching_output['Input.color']:
        all_input_colors.add(input_color)

    # find bidirectional color matching and score
    for input_color in all_input_colors:
        color_bool = color_matching_output['Input.color'] == input_color
        individual_color_df = color_matching_output[color_bool]

        for index in COLOR_INDEX:
            colors = individual_color_df[index].values

            for selected_color in colors:
                if index == COLOR_INDEX[0]:
                    score = 4
                elif index == COLOR_INDEX[1]:
                    score = 3
                elif index == COLOR_INDEX[2]:
                    score = 2
                elif index == COLOR_INDEX[3]:
                    score = 1

                if (input_color, selected_color) in color_matching_score:
                    color_matching_score[(input_color, selected_color)] \
                        = color_matching_score[(input_color, selected_color)] + score
                elif (selected_color, input_color) in color_matching_score:
                    color_matching_score[(selected_color, input_color)] \
                        = color_matching_score[(selected_color, input_color)] + score
                else:
                    color_matching_score[(selected_color, input_color)] = score

    all_tuples = color_matching_score.keys()
    # get the top three
    for color in all_input_colors:
        color_arr = []
        for in_color, sel_color in all_tuples:
            score = color_matching_score[(in_color, sel_color)]
            if color == in_color:
                color_arr.append((score, sel_color))
            elif color == sel_color:
                color_arr.append((score, in_color))
        color_arr = sorted(color_arr, reverse=True)[:3]
        top_three_matching[color] = [(color, item[1]) for item in color_arr]

    return top_three_matching
