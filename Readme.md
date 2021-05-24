
### Project Layout

i) (Question 1)[./question_1.py] 

ii) (Question 2)[./question_2.py] 

iii) (Question 1 Test)[./question_1_test.py] 

iv) (Question 2 Test)[./question_2_test.py] 

v) (Pipfile)[./Pipfile] - Contains Env setup



### Env Setup
I'm using Pipenv to setup virtual environment.

To run the environment:

``pipenv shell``

### Update Environment

To update the environment, run:

``pipenv --python 2.7``

or 


``pipenv --python 3.8``


### Tests

I'm using pytest to write the tests.

To run all the test (in project folder run):

``pytest``

To run individual test:

``pytest question_1_test.py``
