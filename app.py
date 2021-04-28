import pandas as pd
import numpy as np
import os
import re
from flask import Flask, render_template, request, jsonify



path0=os.path.abspath(os.path.dirname(__file__))
#file_0=os.path.join(path0, 'list_tag_key_500.joblib')
#file_1=os.path.join(path0, 'reg_log_saved.joblib')



from pyresparser import ResumeParser
app = Flask(__name__) # Creer app et charger les fonctionalités de Flask

# Home page
@app.route('/') 
def index():
    return render_template('index.html')
                                                    
@app.route('/resume_parsing', methods=['POST'])
def Resume_parsing():
    
    # Appeler les Inputs de la page HTML dashboard
    question = request.form['question'] 
    link_resume = ''
    if question is not None:
        link_resume = str(path0+'\/'+question) 
        #link_resume=question
        resume_parsing = ResumeParser(link_resume).get_extracted_data()
    #return jsonify(resume_parsing)
          
    return render_template('resume_parsing.html', tags = resume_parsing)
                  

if __name__== '__main__': #Executer directement
    app.run(debug=True, port=5000) #Lancer le serveur local (localhost/adresse ip 127.0.0.1)



