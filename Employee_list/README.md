#Employee_list

- Employee List is an application that allows users to create, delete or edit employee details.
- Employee List displays the following information about employees:
  - Name
  - Surname
  - Job Title
  - Date started at company
  - Short Job Description
  - Photo
- Employee List should be able to sort by column headers mentioned above.
 
### How to run Employee_list
- Open your terminal and create your virtual environment using python3.
- 'cd' to your virtual environment and activate it: 
  *source virtual_environment_name/bin/activate*
- Now that your virtual environment is activated get back to the directory 'Employee_list'.
- Install the requirements.txt by running: 
  *pip install -r requirements.txt*
- You need to open your Postgresql and create a database with name "employee_list_db" then exit Postgresql.
- Link your database that you just created to your settings then run:
  *python manage.py makemigrations employee* *python manage.py migrate* this will import all the initial migrations to your project.
- You can access the administration of the application by:
 *python manage.py createsuperuser* you will be prompted to enter your admin username and password. You now have access to the admin site of the project.
- To verify that your project has been created successfully run: 
  *python manage.py runserver*, 
  the server will run at *http://127.0.0.1:8000/* in your browser.
- You can exit the server by:
  *Control+C*

####Contributors

    Thanduxolo Tshiba <thandu@byteorbit.com>

####License & copyright

© Thanduxolo L Tshiba

You are free to copy, modify, and distribute