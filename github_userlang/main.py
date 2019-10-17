from github import Github
from getpass import getpass


def main():
    u = input("YOUR GitHub username : ")
    p = getpass()

    g = Github(login_or_token=u, password=p)

    g_username = input("username to search : ")
    g_user = g.get_user(login=g_username)

    print(g_user.bio)


if __name__ == "__main__":
    main()
