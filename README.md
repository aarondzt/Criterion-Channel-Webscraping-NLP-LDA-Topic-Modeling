# Webscraping the Criterion Channel Collection

[Data source](https://films.criterionchannel.com)
 
### Abstract
For our project, we used film metadata from the Criterion Channel (https://www.criterionchannel.com). The Criterion Channel describes itself as “A Movie Lover’s Dream – Classics and discoveries from around the world, thematically programmed with special features, on a streaming service brought to you by the Criterion Collection.” It is a streaming service for films in the Criterion Collection, but unlike services such as Netflix and Hulu, it does not rely on a recommendation engine to suggest films for viewers to watch. Instead, it relies on a weekly hand-curated newsletter delivered by email that alerts viewers of new or relevant content. For this reason, we decided to build a recommendation engine for the Criterion Channel – one that would allow a viewer to input a film they recently watched and enjoyed, and then receive a list of similar films. We developed two types of content-based recommendation engines: The first uses Latent Dirichlet Allocation (LDA) topic modeling computed over film descriptions; this method takes a target film and then outputs a list of similar films within the same topic ranked by IMDB rating. The second uses cosine similarity computed over TF-IDF matrices of film descriptions; this method takes a target film and then outputs a list of the closest films based on cosine similarity. These two recommendation engines give viewers two options to play with in order to find the next film that they would likely enjoy.

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


