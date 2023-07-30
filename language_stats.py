import requests

from collections import defaultdict
from halo import Halo

class GitHubLanguageStats:
    def __init__(self, username, token, ignore_list=None):
        self.username = username
        self.ignore_list = ignore_list or []
        self.token = token
        self.spinner = Halo(text='Fetching and calculating...', spinner='dots')
        self.headers = {'Authorization': f'token {self.token}'}

    def fetch_repos(self):
        url = f'https://api.github.com/user/repos?per_page=100'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        repos = response.json()
        return [repo['name'] for repo in repos if repo['name'] not in self.ignore_list]

    def fetch_repo_languages(self, repo_name):
        url = f'https://api.github.com/repos/{self.username}/{repo_name}/languages'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def aggregate_languages(self, language_dicts):
        totals = defaultdict(int)
        for languages in language_dicts:
            for language, bytes in languages.items():
                totals[language] += bytes
        return totals

    def fetch_languages(self):
        self.spinner.start()
        repos = self.fetch_repos()
        language_dicts = [self.fetch_repo_languages(repo) for repo in repos]
        self.spinner.stop()
        return self.aggregate_languages(language_dicts)
