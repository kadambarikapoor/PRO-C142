from flask import Flask, jsonify
from content_based_filtering import get_recommendations
from demographic_filtering import output
from storage import all_articles, liked_articles, unliked_articles


app = Flask(__name__)

@app.route('/article-data')
def home():
    return jsonify({
        'data': all_articles[0],
        'message': 'successful'
    }), 404

@app.route('/liked_articles', methods = ['POST'])
def liked():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        'message': 'successful'
    }), 404

@app.route('/unliked_articles', methods = ['POST'])
def unliked():
    article = all_articles[0]
    all_articles = all_articles[1:]
    unliked_articles.append(article)
    return jsonify({
        'message': 'successful'
    }), 404

@app.route('/popular-articles')
def demofilter():
    article = []
    for i in output:
        article.append({
            'title': i[12],
            'text': i[13],
            'url': i[11],
            'contentID': i[4],
            'language': i[14],
            'author_person_id': i[5],
            'total_events': i[15]
        })
    return jsonify({
        'data': article,
        'message': 'succesful'
    }), 404

@app.route('/recommended-articles')
def recommend():
    recommended_articles = []
    for j in liked_articles:
        recommendations = get_recommendations(j[4])
        for k in recommendations:
            recommended_articles.append(k)

    article = []
    for l in output:
        article.append({
            'title': l[12],
            'text': l[13],
            'url': l[11],
            'contentID': l[4],
            'language': l[14],
            'author_person_id': l[5],
            'total_events': l[15]
        })
    return jsonify({
        'data': article,
        'message': 'succesful'
    }), 404

if __name__ == '__main__':
    app.run()