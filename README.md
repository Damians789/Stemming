# Stemming
The purpose of this program was to experiment with different stemmatizers

I was working on SMS Spam Collection database, which consisted mainly of caller ID and the text message itself.

The stemmers that were compared during the experiment:
- Porter Stemmer
- Lancaster Stemmer
- Snowball Stemmer
- Krovetz Stemmer
- Regexp Stemmer

Some general context

Stemming comes from the root of the word 'stem'. It is a normalization technique (or a word) that is found on the text of various morphological variations of a proper word having its 'stem', e.g. the word 'wait' has the same meaning as 'waiting', 'waited', 'waited'. This method of pre-processing allows e.g. for searching words in search engines.

Results

The results are mostly what we should expect. Lancaster Stemmer often works too zealously, which causes the word to lose its original meaning. Regexp Stemmer works as instructed. Stemmers Porter and Snowball have a high similarity ratio of results (~98%), which is not surprising, because they are the work of the same creator. Porter, Snowball and Krovetz Stemmer are a group that shows higher similarity of results than the rest of the tested stemmers (~65%).

![obraz](https://user-images.githubusercontent.com/92166393/207657886-bfa19294-35c4-4ae2-bd17-991d2f082909.png)
