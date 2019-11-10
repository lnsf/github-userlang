from github import Github
from getpass import getpass
import matplotlib.pyplot as plt
import json
import os
from time import sleep


def main():
    u = input("YOUR GitHub username: ")
    p = getpass()

    g = Github(login_or_token=u, password=p)

    g_username = input("username to search: ")
    g_user = g.get_user(login=g_username)

    g_repos = g_user.get_repos()

    repos = []
    repo_index = 0
    while True:
        sleep(1)
        repos_page = g_repos.get_page(repo_index)
        if len(repos_page) == 0:
            break
        repos = [*repos, *repos_page]
        repo_index += 1

    langs = {}
    for r in repos:
        if r.language not in langs.keys():
            langs[r.language] = 1
        else:
            langs[r.language] += 1

    sorted_langs = sorted(langs.items(), key=lambda x: x[1], reverse=True)
    print(sorted_langs)

    # pie chart
    colors = []
    with open(os.getcwd() + '/github-colors' + '/colors.json', 'r') as file:
        j = json.load(file)
        for lang in sorted_langs:
            if lang[0] in j.keys():
                colors.append(j[lang[0]]['color'])
            else:
                colors.append('#FFFFFF')

    print(colors)


if __name__ == "__main__":
    main()
