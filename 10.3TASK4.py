import sqlite3
def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = ?;"
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()
    conn.close()
    return result

user_input = input("Enter user ID: ")
print(get_user_data(int(user_input)))