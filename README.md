# todolist-django

Users can create an account and then add, update, and delete their tasks. They also have the possibility to view all details of each task.

## Installation

In order to run the project on your local machine, you must follow these steps:

1. Install Python version 3.11
   ([Python](https://www.python.org/downloads/))

   If you already have installed IDE, which support python you can skip this step, but if not install IDE (for example, PyCharm) 



2. Clone the repository 



3. To install all necessary libraries in the project terminal, type in:
```bash
pip install -r requirements.txt
```
* Also you can provide initial data by type in:
```bash
python manage.py loaddata task.json
```


4. I strongly recommend using a specific virtual environment for this project. You can create one by typing the following command: 
```bash
python -m venv <name-of-your-enviroment> 
```
* Activate the virtual environment:

Windows
```bash
.\env\Scripts\activate
```
macOS/Linux
```bash
source env/bin/activate
```
* And add them by accessing the interpreter settings and selecting the file from 
the folder where we created our virtual environment (name-of-your-environment -> Scripts -> python.exe).



5. If you have completed all the steps, you can run the project by typing the following command into your terminal:
```bash
python manage.py runserver 
```
* And type into your browser ' http://127.0.0.1:8000 '
