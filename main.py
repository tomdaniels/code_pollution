import argparse

from language_stats import GitHubLanguageStats

def parse_args():
    parser = argparse.ArgumentParser(description="Code pollution detector; how many bytes have you written?")
    parser.add_argument('-u', '--username', default='', help='Your GitHub username')
    parser.add_argument('-t', '--token', default='', help='Your GitHub Pesonal Access Token (PAT)')
    parser.add_argument('-i', '--ignore', nargs='+', default=[], help='An ignore list of repository names')
    return parser.parse_args()

def main():
    args = parse_args()
    stats = GitHubLanguageStats(args)
    print(stats.fetch_languages())

if __name__ == "__main__":
    main()
