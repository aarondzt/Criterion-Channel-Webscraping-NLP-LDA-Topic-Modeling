# Webscraping the Criterion Channel Collection

## Contents
* [Data source](https://films.criterionchannel.com)
* [Code/report](Webscraping.ipynb)
* [CSV of scraped data](data/Criterion.csv)
 
## Overview
For this project, I decided to use the Criterion Channel Collection for a webscraping exercise. The Criterion Channel is a streaming service like Netflix, but for the classic films inducted into the Criterion Collection. I am interested in what directors, countries, and decades are most highly represented in this collection. It seems like [someone](https://www.reddit.com/r/criterion/comments/bbbgo0/im_a_web_developer_and_a_big_fan_of_criterion_ive) has embarked on a similar project before, and it was well-received by the community of Criterion fans. However, the link to the webpage they created is currently broken, so this project could potentially serve to fill that niche.

## Goals
To create a .csv file containing all the films in the Criterion Channel with their corresponding directors, countries, years of release and descriptions. Then, to run exploratory data analysis to determine what directors, countries, and decades are most highly represented. A further motivation is that this dataset could be used in the future for a natural language processing project, or combined with other film datasets to explore the features of these films in greater depth. Overall, I hope that this project can be an interesting resource for anyone who wants to learn more about the artistic achievements in the global history of film.

## Discussion

The final dataset has seven columns (Title	Director	Country	Year	Total Hours	Description	Url) and 1454 rows (representing the feature-length films in the collection). I was surprised to find that the country with the most representation in the Collection is Japan, and that the director Keisuke Kinoshita (whom I had never heard of previously) has ~40 films in the collection. Kinoshita was an extremely prolific filmmaker (To quote Kinoshita: "I can’t help it. Ideas for films have always just popped into my head like scraps of paper into a wastebasket") who was also held in consistently high regard by critics. Given that the Collection focuses on films regarded as classics, I was not surprised that the golden decade of filmmaking, the 1960s, had the most entries. 

Although the Criterion Collection is supposed to represent the greatest films ever released, mere numerical representation does not make a director, country, or decade the greatest. It would be interesting to combine a dataset of ratings or some metric of influence in order to weight the films per director. Another idea would be to combine a dataset of country features to determine which country produces the most Criterion Collection films per capita, relative to GDP, etc. 

## Limitations
The organization of the films on the Criterion Channel website is not perfect, so there are some minor errors in the data that I scraped that probably need to be manually corrected.

## Project Info
<pre>
Contributors : <a href=https://github.com/aarondzt>Aaron Tan</a>
</pre>

<pre>
Languages    : Python
Tools/IDE    : Anaconda
Libraries    : numpy, pandas, requests, BeautifulSoup, matplotlib, seaborn
</pre>

<pre>
Duration     : October 2020
Last Update  : 10.02.2020
</pre>


