"""
Configuration of syllabus server.
Edit to fit development or deployment environment.

"""
import random 

### My local development environment
#PORT=5000
#DEBUG = True

### On ix.cs.uoregon.edu
#PORT=random.randint(5000,8000)
PORT=8880
SERVER_NAME = "ix.cs.uoregon.edu:{}".format(PORT)
DEBUG = False # Because it's unsafe to run outside localhost
