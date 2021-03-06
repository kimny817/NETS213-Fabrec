# Fabrec

_**By Jina Lo, Nayeong Kim, Rose Kong, Shannie Cheng**_

## Data

### Raw Data

#### data/image data

The raw data we have include the glossary of all the clothing styles. Specifically, we have included an image data folder in the github. image data is divided into four subcategories, including dress, pants, shoes, tops. All the images would represent a specific style of clothing in its category. The image data is used in HIT1-2, which is the style matching. We would give Turkers either a top and ask them to find a matching style bottom, a bottom to find a matching style top, or a dress to find a matching style shoes.

Each image data is names in the format of *style*.jpg which would be helpful for us to process the data later on in our aggregation or quality control module

### Input/Output Data

#### data/HIT1
HIT1 consists of 2 sub-HITs which are labeled HIT1-1 and HIT1-2. HIT1-2 is used for color matching, where the input data would be consists of input.color, which is the color to ask turkers to match on. In addition, there are 9 different colors given to turkers where we ask turkers to select and rank top 4 matching color.

HIT1-1 output would consist of all the turkerIDs, HITs description as well as the input.color, answer.color1, answer.color2, answer.color3, answer.color4 which represent the top 4 matching color selected by turkers. 

HIT1-2 consists of style matching, which the input would be a picture of either a top/bottom/dress, and there would be 9 complementary pictures given to turkers for them to select. HIT1-2 output would consists of all the pictures as well as the number of times each picture is clicked. 

HIT1 would represents as the reference data which would direct future turkers in providing clothes recommendations based on user input.

#### data/HIT2
HIT2 is used to collect clothing recommendations from workers while presenting them the color and style matching we obtained from HIT1-1 and HIT1-2. Workers are presented with input CSV which suggests 3 styles and 3 colors. The worker must input 3 links for pieces of recommended clothing. 

#### data/HIT3
HIT3 takes the links submitted in HIT2 and asks Turkers to flag non-clothing items or inappropriate links. Additionally, Turkers will choose the best 3 items of clothing. The input CSV contains all the links to clothing items recommended by Turkers. The output CSV shows the flagged items in addition to how many votes there are for each item. 

## Src

### Quality Control/Aggregation Module

#### src/*_aggregation.py 
Aggregation Module consists of several parts. The first part would be collecting the top 3 ranking matching colors and top 3 matching styles from HIT1.

Second part would include the output from the first part, which is used as a reference for turkers to recommendations to user input. Then the data aggregated from HIT2 would consist of all the links submitted. 

Third part (HIT3) would be getting the top 3 links from HIT2 that was voted the most. 

#### src/*_qc*.py 

Quality control exists in processing the HIT3 outputs, where we would ask turkers to flag non-clothing or inappropriate pictures, we would exclude the these pictures. Our second quality control is implemented in HIT3. We will insert a link to a non-clothing item and filter out answers accordingly. 
