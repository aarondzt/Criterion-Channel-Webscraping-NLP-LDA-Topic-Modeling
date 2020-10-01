# Webscraping the Criterion Channel Collection
 
## Summary
For this project, I decided to use the Criterion Channel Collection for a webscraping exercise. The Criterion Channel is a streaming service like Netflix, but for the classic films inducted into the Criterion Collection. As you will see in the iPython Notebook, I used BeautifulSoup to scrape the titles, directors, release years, and countries of origin from https://films.criterionchannel.com. In order to scrape the durations of each film, I wrote a for loop that entered into each film's own page and scraped from "class_ = 'duration-container'." These durations came in the form of "HH:MM:SS" and had to be transformed using Python code in order to calculate total hours as a float. Additionally, I scraped the descriptions of each film, which may be interesting to analyze using natural language processing in the future. For my analysis, I excluded "films" with duration < 1 hour, since these were mostly shorts. I then plotted the value_counts for the directors, countries, and decades that have the most entries in the Criterion Collection. I was surprised to find that the country with the most representation in the Collection is Japan, and that the director Keisuke Kinoshita (whom I had never heard of previously) has ~40 films in the collection. Kinoshita was an extremely prolific filmmaker ("I can’t help it. Ideas for films have always just popped into my head like scraps of paper into a wastebasket") who was also held in consistently high regard by critics. Given that the Collection focuses on films regarded as classics, I was not surprised that the golden decade of filmmaking, the 1960s, had the most entries. 

Update: I tried to run the code again and it didn't work. It turns out the Criterion Channel added more films to their collection, but the films' links are broken, so I added a new piece of code that scrapes 200/404 outputs from requests.get and filters out 404 links.

## Limitations and Future Directions
The organization of the films on the Criterion Channel website is not perfect, so there are some minor errors in the data that I scraped that probably need to be manually corrected. In the future, I would be interested in combining this dataset with a dataset of audience/critic ratings. I could then use this combined dataset to guide my own selection of films to watch.

## Files
[Data source](https://films.criterionchannel.com)

[Technical notebook](Webscraping.ipynb)

[CSV of scraped data](data/Criterion.csv)
