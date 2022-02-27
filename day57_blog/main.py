from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blog_posts = blog_data)

# Just need to be careful with teh post_id as it is started from 1 (not 0) as the blog_id input from the challenge
@app.route('/<post_id>')
def a_post(post_id):
    return render_template("post.html", this_post = blog_data[int(post_id)-1])

if __name__ == "__main__":
    blog_data = requests.get("https://api.npoint.io/9b48b7bcfc3180ef74f4", verify=False).json()
    print(blog_data)
    app.run(debug=True)
