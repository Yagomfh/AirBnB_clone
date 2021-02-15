# AirBnB clone

## What is it?

The goal of the project is to deploy on a server a simple copy of the AirBnB website. This project will not implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

**Main engineering features:**

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/d2d06462824fab5846f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210215%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210215T094552Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=78aeb588f53b01e242acf5471902da5ec525e4ea843a5d793a9bdd05407620d2)

## The console

**1) Download it:**

```
$ git clone https://github.com/Yagomfh/AirBnB_clone
```

**2) Run it:**

```
$ ./console.py
```

**3) Quit it:**

```
(hbnb) quit
or
(hbnb) EOF
```

## Commands featured in this console

You can check the list of commands and builtins of this shell by running `(hbnb) help`.

You can get a description of the command by running `help <command name>`.

## Examples

**Create a new instance of `User`**

```
(hbnb) create User
c1a6ffe1-fadb-4f91-a067-d555ea8f77ae
```

**Show string representation of a instance**

```
show User c1a6ffe1-fadb-4f91-a067-d555ea8f77ae
[User] (c1a6ffe1-fadb-4f91-a067-d555ea8f77ae) {'id': 'c1a6ffe1-fadb-4f91-a067-d555ea8f77ae', 'created_at': datetime.datetime(2021, 2, 15, 10, 10, 21, 996040), 'updated_at': datetime.datetime(2021, 2, 15, 10, 10, 21, 996056)}
```

**Update instance attributes**

```
(hbnb) update User c1a6ffe1-fadb-4f91-a067-d555ea8f77ae first_name Elon
(hbnb) update User c1a6ffe1-fadb-4f91-a067-d555ea8f77ae last_name Musk
(hbnb) show User c1a6ffe1-fadb-4f91-a067-d555ea8f77ae
[User] (c1a6ffe1-fadb-4f91-a067-d555ea8f77ae) {'first_name': 'Elon', 'id': 'c1a6ffe1-fadb-4f91-a067-d555ea8f77ae', 'created_at': datetime.datetime(2021, 2, 15, 10, 10, 21, 996040), 'last_name': 'Musk', 'updated_at': datetime.datetime(2021, 2, 15, 10, 10, 21, 996056)}
```

**Delete an instance**

```
(hbnb) destroy User c1a6ffe1-fadb-4f91-a067-d555ea8f77ae
(hbnb) show User c1a6ffe1-fadb-4f91-a067-d555ea8f77ae
** no instance found **
```

## Author

[Yago Martinez-Falero Hein](https://github.com/Yagomfh)
