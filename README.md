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

1. Ensure Django is installed by running the following command in bash: `$ python3 -m django --version`
2. Clone the repository: `$ git clone https://github.com/gavin-robey/CarRentalService`
3. Enter the repository: `$ cd CarRentalService`
4. Make migrations by: `$ python3 manage.py makemigrations` 
5. Then migrate changes: `$ python3 manage.py migrate`
6. Launch Server: `$ python3 manage.py runserver`
7. Run server by visiting: http://127.0.0.1:8000/ 

## Testing data

To load in testing vehicle and reservation data, run the following commands:

```
python manage.py loaddata reservations_mock.json
python manage.py loaddata vehicles_mock.json
```


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
