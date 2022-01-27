from flask import Flask, escape,request,render_template
import pickle
import pickle as pickle

vector=pickle.load(open("vectorizer.pkl",'rb'))
model=pickle.load(open("finalized_model.pkl",'rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method=="POST":
        news=str(request.form['news'])
        print(news)
        predict=model.predict(vector.transform([news]))[0]
        print(predict)
        return render_template("predicton.html",prediction_text="New headline is -> {}".format(predict))

    else:
         return render_template("prediction.html")
    
       
if __name__=='_main_':
    app.run()