# Webscraping the Criterion Channel Collection

## Contents
* [Data source](https://films.criterionchannel.com)
* [Technical notebook](Webscraping.ipynb)
* [CSV of scraped data](data/Criterion.csv)
 
## Summary
For this project, I decided to use the Criterion Channel Collection for a webscraping exercise. The Criterion Channel is a streaming service like Netflix, but for the classic films inducted into the Criterion Collection. 

## Discussion

I was surprised to find that the country with the most representation in the Collection is Japan, and that the director Keisuke Kinoshita (whom I had never heard of previously) has ~40 films in the collection. Kinoshita was an extremely prolific filmmaker (To quote Kinoshita: "I can’t help it. Ideas for films have always just popped into my head like scraps of paper into a wastebasket") who was also held in consistently high regard by critics. Given that the Collection focuses on films regarded as classics, I was not surprised that the golden decade of filmmaking, the 1960s, had the most entries.

## Limitations and Future Directions
The organization of the films on the Criterion Channel website is not perfect, so there are some minor errors in the data that I scraped that probably need to be manually corrected. In the future, I may use this dataset for a natural language processing project, or combine it with other film datasets to explore the features of these films in greater depth.

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


