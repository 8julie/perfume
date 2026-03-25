# perfume

Takes a Fragrantica fragrance and gives you possible ingredients that are in said fragrance with TGSC data. 

An ongoing project. Not intended to be complete. Feel free to submit issues if you run into them!




# Documentation

|File|Notes|
|--|--|
|[`README.md`](README.md)|This current file|
|[`REFERENCE.md`](REFERENCE.md)|A reference guide for how the data is structured in this repo|
|[`NOTES.md`](NOTES.md)|Contains notes about data sources|



# Installation guide
Optional: To run tests use ``python test.py``



## Python
`pip install requests `

`pip install beautifulsoup4`



## Running

1. Initial build: ``python scraper.py``
   + `/ingredients` and `index.json` should appear (they are gitignored)
2. Connect to FragDB