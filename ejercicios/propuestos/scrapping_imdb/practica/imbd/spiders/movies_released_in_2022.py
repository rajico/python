import scrapy
import re


class MoviesReleasedIn2022Spider(scrapy.Spider):
    name = "movies-released-in-2022"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/search/title/?title_type=feature&release_date=2022-01-01,"
                  "2022-12-31&runtime=1,&sort=release_date,asc&count=250"]
    current_page = 1

    def parse(self, response):
        # Getting all movies from the list
        movies_el = response.css('div.lister-item > .lister-item-content')
        year_pattern = re.compile(r'\(.*?(\d+).*\)')

        for movie_el in movies_el:
            # Extracting movie information
            title = movie_el.css('.lister-item-header > a::text').get()

            try:
                year = movie_el.css(
                    '.lister-item-header > .lister-item-year::text').get()
                year = year_pattern.findall(year)[0]
            except:
                year = None

            try:
                duration = movie_el.css(
                    'p:nth-of-type(1) > span.runtime::text').get().split()[0]
            except:
                duration = None

            try:
                genres = movie_el.css(
                    'p:nth-of-type(1) > span.genre::text').get().strip()
            except:
                genres = None

            try:
                rating = movie_el.css(
                    '.ratings-bar > .ratings-imdb-rating > strong::text').get()
            except:
                rating = None

            try:
                synopsis = movie_el.css('p:nth-of-type(2)::text').get().strip()
            except:
                synopsis = None

            people_raw = ''.join([x.strip() for x in movie_el.css(
                'p:nth-of-type(3) *::text').getall()])
            people_raw_split = people_raw.split('|')

            try:
                directors = people_raw_split[0].split(':')[1]
            except:
                directors = None

            try:
                stars = people_raw_split[1].split(':')[1]
            except:
                stars = None

            # Return data extracted
            yield {
                "title": title,
                "year": year,
                "duration": duration,
                "genres": genres,
                "rating": rating,
                "synopsis": synopsis,
                "directors": directors,
                "stars": stars
            }

        # Handle pagination
        next_page = response.css('.next-page')
        if next_page and self.current_page < 37:
            self.current_page += 1
            yield response.follow(next_page[0])
