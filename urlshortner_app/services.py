from django.conf import settings
from random import choice
from string import ascii_letters, digits
from urllib.parse import urlparse

from .repos import UrlRepos

# Try to get the value from the settings module
SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAILABLE_CHARS = ascii_letters + digits


class UrlServices:
    repos = UrlRepos()

    def get_code_for_url(self, long_url):
        """
        Returns generated code for a given url
        """
        random_code = self.create_random_code()

        if random_code not in [obj.short_url for obj in self.repos.get_all_urls()]:   # random code - unique
            if not self.repos.url_exists(long_url):   # if url not in db
                return random_code
        else:   # if code is not unique
            self.get_code_for_url(long_url)   # generate again

    def save_url(self, long_url):
        code = self.get_code_for_url(long_url)
        short_url = ''.join((self.get_url_domain(long_url), '/', code))
        self.repos.save_url(
            long_url=long_url,
            short_url=short_url
        )

    @staticmethod
    def get_url_domain(long_url):
        return urlparse(long_url).netloc

    @staticmethod
    def create_random_code(chars=AVAILABLE_CHARS):
        """
        Creates a random string with the predetermined size
        """
        return "".join(
            [choice(chars) for _ in range(SIZE)]
        )