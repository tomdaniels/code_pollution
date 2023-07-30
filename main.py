import argparse

from language_stats import GitHubLanguageStats

def parse_args():
    parser = argparse.ArgumentParser(description='Ever wondered how many bytes you have written in each programming language?')
    parser.add_argument('-t', '--token', default='', help='Your GitHub Pesonal Access Token (PAT)')
    parser.add_argument('-i', '--ignore', nargs='+', default=[], help='An ignore list of repository names')
    return parser.parse_args()

def main():
    args = parse_args()
    username = 'tomdaniels'
    stats = GitHubLanguageStats(username, token=args.token, ignore_list=args.ignore)
    print(stats.fetch_languages())

if __name__ == "__main__":
    main()
