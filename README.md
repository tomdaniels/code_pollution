# Language Stats

Uses public GitHub API's to determine the total number of bytes you have written in each programming language by looking through all of your github projects.

Clone the repository and install the requirements.txt with `pip`. Run the script with your PAT via command line args:

```bash
python .main.py -t <YOUR_PAT>
```

For users with huge repository numbers the calls will be quite expensive, using your PAT increases the rate limit to 5000 an hour I think so it should be safe but that's why it's asking for your PAT.

Script also supports `ignore_repos`, for example some "workspace"'s count as a repository but are not valid requests for the `/repos` endpoint. The script might crash if that happens but the repo name will be in the url so run it again with `-i <REPO_NAME>`. It can support a list of names too.

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
