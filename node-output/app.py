from flasgger import Swagger
from flask import Flask, jsonify, request
import mail_sender
import jd_generation
app = Flask(__name__)
swagger = Swagger(app)
# returns the data that we send when we use POST.
@app.route('/send_mail', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})
    elif request.method == "POST":
        json_data=request.get_json(force=True)
        print(json_data)
        return mail_sender.send_mail(json_data)
@app.route("/generate_jd",methods=['POST'])
def generateJD():
     json_data=request.get_json(force=True)
     prompt="Generate a 100 sentence job description for a user experience designer with the following characteristics:\nCompany - "+json_data['company']+"\nlocation - "+json_data['location']+"\nEducation - "+json_data['education']+"\nExperience - "+json_data['experience']+"\nRequired Skills - "+json_data['skills']+"\n\n"
     return jd_generation.generat(prompt)
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)
