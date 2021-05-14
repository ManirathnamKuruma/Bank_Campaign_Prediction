from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import sklearn
app = Flask(__name__)
model = pickle.load(open('log_reg_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        job=request.form['job']
        if (job == 'blue-collar'):
            job = 9732
        elif (job == 'management'):
            job = 9458
        elif (job == 'technician'):
            job = 7597
        elif (job == 'admin'):
            job = 5171
        elif (job == 'services'):
            job = 4154
        elif (job == 'retired'):
            job = 2264
        elif (job == 'self-employed'):
            job = 1579
        elif (job == 'entrepreneur'):
            job = 1487
        elif (job == 'unemployed'):
            job = 1303
        elif (job == 'housemaid'):
            job = 1240
        elif (job == 'student'):
            job = 938
        else:
            job = 288
        marital=request.form['marital']
        if (marital == 'married'):
            marital = 27214
        elif (marital == 'single'):
            marital = 12790
        else:
            marital = 5207
        education=request.form['education']
        if (education == 'secondary'):
            education = 23202
        elif (education == 'tertiary'):
            education = 13301
        elif (education == 'primary'):
            education = 6851
        else:
            education = 1857
        default=request.form['default']
        if (default == 'yes'):
            default = 815
        else:
            default = 44396
        balance=int(request.form['balance'])
        housing = request.form['housing']
        if (housing == 'yes'):
            housing = 25130
        else:
            housing = 20081
        loan = request.form['loan']
        if (loan == 'yes'):
            loan = 7244
        else:
            loan = 37967
        contact = request.form['contact']
        if (contact == 'cellular'):
            contact = 29285
        elif (contact == 'unknown'):
            contact = 13020
        else:
            contact = 2906
        day = int(request.form['day'])
        month = request.form['month']
        if (month == 'jan'):
            month = 1403
        elif (month == 'feb'):
            month = 2649
        elif (month == 'mar'):
            month = 477
        elif (month == 'apr'):
            month = 2932
        elif (month == 'may'):
            month = 13766
        elif (month == 'jun'):
            month = 5341
        elif (month == 'jul'):
            month = 6895
        elif (month == 'aug'):
            month = 6247
        elif (month == 'sep'):
            month = 579
        elif (month == 'oct'):
            month = 738
        elif (month == 'nov'):
            month = 3970
        else:
            month = 214
        duration = int(request.form['duration'])
        campaign = int(request.form['campaign'])
        pdays = int(request.form['pdays'])
        poutcome = request.form['poutcome']
        if (poutcome == 'unknown'):
            poutcome = 36959
        elif (poutcome == 'failure'):
            poutcome = 4901
        elif (poutcome == 'other'):
            poutcome = 1840
        else:
            poutcome = 1511

        prediction=model.predict([[age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,poutcome]])
        output=prediction[0]


        if output==0:
            return render_template('index.html',prediction_text="The customer is not interested in subscription")
        else:
            return render_template('index.html',prediction_text="The customer is interested in subscription")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

