# AirBnB Clone - Command Interpreter

This is the first step towards building a full-stack clone of the AirBnB web application. The goal of this project is to create a command-line interpreter that can manage various objects like users, places, cities, and more. This command interpreter serves as a foundation for managing data and will be used in future projects to extend the application with HTML/CSS, API development, and database integration.

## Command Interpreter

The command interpreter is a shell-like tool designed for managing AirBnB objects.

### How to Start It

Run the following command in your terminal:
```bash
./console.py

```

This will start an interactive command prompt where you can type commands to manage your objects.

## How to Use It

Once inside the command interpreter, you can perform the following actions:

- **Create an object**: 
  - This command creates a new instance of a class.
  - Syntax:
    ```bash
    (hbnb) create <ClassName>
    ```

- **Show an object**:
  - This command retrieves the string representation of an instance based on the class name and ID.
  - Syntax:
    ```bash
    (hbnb) show <ClassName> <object_id>
    ```

- **Update an object**:
  - This command updates the attributes of an instance based on the class name, ID, and attribute name and value.
  - Syntax:
    ```bash
    (hbnb) update <ClassName> <object_id> <attribute_name> <attribute_value>
    ```

- **Delete an object**:
  - This command deletes an instance based on the class name and ID.
  - Syntax:
    ```bash
    (hbnb) destroy <ClassName> <object_id>
    ```

- **Exit the interpreter**:
  - This command exits the command interpreter.
  - Syntax:
    ```bash
    (hbnb) quit
    ```

### Examples

```bash
$ ./console.py
(hbnb) create User
(hbnb) show User 1234-5678-9012
(hbnb) update User 1234-5678-9012 name "John Doe"
(hbnb) destroy User 1234-5678-9012
(hbnb) quit
$
