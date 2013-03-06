from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'shortener.views.index'),
    url(r'^add/$', 'shortener.views.add'),
    url(r'^remove/(?P<url_id>\d+)/$', 'shortener.views.remove'),
    url(r'^(?P<shortened_url>.*)/$', 'shortener.views.expand'),

    # Examples:
    # url(r'^$', 'shortener.views.home', name='home'),
    # url(r'^shortener/', include('shortener.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
