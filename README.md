# Code pollution detector

Uses the public GitHub API to determine the total number of bytes you have written in each programming language by looking through all of your github repositories.

You need your PAT (this helps with rate limiting for folks with alot of repos) and can also provide an ignore_list. Some workspaces should be filtered out as they do get returned from the Github `/repos` endpoint, but will throw an exception on the `/languages` endpoint. If that happens, just add the repository name from the endpoint stacktrace after the `-i` flag.

## Get Started

Clone or download the repository and install the requirements.txt with `pip`. Run the script with your PAT via command line args:

```bash
usage: main.py [-h] [-t TOKEN] [-i IGNORE [IGNORE ...]]

Code pollution detector; how many bytes have you written?

options:
  -h, --help            show this help message and exit
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
