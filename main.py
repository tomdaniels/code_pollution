import argparse

from functools import partial
from language_stats import GitHubLanguageStats

description = "Code pollution detector; how many bytes have you written?"

def parse_args():
    parser = argparse.ArgumentParser(description)
    add_argument = partial(parser.add_argument)

    add_argument('-u', '--username', default='', help='Your GitHub username')
    add_argument('-t', '--token',    default='', help='Your GitHub Pesonal Access Token (PAT)')
    add_argument('-i', '--ignore',   default=[], help='An ignore list of repository names', nargs='+')
    
    return parser.parse_args()

def main():
    args = parse_args()
    gh = GitHubLanguageStats(args)
    print(gh.fetch_language_bytes())

if __name__ == "__main__":
    main()
