from .models import Shortener


class UrlRepos:
    @staticmethod
    def get_long_url(short_url):
        return Shortener.objects.get(short_url=short_url).long_url

    @staticmethod
    def url_exists(long_url):
        return Shortener.objects.filter(long_url=long_url).exists()

    @staticmethod
    def get_all_urls():
        return Shortener.objects.all()

    @staticmethod
    def save_url(long_url, short_url):
        if not Shortener.objects.filter(long_url=long_url).exists():
            Shortener.objects.create(
                long_url=long_url,
                short_url=short_url
            )
