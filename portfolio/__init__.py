from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with python and mongodb",  # is what will be displayed on the homepage.
        "thumb": "img/habit-tracking.png",  # is the image shown on the homepage.
        "categories": ["python", "web"],  # are shown on the homepage.
        "hero": "img/habit-tracking-hero.png",  # is the image shown on each project page.
        "slug": "habit-tracking",  # is the URL which is unique to each project
        "prod": "https://udemy.com",
    },
    {
        "name": "Personal Finance tracking app with react",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
    },
    {
        "name": "REST API documentation with Postman and Swagger",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing"],
        "slug": "api-docs",
    },
]

slug_to_project = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])
