import pandas as pd
import numpy as np

INPUT_INDEX = ['Input.link1', 'Input.link2', 'Input.link3', 'Input.link4', 'Input.link5',
               'Input.link6', 'Input.link7', 'Input.link8', 'Input.link9']

ANSWER_INDEX = ['Answer.link1', 'Answer.link2', 'Answer.link3', 'Answer.link4', 'Answer.link5',
                'Answer.link6', 'Answer.link7', 'Answer.link8', 'Answer.link9']

CLOTHES_LINK_INDEX = ['link1', 'link2', 'link3', 'link4',
                      'link5', 'link6', 'link7', 'link8', 'link9']


def clothes_ranking_aggregation(csv_file_path):
    clothes_ranking = pd.read_csv(csv_file_path)

    all_input_clothes = set()
    clothes_score = dict()
    output_df = pd.DataFrame(columns=['input_image', 'top_link1', 'top_link2',
                                      'top_link3', 'top_link4'])

    # get all input colors
    for input_clothes in clothes_ranking['Input.input']:
        all_input_clothes.add(input_clothes)

    print(len(all_input_clothes))

    # find clothes for each of the input
    for input_clothes in all_input_clothes:
        clothes_bool = clothes_ranking['Input.input'] == input_clothes
        individual_clothes_df = clothes_ranking[clothes_bool]

        clothes_score_dict = dict()
        for i in range(len(INPUT_INDEX)):
            input_link_index = INPUT_INDEX[i]
            score_index = ANSWER_INDEX[i]
            clothes = individual_clothes_df[input_link_index].values[0]
            clothes_score_sum = np.sum(individual_clothes_df[score_index].values)

            clothes_score_dict[clothes] = clothes_score_sum

        top_three_clothes_score = sorted(clothes_score_dict.items(),
                                         key=lambda kv: kv[1], reverse=True)[:4]
        clothes_link_array = []
        for key, value in top_three_clothes_score:
            length = len(key)
            index = int(key[(length - 5):(length - 4)])
            clothes_index = CLOTHES_LINK_INDEX[index - 1]
            clothes_link = individual_clothes_df[clothes_index].values[0]

            clothes_link_array.append(clothes_link)

        output_df = output_df.append({'input_image': input_clothes, 'top_link1': clothes_link_array[0],
                                      'top_link2': clothes_link_array[1],
                                      'top_link3': clothes_link_array[2],
                                      'top_link4': clothes_link_array[3]}, ignore_index=True)

    return output_df







clothes_ranking_aggregation('Batch_235617_batch_results.csv')
