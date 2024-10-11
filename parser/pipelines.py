# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from core.models import Publication, Category


class PublicationPipeline:
    async def process_item(self, item, spider):
        category, _ = await Category.objects.aget_or_create(
            name=str(item.get("category")).lower().strip()
        )

        publication, _ = await Publication.objects.aget_or_create(
            title=item.get("title"),
            category=category,
            preview=item.get("preview"),
            link=item.get("link"),
            date=item.get("date"),
        )

        return item
