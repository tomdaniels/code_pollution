import requests

from collections import defaultdict
from halo import Halo

class GitHubLanguageStats:
    BASE_URL = 'https://api.github.com'

    def __init__(self, args):
        self.username = args.username
        self.token = args.token
        self.ignore_list = args.ignore or []
        self.spinner = Halo(text='Fetching and calculating...', spinner='dots')
        self.headers = {'Authorization': f'token {self.token}'}

    def fetch_json(self, url):
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_repos(self):
        repos = self.fetch_json(f'{self.BASE_URL}/user/repos?per_page=100')
        filtered_repos = [];
        for repo in repos:
            if repo["name"] not in self.ignore_list:
                filtered_repos.append(repo["name"])
        return filtered_repos;

    def fetch_repo_languages(self, repo_name):
        url = f'{self.BASE_URL}/repos/{self.username}/{repo_name}/languages'
        return self.fetch_json(url)

    def aggregate_languages(self, language_dicts):
        totals = defaultdict(int)
        for languages in language_dicts:
            for language, bytes in languages.items():
                totals[language] += bytes
        return totals

    def fetch_language_bytes(self):
        self.spinner.start()
        repos = self.fetch_repos()
        language_dicts = list(map(self.fetch_repo_languages, repos))
        self.spinner.stop()
        return self.aggregate_languages(language_dicts)
