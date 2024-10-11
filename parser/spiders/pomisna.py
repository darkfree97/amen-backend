import locale

from datetime import datetime
from typing import Any, Iterable
from scrapy import Spider
from scrapy.http import Request, Response

from core.models import Publication


locale.setlocale(locale.LC_ALL, "uk_UA.utf8")


class PomisnaSpider(Spider):
    name = "pomisna"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.last_parsed_publication = Publication.objects.order_by("-date").first()

    def start_requests(self) -> Iterable[Request]:
        yield Request(url="https://www.pomisna.info/uk/category/vsi-novyny/")

    def parse(self, response: Response, **kwargs: Any):
        articles = response.css("body > div > div > div.row > div > article")
        for article in articles:
            item = dict()
            item["date"] = datetime.strptime(
                article.css(".date-item::text").get(), "%d %B %Y"
            ).date()
            item["category"] = article.css(".cat>a::text").get().strip()
            item["title"] = article.css("h3>a::text").get()
            item["link"] = article.css("h3>a::attr('href')").get()
            item["preview"] = article.css(".cat_on_thumb>a>img::attr('src')").get()

            if item["link"] == self.last_parsed_publication.link:
                return

            yield item
        next_url = response.css("a.next::attr('href')").get()
        if next_url:
            yield Request(url=next_url)
