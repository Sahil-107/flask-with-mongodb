from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask("app", template_folder=".")
client = MongoClient("mongodb+srv://admin:<password>@cluster0.gx5mz.mongodb.net/mydb?ssl=true&ssl_cert_reqs=CERT_NONE")
db= client.mydb
collections = db.collections

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/insert")
def insert():
    name=request.args.get('name')
    password=request.args.get('password')
    age=request.args.get('age')

    values={"name": name, "password":password, "age":age}
    
    collections.insert_one(values)
    return render_template("res.html", res="Records Inserted in Database")

@app.route("/update")
def update():
    password=request.args.get('password')
    new_name=request.args.get('new_name')
    new_age=request.args.get('new_age')

    query={"password":password}
    values={"$set":{"name":new_name, "age":new_age}}
    
    collections.update_one(query,values)
    return render_template("res.html", res="Records updated")

@app.route("/delete")
def delete():
    password=request.args.get('password')
    query={"password":password}    
    collections.delete_one(query)
    return render_template("res.html", res="Record deleted")

@app.route("/read")
def read():    
    records=collections.find()
    for record in records:
        name=record["name"]
    return render_template("res.html", res=name)
if __name__ == "__main__":
    app.run()