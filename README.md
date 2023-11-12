# Overview

I developed a Contact Management System as part of my ongoing journey as a software engineer to enhance my skills and understanding of cloud-based applications. The system allows users to perform basic operations like adding, deleting, and displaying contacts. The application integrates with a Cloud Database, specifically Firebase Firestore, to persistently store contact information.

The purpose of this software is to create a simple yet functional contact management system that leverages a cloud database for data storage. This project aims to demonstrate the integration of a Python application with Firebase Firestore and showcase basic CRUD (Create, Read, Update, Delete) operations.

[Software Demo Video](https://www.youtube.com/watch?v=qt5vADP1sQQ)

# Cloud Database

I utilized Firebase Firestore as the cloud database for this project. Firestore is a NoSQL document-oriented database that seamlessly integrates with Firebase projects. It provides real-time synchronization and scalable storage for structured data.

The database consists of a single collection named "Persons", where each document represents a contact. The documents are identified by the first name of the contact, and each document contains fields such as First Name, Last Name, Email, and Phone.

# Development Environment

- __Language:__ Python

- __Tools:__ Firebase, Visual Studio Code

- __Libraries:__ ``firebase_admin`` for Firebase integration, ``os`` to clear the terminal screen, and ``time`` to pause execution

# Useful Websites

- [Firestore Documentation](https://firebase.google.com/docs/firestore/quickstart#python_5)
- [YouTube](https://www.youtube.com/watch?v=b4W3YQdViTI&t=656s)
- [Python Firestore Documentation](https://cloud.google.com/python/docs/reference/firestore/latest/index.html)

# Future Work

- Implement user authentication to secure the contact data.
- Enhance the user interface for a more user-friendly experience.
- Explore additional features such as and sorting and connecting contacts.