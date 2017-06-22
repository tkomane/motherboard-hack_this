# motherboard-hack_this
A repository for various scripts I'll be working on based on the Hack This tutorial series by Michael Byrne

The idea is to use this series to quickly familiarise myself with Git and Github whilst also doing some cool things with Python.

<h2>What the scripts do</h2>
<h3>extractor.py</h3>
This is a script that extracts <a href="https://en.wikipedia.org/wiki/Exif">Exif</a> data from a jpg image file. This includes things like the make and model of the device that took the picture, the date when it was taken, as well as more private information like the location where it was taken, etc.

If you feel like testing out the script, add your own picture (titled 'image.jpg') to a clone of the directory and then run it accordingly.

<h3>scraper.py</h3>
I had some fun with this. Michael's tut was (understandably) too undetailed, given that it's directed towards non-programmers, so because I decided to do my own thing rather than just copy word for word, I winded up getting a bit lost, but I still think what I came up with is cool.

Essentially it scrapes the <a href="http://www.imdb.com/chart/top">IMDb Top 250</a> chart and returns a list of the 'best' years for movies according to users of the website. These means the years with the highest freqeuncy on the chart.

Incidentally, these are the top  10 'best' years according to the users paired with frequency):
<ol>
<li>1995: 9</li>
<li>1957: 7</li>
<li>2000: 7</li>
<li>2003: 7</li>
<li>2001: 7</li>
<li>2009: 6</li>
<li>1975: 6</li>
<li>2014: 6</li>
<li>2010: 5</li>
<li>1997: 5</li>
</ol>

- hmm, not sure I agree.
