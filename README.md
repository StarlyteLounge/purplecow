# Purple Cow Project
As part of a larger project, there needed to be a proof-of-concept microservice that accepted JSON data to identify and catalog people. Each person would be given an unique ID that is associated with their name.

## Install and Run
### Install
Installation is as simple as cloning or exporting this git repository. As this is a very simple POC project, there aren't many files and they should all reside in the same directory.
```console
$ git clone https://github.com/StarlyteLounge/purplecow.git
```
Python 3.7 or newer must be installed and used for this app. Flask 2.1 is required as well, use pip to install it.
```console
$ sudo apt update && sudo apt install -y python3-pip # if not yet installed
$ pip install Flask
```
### Run
After the files have been downloaded and Flask has been installed, the microservice can be started from the command line.
#### MacOS/Linux/Windows WSL
Launch the microservice from the command line:
```console
$ python3 ppc.py
```

Alternatively, you can make ppc.py executable, and launch it directly:
```console
$ chmod +x ppc.py
$ ./ppc.py
```
#### Windows
tbd
## Configuration
Configuration is limited to hostname and port. These are provided in the settings.cfg file. A restart of the microservice is required before a configuration change is seen in a running microservice. A second microservice can be launched on a different port by editing the settings.cfg file and starting up a new one from the command line.
## Use
The microservice responds to http requests in order to maintain the database of people.
The `/items` endpoint is the only valid endpoint.

Implemented http verbs:
- **POST** is used to populate the database. When POSTing to `/items`, pass a JSON list of dictionaries in the body. An example:

```
[
    {
        "id": 1001,
        "name": "Mary"
    },
    {
        "id": 1002,
        "name": "John"
    },
    {
        "id": 1003,
        "name": "Jane"
    }
]
```

would cause 3 entries in the database, one for Mary, one for John, and one for Jane.
The http response is "post complete" if the request is successful.

- **GET** retrieves the entire database as a JSON string, identical in nature as the example above. The http response is the JSON string when successful.

If the database is empty, the http response is "no people".

- **DELETE** removes all entries from the database. The http response is "the database has been cleared" if the request is successful.

