from flask import Flask, render_template, request
import pymysql.cursors

app = Flask(__name__)

# Define a route to display the data
@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        # Connect to the database
        connection = pymysql.connect(
            host='aws.capwuc2kdl0e.ap-northeast-1.rds.amazonaws.com',
            user='admin',
            password='12345678',
            db='mydatabase',
            charset='utf8mb4',
            connect_timeout=30,
            cursorclass=pymysql.cursors.DictCursor
        )

        if request.method == 'POST':
            # Delete a record from the database
            person_id = request.form['person_id']
            with connection.cursor() as cursor:
                sql = f"DELETE FROM person WHERE id={person_id}"
                cursor.execute(sql)
            connection.commit()

        with connection.cursor() as cursor:
            # Retrieve the data from the database
            sql = "SELECT * FROM sensor"  # replace 'mytable' with the name of your table
            cursor.execute(sql)
            result = cursor.fetchall()

            # Render the data in a HTML template
            return render_template('index.html', data=result)

    except Exception as e:
        return str(e)
    finally:
        # Close the database connection
        connection.close()

# Run the app and the data update thread
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
