from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.utils.feedgenerator import Atom1Feed


class PostsFeed(Feed):
    feed_type = Atom1Feed

    title = 'Pankaj Blog Feeds'
    link = '/blog/'
    description = 'latest Posts!'

    def items(self):
        return Post.objects.all()[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 20)

