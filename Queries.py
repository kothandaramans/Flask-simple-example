ALL_BOOKS = "SELECT bo.book_id, bo.book_name, au.author_name, au.country, bo.description FROM Books bo INNER JOIN Authors au ON bo.author_id = au.author_id;"

SPECIFIC_BOOK = "SELECT bo.book_name, au.author_name, au.country, bo.description FROM Books bo INNER JOIN Authors au ON bo.author_id = au.author_id AND bo.book_id = {0};"

INSERT_BOOK = "INSERT INTO Books VALUES(null,'{0}','{1}',{2});"

UPDATE_BOOK = "UPDATE Books SET book_name='{0}', description='{1}', author_id='{2}' where book_id = {3};"

DELETE_BOOK = "DELETE FROM Books WHERE book_id = {0};"

ALL_AUTHORS = "SELECT * FROM Authors;"

SPECIFIC_AUTHOR = "SELECT * FROM Authors WHERE author_id = {0};"