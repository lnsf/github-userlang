from github import Github
from getpass import getpass
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

    sorted(langs)


if __name__ == "__main__":
    main()
