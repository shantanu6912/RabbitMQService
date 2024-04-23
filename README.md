# Project Name
   RabbitMQService

# Project Objective:
    Develop a backend system in Python that handles incoming MQTT messages via RabbitMQ and stores them in MongoDB. This project will test your ability to integrate MQTT messaging with RabbitMQ, process messages in Python, and efficiently store data in MongoDB.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation
* RabbitMQ Installation:
   - Make sure you install erlang before RabbitMQ.
1. Download RabbitMQ:
   - Visit the RabbitMQ download page: [RabbitMQ Download](https://www.rabbitmq.com/docs/download)
   - Choose the appropriate installer for your operating system.
2. Install RabbitMQ:
   - Follow the installation instructions provided on the RabbitMQ website or in the README file included with the download.
   - For Windows, run the installer and follow the installation wizard.
   - For macOS and Linux, follow the installation instructions provided for your specific distribution.
3. Start RabbitMQ:
   - After installation, RabbitMQ should start automatically.
   - Alternatively, you can start RabbitMQ manually using the appropriate command or script for your operating system.
4. Access RabbitMQ Management Console (Optional):
   - RabbitMQ comes with a web-based management console for managing RabbitMQ server, queues, exchanges, users, and more.
   - To access the management console, open a web browser and navigate to http://localhost:15672/.
   - Log in using the default credentials (username: guest, password: guest). You can change the password later from the management console.
5. Verify Installation:
   - Once RabbitMQ is installed and running, you can verify its status by accessing the management console or using command-line tools like rabbitmqctl (for macOS and Linux) or rabbitmq-service status (for Windows).

* MongoDB Installation:
1. Download MongoDB:
   - Visit the MongoDB download page:  [MongoDB Download Center](https://www.mongodb.com/try/download/community)
   - Choose the appropriate installer for your operating system.
2. Install MongoDB:
   - Follow the installation instructions provided on the MongoDB website or in the README file included with the download.
   - For Windows, run the installer and follow the installation wizard.
   - For macOS and Linux, follow the installation instructions provided for your specific distribution.
3. Start MongoDB:
   - After installation, you may need to start MongoDB manually.
   - For Windows, you can start MongoDB as a service using the Services management console (services.msc).
   - For macOS and Linux, you can start MongoDB using the appropriate command or script.
4. Access MongoDB Shell (Optional):
   - MongoDB provides a shell interface for interacting with MongoDB databases.
   - To access the MongoDB shell, open a terminal or command prompt and run the mongo command.
5. Verify Installation:
   - Once MongoDB is installed and running, you can verify its status by connecting to the MongoDB server using the MongoDB shell or a MongoDB client.

* Python libraries to be installed
  - pip install pika
  - pip install pymongo
  - pip install pypiwin32
  - pip install pyinstaller

## Usage
* Below Steps are for windows OS:

1. Clone the repo.
2. Open Command prompt and navigate to RabbitMQService directory of clonned repo and run below command.
3. pyinstaller.exe --hiddenimport win32timezone -F mqtt_service.py
4. After executing above command dist directory will get created in RabbitMQService.
5. mqtt_service.exe will be present in dist which will be the service executable file.
6. Download and extract nssm Featured pre-release via [MSSM Download](https://nssm.cc/download)
7. Open new command prompt as administrator and navigate to win64 directory in nssm download where nssm.exe is present.
8. Make sure your RabbitMQ server and mongoDB is connected.
9. Run below command to install the service:
   - nssm install RabbitMQService "file path of mqtt_service.exe file"
   - for ex: nssm install assignment2 "C:\Users\Dell\Desktop\RabbitMQService\dist\mqtt_service.exe"
10. Run below command to start the service:
   - net start assignment2
11. Run below command to check if service is running.
   - sc query assignment2 

# Project Working 

* After Above steps your service it  ready to subcribe rabbitMQ messages on topic "devices/data".
* A file named publish.py is given in repo to publish messages through RabbitMQ.
* if {"type": "retrive"} is the message publish then all mongo db data will be retrived from database and stored in log file.
* Log file is stored in logs folder of dist folder.
* if "LIGHT" present in id of received message then message is transformed and stored in DB.






