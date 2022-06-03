from flask import Flask, render_template, request
import requests


# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "dtEJtUBwh-4FQHs46Ph-mq8d9VTPBNvgIfLIAMPDUMe8"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/predict", methods= ['POST'])
def predict():
    id = request.form['id']
    cycle = request.form['cycle']
    setting1 = request.form['setting1']
    setting2 = request.form['setting2']
    setting3 = request.form['setting3']
    
    s1 = request.form['s1']
    s2 = request.form['s2']
    s3 = request.form['s3']
    s4 = request.form['s4']
    s5 = request.form['s5']
    s6 = request.form['s6']
    s7 = request.form['s7']
    s8 = request.form['s8']
    s9 = request.form['s9']
    s10 = request.form['s10']
    s11 = request.form['s11']
    s12 = request.form['s12']
    s13 = request.form['s13']
    s14 = request.form['s14']
    s15 = request.form['s15']
    s16 = request.form['s16']
    s17 = request.form['s17']
    s18 = request.form['s18']
    s19 = request.form['s19']
    s20 = request.form['s20']
    s21 = request.form['s21']
    
    input_value_temp = [[float(id), float(cycle), float(setting1), float(setting2), float(setting3), float(s1), float(s2), float(s3), float(s4), float(s5), float(s6), float(s7),float(s8), float(s9),float(s10),float(s11),float(s12),float(s13),float(s14),float(s15),float(s16),float(s17),float(s18),float(s19),float(s20),float(s21)]]
    
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": [["f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13","f14","f15","f16","f17","f18","f19","f20","f21","f22","f23","f24","f25"]], "values": input_value_temp }]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/8fd4abc3-1277-4751-af1d-bd2ced281393/predictions?version=2022-06-03', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    
    pred = response_scoring.json()
    output = pred['predictions'][0]['values'][0][0]
    result_text = "Maintenance Required!! Expected a failure within 30 days."

    if(output == 0):
        result_text = "No failure expected within 30 days."
    
    

    return render_template('index.html',result=result_text)


# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)