# [Listit Backend](backend-listit.herokuapp.com) v1.0.0
Listit Backend is responsible to provide json data to function list items app.

### Post Request

Create New Employee:
```sh
$ curl -X POST -d '{"email":"sakib3@gmail.com","password":"12323"}' http://localhost:5000/api/v1/employees/ --header "Content-Type:application/json"
```
Create New Product:
```sh
$ curl -X POST -d '{"name":"milk","family":"liquid"}' http://localhost:5000/api/v1/products/ --header "Content-Type:application/json"
```
### Created by
[Sabbir Rahman Sakib]()