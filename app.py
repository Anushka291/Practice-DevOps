from flask import Flask, request,render_template
app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def register():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        event=request.form["event"]

        if email=="anu@gmail.com":
            return f"""
            <h2>Registration Successful"</h>
            <p>Name:{name}</p>
            <p>Email:{email}</p>
            <p>Event:{event}</p>
            """
        else:
            return "Cannot register!"
    return render_template("index.html")

if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
