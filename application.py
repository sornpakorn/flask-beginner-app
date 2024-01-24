####### Start: Workshop 1 #######

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def test():
#     return "Sornpakorn.S is studying EES398"

####### End: Workshop 1 #######




####### Start: Workshop 2 #######

# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def home():
#    return render_template('index.html')

# @app.route('/result')
# def result():
#    return render_template('result.html')


# if __name__ == '__main__':
#    app.run()

####### End: Workshop 2 #######




####### Start: Workshop 3 #######

from flask import Flask, render_template, request
from googleapiclient.discovery import build

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with the actual API key you obtained from the Google Cloud Console
API_KEY = 'your API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.form.get('query')
    videos = youtube_search(query)
    return render_template('result.html', videos=videos)

def youtube_search(query):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Perform the search
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=10
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        video = {
            'title': search_result['snippet']['title'],
            'video_id': search_result['id']['videoId'],
        }
        videos.append(video)

    return videos

if __name__ == '__main__':
    app.run()

####### End: Workshop 3 #######