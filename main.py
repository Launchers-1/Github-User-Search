from flask import Flask, render_template, request, jsonify
from github import Github
import os

app = Flask(__name__)

# Replace <your_access_token> with your actual personal access token
access_token = os.environ['GithubApiCode']
github = Github(access_token)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/usersearch', methods=['POST'])
def usersearch():
  username = request.form['username']
  try:
    user = github.get_user(username)
    user_data = user.raw_data

    pfp = user_data['avatar_url']
    login = "@" + user_data['login']
    link = user_data['html_url']
    twitter_username = user_data.get('twitter_username', '')
    blog = user_data.get('blog', '')
    company = user_data.get('company', '')

    return render_template('index.html',
                           username=username,
                           login=login,
                           name=name,
                           public_repos=public_repos,
                           followers=followers,
                           following=following,
                           twitter_username=twitter_username,
                           blog=blog,
                           company=company,
                           country=country,
                           pfp=pfp,
                           link=link)  #
  except Exception as e:
    return render_template(
      'index.html',
      username=username,
      error=str(e),
    )


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
