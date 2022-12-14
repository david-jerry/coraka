from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from coraka.users.views import consent, subscribe

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("firm/", TemplateView.as_view(template_name="pages/firm.html"), name="firm"),
    path("network/", TemplateView.as_view(template_name="pages/career.html"), name="career"),
    path("portfolio/", TemplateView.as_view(template_name="pages/portfolio.html"), name="portfolio"),
    path(
        "contact/", TemplateView.as_view(template_name="pages/contact.html"), name="contact"
    ),
    path('consent', consent, name='consent'),
    path('subscribe', subscribe, name='subscribe'),
    # Django Admin, use {% url 'admin:index' %}
    path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    path(
        "jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")
    ),  # Django JET dashboard URLS
    path("admin/", include("admin_honeypot.urls", "admin_honeypot")),
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
