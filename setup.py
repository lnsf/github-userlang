import setuptools
import os
import subprocess

setuptools.setup()

if os.path.exists(os.getcwd() + '/github-colors'):
    os.chdir('./github-colors')
    subprocess.run(['git', 'pull'])
else:
    subprocess.run(
        ['git', 'clone', 'https://github.com/ozh/github-colors',
            os.getcwd() + '/github-colors']
    )
