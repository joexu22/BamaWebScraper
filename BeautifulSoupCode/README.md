# Beautiful Soup as a Web-Scraping Tool

Admittedly this is a code graveyard.
I guess I wrote the original here as a way of going through the BeautifulSoup documentation.
From the hints, given in the code, I assume that there was some book related to Packet Publishing that I used as a template.
In any case, I am here to revive some dead code.

Note To Self -
    My coding skills do not seem to be all that better than from before
    At least I can now sniff out bad code.

## Todo

I've changed all of these into a suite of Python unittest
What I need to do is turn this into automated test suit using a CICD pipeline

## To Run

Run this from a parent folder
```python3 -m unittest discover .```

## To Run Using Docker

docker build -t bama-web-scraper .
docker run -p 3000:3000 bama-web-scraper

## To Run Using Docker Compose

docker-compose up