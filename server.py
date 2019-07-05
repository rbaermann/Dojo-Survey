from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():
    print('Got Post Info')
    print(request.form)
    name_from_form = request.form['name']
    loc_from_form = request.form['Dojo_Location']
    lang_from_form = request.form['Favorite_Language']
    comment_from_form = request.form['comment']
    return render_template('show.html', name_on_template=name_from_form, loc_on_template=loc_from_form, lang_on_template=lang_from_form, comment_on_template=comment_from_form)


if __name__ == '__main__':
    app.run(debug = True)