# Bama Course Equivalency WebScraper

[![GitHub issues](https://img.shields.io/github/issues/joexu22/BamaWebScraper.svg?style=plastic)](https://github.com/joexu22/BamaWebScraper/issues) [![GitHub forks](https://img.shields.io/github/forks/joexu22/BamaWebScraper.svg?style=plastic)](https://github.com/joexu22/BamaWebScraper/network) [![GitHub stars](https://img.shields.io/github/stars/joexu22/BamaWebScraper.svg?style=plastic)](https://github.com/joexu22/BamaWebScraper/stargazers) [![GitHub license](https://img.shields.io/badge/license-Apache%202-blue.svg?style=plastic)](https://raw.githubusercontent.com/joexu22/BamaWebScraper/master/LICENSE)

**Bama Course Equivalency WebScraper** is a web-scraping project which allows an University of Alabama, Tuscaloosa student to check where in the country they can take a course, without having to be at Bama. This project was brought about by a personal desire to not return to Bama just for a specific class.

_Roll Tide!_<br>
[![](Images/BamaBanner.png)](https://ssb.ua.edu/pls/PROD/rtstreq.P_Searchtype)

--------------------------------------------------------------------------------

## Table of Contents

1. **[How To](#how-to-use)**
2. **[Support](#support)**
3. **[Authors](#authors)**
4. **[License](#license)**

## How To Use?

This **WebScraping** service is currently under construction...<br>

Install Docker

Run the following command for a simple BeautifulSoup test code:<br>
```docker-compose up```

TODO: I actually need to get to the real part of the project, the Selenium scraper

TODO: This does not yet work as intended
docker run --rm -d -v mysql:/var/lib/mysql \
  -v mysql_config:/etc/mysql -p 5000:5000 \
  --network mysqlnet \
  --name mysqldb \
  -e MYSQL_ROOT_PASSWORD=password \
  mysql

docker run \
  --rm -d \
  --network mysqlnet \
  --name rest-server \
  -p 5001:5001 \
  bama-web-scraper

It will be made available once the product is finished. The idea is that the user can simply enter in the course ID for the Bama class and it will automatically search for all relevant classes in the country, as listed on the equivalency table.

## Support

Write me a suggestion at my personal web-page:

- [Contact](http://www.xuguanzhou.io)

## Authors

**[Xu Guanzhou, "Joe"](https://github.com/joexu22/BamaWebScraper)**

## License

[![Apache License](Images/ApacheLicense.png)](http://www.apache.org/licenses/)

**[⬆ back to top](#table-of-contents)**
