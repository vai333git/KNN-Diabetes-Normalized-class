from flask import Flask,render_template,jsonify,request

from Project_app.utils import Diabetes

app = Flask(__name__)

######################################################################
############################## BASE / HOME API #######################
######################################################################

@app.route('/')
def Home_API():
    print('Welcome to the Home API')
    return render_template('index.html')

############################## SUBMIT API ##########################

@app.route('/submit',methods = ['POST','GET'])
def submit():   
    
    if request.method == 'POST':
        
        Glucose   = float(request.form['Glucose'])       
        BloodPressure    = float(request.form['BloodPressure'])
        SkinThickness   = float(request.form['SkinThickness'])
        Insulin    = float(request.form['Insulin'])
        BMI    = float(request.form['BMI'])
        DiabetesPedigreeFunction    = float(request.form['DiabetesPedigreeFunction'])
        Age    = float(request.form['Age'])
        

    db = Diabetes(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    Outcome = db.get_predicted_outcome()
    
    # return jsonify({'Result':f'The Logistic Model has Predicted the Outcome  of the test data as: {Outcome}'})
    return render_template('result.html',result = Outcome)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 9090)        
