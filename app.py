from flask import Flask, render_template

app = Flask(__name__)

MANHWA = [
   {
      'title': 'Solo Leveling',
      'author': 'Chugong',
      'genre': 'Action, Fantasy, Martial Arts',
      'rating': 9.5,
      'image': '/static/solo-leveling.jpg',
      'link' : 'https://kunmanga.com/manga/solo-leveling/'
   },
   {
      'title' : 'Eat and Go',
      'author' : 'Jung Seung Wook',
      'genre' : 'Comedy, Fantasy, Martial Arts',
      'rating' : 9.5,
      'image' : 'https://kunmanga.com/wp-content/uploads/2025/05/Eat-and-Go-193x278.jpg',
      'link' : 'https://kunmanga.com/manga/eat-and-go/'
   },
   {
      'title' : 'The Beginning After The End',
      'author' : 'Tae Joon Park',
      'genre' : 'Action, Fantasy, Martial Arts',
      'rating' : 9.5,
      'image' : 'https://kunmanga.com/wp-content/uploads/17-1583497020-3544-193x278.jpg',
      'link' : 'https://kunmanga.com/manga/the-beginning-after-the-end/'
   },
   {
      'title' : 'The Beginning After The End',
      'author' : 'Tae Joon Park',
      'genre' : 'Action, Fantasy, Martial Arts',
      'rating' : 9.5,
      'image' : 'https://kunmanga.com/wp-content/uploads/17-1583497020-3544-193x278.jpg',
      'link' : 'https://kunmanga.com/manga/the-beginning-after-the-end/'
   }
]

@app.route('/')
def hello_manhwa():
   return render_template('gallery_view.html', 
                          manhwas=MANHWA)

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)

