from flask import Flask,jsonify,request

app=Flask(__name__)

book_db=[
    {
        'name':'secret',
        'price':250
    },
    {
        'name': 'deep dark ',
        'price': 350

    }
]
# get all book
@app.route('/book')
def get_all_book():
    return book_db


@app.route('/book/<string:name>')
def get_book(name):
    for book in book_db:
        if book['name'] == name:
            return jsonify(book)

    return jsonify({'book not found'})
# create a book
@app.route('/book',methods=['POST'])
def create_book():
    body_data=request.get_json()
    book_db.append(body_data)

    return jsonify({'massage':'book is creaed'})


app.run(port=5000)