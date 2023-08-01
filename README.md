# Code pollution detector

Uses the public GitHub API to determine the total number of bytes you have written in each programming language by looking through all of your github repositories.

You need:

- `-u` username (github)
- `-t` [PersonalAccessToken](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) _helps with rate limiting_.

## Get Started

Clone or download the repository and install the requirements.txt with `pip`. Run the script with your username & PAT via command line args:

```bash
usage: main.py [-h] [-u USERNAME] [-t TOKEN] [-i IGNORE [IGNORE ...]]

Code pollution detector; how many bytes do you do?

options:
  -h --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Your GitHub username
  -t TOKEN, --token TOKEN
                        Your GitHub Pesonal Access Token (PAT)
  -i IGNORE [IGNORE ...], --ignore IGNORE [IGNORE ...]
                        An ignore list of repository names
```

### What you get:

```python
# a dict of all languages you have written with the total number of bytes
bytes_written = {
  'HTML': 43437, 'JavaScript': 517276,
  'CSS': 32389, 'Java': 16514, 'C++': 25858,
  'Elm': 2435, 'SCSS': 15376, 'ASP.NET': 181725,
  'C#': 8352, 'Less': 2723, 'Kotlin': 11464,
  'Dockerfile': 384, 'Python': 3253, 'TypeScript': 146401}
```

---

#### Exceptions

**`--ignore` is only helpful if you have any [CodeSpace](https://github.com/features/codespaces) projects.**
