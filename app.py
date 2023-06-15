from flask import  Flask, render_template,request
import numpy as np
import pickle

app=Flask(__name__)


#route

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict_price():
    
    gen=request.form['Gender']
    if gen=='M':
       gen=1
    else:
       gen=1.0

    mar=request.form['Married']
    if mar=='Un':
       mar=0
    else:
       mar=1.0


    dep = request.form['Dependents']
    if dep == '0':
        dep = 0
    elif dep == '1':
        dep = 1
    elif dep == '2':
        dep = 2
    else:
        dep = 3


    edu=request.form['Education']
    if edu=='Grad':
       edu=1
    else:
       edu=0

    se=request.form['SEmp']
    if se=='Nse':
       se=0
    else:
       se=1

    inc =float(request.form['income'])
    coa=float(request.form['CoInc'])
    LoReq=float(request.form['LoReq'])

    LT=request.form['LTerm']
    if LT=='18M':
       LT= 480
    elif LT == '12M':
       LT = 360
    elif LT == '10M':
        LT= 300
    elif LT == '8M':
        LT= 240
    else:
       LT= 180

    ch=request.form['CrH']
    if ch=='ND':
       ch=1
    else:
       ch=0
    
    pa=request.form['PArea']
    if pa=='sub':
       pa= 1
    elif pa == 'urb':
       pa = 2
    else:
       pa= 0


   
    
    data = [np.array([gen, mar, dep, edu, se, inc, coa, LoReq, LT, ch, pa])]
    model = pickle.load(open('models/lr.pkl', 'rb'))

    #model = pickle.load(open('lr.pkl', 'rb'))

   

    result=np.round(model.predict(data))    
    if result == 1:
      msg = "Congratulations!! Your Loan application has been approved!"
    else:
      msg = "Sorry Your Loan application has been rejected."
    return render_template('index.html',prediction_value=msg)



if __name__=="__main__":
    app.run(debug=True)
    
    