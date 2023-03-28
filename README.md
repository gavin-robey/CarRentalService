# Dan's Rental Car

This app allows customers to rent a car from the conviencience of their laptop. It also helps manage employees and inventory of *Dan's Rental Car*.

## Workspace layout

*Dan's Rental Car* is a web app that will be stored in this repository. 

All code pertaining to this project is stored in the "CarRentalService" directory with exception to this README file, the .gitignore file, and "manage.py".

All documentation including the Project plan, Use Case Diagrams, Activity diagrams, Class diagrams, Prototypes, and Requirements Definition are stored in the "docs" folder.

## Version-control procedures

Each collaborator will fork and clone this repository to their own *github* account. Whenever changes must be made to the repository, each collaborator will send a pull request to ensure any issues are montitored and controlled. 

## Tool stack description and setup procedure

Our project uses django which helps automatically organize our tool stack. This will include: an SQLite database managed by python scripts, python for backend management, Javascript, HTML, and CSS. 

## Build instructions

1. Ensure both Django and Python are installed by running the following commands in bash: 
```terminal
python3 --version 
```
```
python3 -m django --version
```
2. Install Node.js
  * Download the installer from [NodeJS WebSite](https://nodejs.org/en).
  * Run the installer.
  * Follow the installer steps, agree the license agreement and click the next button.
  * Restart your system/machine.
3. Ensure both Node.js and npm are installed:
```
node -v
```
```
npm -v
```
4. Install pip:
```
python3 get-pip.py
```
5. Clone the repository: 
```
git clone https://github.com/gavin-robey/CarRentalService
```
6. Enter the repository: 
```
cd CarRentalService
```
7. Install Tailwind CSS 
  * Install the django-tailwind package via pip
  ```
  python3 -m pip install django-tailwind
  ```
  * Install Tailwind CSS dependencies, by running the following command
  ```
  python3 manage.py tailwind install
  ```
8. Install Pillow
```
python3 -m pip install --upgrade Pillow
``` 
9. Make migrations by: 
```
python3 manage.py makemigrations
```
10. Then migrate changes: 
```
python3 manage.py migrate
```
11.  load in testing vehicle and reservation data:
```
python manage.py loaddata reservations_mock.json
python manage.py loaddata vehicles_mock.json
```
12. Launch Server: 
```
python3 manage.py runserver
```
13. Run server by visiting: http://127.0.0.1:8000/ 


## Unit Testing Instructions

To test all unit tests in the project run the following command:

```
python manage.py test
```

To test all tests associated with the Reservation Object, run the following command:

```
python manage.py test reservation

```

## System Testing Instructions

Once the app is built, the system can be tested by visiting http://127.0.0.1:8000/ in a browser. Login to the web app using the following credentials. Username: SystemTest, Password: systest. This login will allow access to all actions as a customer, till employee, manager, and retrieval specialist in a test environment. This feature is not built yet, but once the project is implemented it will become available. 

## Other development notes, as needed

Development notes will be added as development continues.
