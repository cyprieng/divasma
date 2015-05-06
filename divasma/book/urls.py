from django.conf.urls import patterns, url

urlpatterns = patterns('divasma.book.views',
    url(r'^(?P<id>\d+)-(?P<slug>[A-Za-z\-]+)', 'book_view'),
)
