from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'corrigendum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
