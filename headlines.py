import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}


@app.route("/")
#@app.route("/<publication>")
def get_news(): #get_news(publication="bbc"):
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
           publication ="bbc"
    else:
           publication =query.lower()

    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries']#[0]
    return render_template("home.html",articles=first_article
                           #title=first_article.get("title"),
                           #published=first_article.get("published"),
                           #summary=first_article.get("summary")
 )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
