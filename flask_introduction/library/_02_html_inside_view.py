"""In this example, we're returning valid HTML code.

If you open this example in your browser, you'll see the page rendered
nicely as a real HTML page. That means that Flask took care of returning
to the client the `Content-Type: 'text/html'`.

**TODO**
Use the list of authors present in the `hello_world` view to
return a <ul> HTML tag containing the authors in the list.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    html = """
        <html>
            <h1>Welcome to our Library!</h1>
            <ul>
            {authors_ul}
            </ul>
        </html>
    """

    listofauthors = ""
    authors = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]
    for author in authors:
        listofauthors += "<li>"+author+"</li>"
    # build an <ul> with authors
    return html.format(authors_ul=listofauthors)
