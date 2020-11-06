#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from dbconnection import connect
from Queries import ALL_BOOKS, SPECIFIC_BOOK, INSERT_BOOK, UPDATE_BOOK
from Queries import DELETE_BOOK, ALL_AUTHORS, SPECIFIC_AUTHOR

book_post = reqparse.RequestParser()
book_post.add_argument('book_name', type=str, 
                        help='Name of book is required', required=True)
book_post.add_argument('description', type=str, 
                        help='Description of book is required', required=True)
book_post.add_argument('author_id', type=int, 
                        help='Author id is required', required=True)

app = Flask(__name__)
api = Api(app)

class Books(Resource):
    def get(self):
        # connect to database
        conn = connect()
        # This line performs query and returns json result
        query = conn.execute(ALL_BOOKS) 
        # Fetches all the rows
        return {'Books': [dict(zip(tuple (query.keys()) ,i)) 
                          for i in query.cursor]} 
    
    def post(self):
        book_post.parse_args()
        conn = connect()
        BookName = request.json['book_name']
        Description = request.json['description']
        AuthorId = request.json['author_id']
        authors_id_exist = len(conn.execute(SPECIFIC_AUTHOR.format(AuthorId))
                                                           .cursor.fetchall())
        if(authors_id_exist):
            try:
                conn.execute(INSERT_BOOK.format(BookName, Description, 
                                                AuthorId))
                return {'status': 'inserted'}
            except:
                return {'status': 'duplicate authors not allowed'}
        return {'status': " Author not present in the table"}

class Book_Id(Resource):
    def get(self, book_id):
        conn = connect()
        query = conn.execute(SPECIFIC_BOOK.format(book_id))
        result = {'Book': [dict(zip(tuple (query.keys()) ,i)) 
                           for i in query.cursor]}
        return jsonify(result)

    def put(self, book_id):
        conn = connect()
        BookName = request.json['book_name']
        Description = request.json['description']
        AuthorId = request.json['author_id']
        authors_id_exist = len(conn.execute(SPECIFIC_AUTHOR.format(AuthorId))
                                                           .cursor.fetchall())
        if(authors_id_exist):
            conn.execute(UPDATE_BOOK.format(BookName, Description, 
                                            AuthorId, book_id))
            return jsonify({'status': 'updated'})
        return {'status': "Author doesn't exist"}

    # Additional
    def delete(self, book_id):
        try:
            conn = connect()
            conn.execute(DELETE_BOOK.format(book_id))
            return jsonify({'status': 'deleted'})
        except:
            return jsonify({'status': 'error'})
    
class Authors(Resource):
    def get(self):
        conn = connect()
        query = conn.execute(ALL_AUTHORS)
        result = {'Authors': [dict(zip(tuple (query.keys()) ,i)) 
                              for i in query.cursor]}
        return jsonify(result)

api.add_resource(Books, '/books') # Route_1
api.add_resource(Book_Id, '/books/<book_id>') # Route_2
api.add_resource(Authors, '/authors') # Route_3

if __name__ == '__main__':
    app.run()