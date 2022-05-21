# Kim's Feedback Forms
### By Maureen Mwangi. 
+ [Description](#Description)
+ [Installation process](#installation-process)
+ [Technologies used](#technologies-used)
+ [Known-Bugs](#known-bugs)
+ [Contact Information](#contact-information)
+ [Collaborators](#collaborators)
+ [Copyright and License](#copyright-and-license-information) 

## Description
this is a feedback form to give to your clients or add to your website so that they can give you their opinion on your service.<br>
Continuous feedback from your clients will help you to improve your services and thereby land more clients.<br>
The following is a live link to the project:
[Live link](https://kim-feedback.herokuapp.com/)
## Installation process
To access my repository link:
`https://github.com/maureen-james/Kim-s-feedback-form.git`

*To clone this repository locally, type the following command on your terminal.*

If using HTTP keys, type:

`https://github.com/maureen-james/Kim-s-feedback-form.git`


If using SSH keys, then type:

`git@github.com:maureen-james/Kim-s-feedback-form.git`

On running the commands successfully, you should have a local version of this repository.
Navigate to the target directory and open it with a prefered IDE :

Firstly;
1. Create a virtual environment by running the following command:

    `python3 -m  venv virtual`

    To install all stable dependencies used to run the application:

    `pip install -r requirements.txt`

    Activate the virtual environment by:

    `source virtual/bin/activate`

    And run the application from the virtual environment
    
2. Create a database of your choice and change the configurations in the config.py file.
3. Make and update database migrations to determine the tables schema.

4. On running the application, type the following on the terminal;
+ `chmod a+x start.sh`
Then type
`./start.sh`
5. To test the application;
+ `python3.8 manage.py test`

6. To navigate to a local browser, Type this on a preferred browser:
+ `127.0.0.1:5000`

## Technologies used
* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)
## Known-Bugs
No bugs identified during build.
## Contact information
+ Author E-mail ; `maureen.mwangi@student.moringaschool.com`
+ Phone Number: +254 711861542.
## Collaborators
+ [Ajedidah Mwanzia](https://github.com/AjedidahMwanzia)
+ [Kimberly Olanga](https://github.com/kim-olanga)
+ [Williams Oditi](https://github.com/Williamsoditi)
## Copyright and License
[MIT LICENSE](https://github.com/maureen-james/Kim-s-feedback-form/blob/main/LICENSE)

