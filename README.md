[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/wTBA-Etm)


# File Manager : clean code and error handling

File Manager is a simple and fast API developped by the **BugHunters**, which allows you to manage files, either on the cloud or locally. It depends on your base configuration, it's up to you.

## Who are the BugHunters ? 
___BugHunters___ is a group of junior IT developers who are part of the HEI Tribute. Here are the members : 
- Mihary Joël : [miharyjoe](https://github.com/MiharyJoe) - STD21004
- RAFALIMANANA Rojotiana Nomena : [Noums26](https://github.com/Noums26) - STD21007
- RAKOTOMAHEFA Fanomezana Sarobidy : [Sarobidy-23](https://github.com/Sarobidy-23) - STD21011
- RANDRIAMANGA Iloniavo : [Iloniavo](https://github.com/Iloniavo) - STD21020
- RAZANAPANALA Tsirimaholy : [Tsirymaholy](https://github.com/Tsirimaholy) - STD210XX


## What's the purpose ?
File Manager supports four types of files extensions : 
- words : .docx, .txt, ...  
- images : .jpeg, .png
- videos : .mp4, .mkv, .ts
- pdf : .pdf

**Each file is filed in the corresponding folders**.

There are two different implementations with different programming language : 
- Python : with Django framework [here](https://github.com/hei-school/cc-hei-hub-bughunter/tree/feature/python)
- Java : with Spring Boot framework - [here](https://github.com/hei-school/cc-hei-hub-bughunter/tree/feature/java)
You can find in each branch how to set up the API.

## What are the error we want to handle ? 
- FileNotFound : 404
- BadFileType : 400
- TooManyRequest : 429
- RequestTimeOut : 408
- FileTooLarge : 423
- NotImplemented : 501
- ServerError : 500
- DuplicatedFile : 100
- CorruptedFile : 500
- LockException : 423
- LegalReason : 453
- FilenameInvalid : 400
- SensitiveFile : 400
- NotAuthorized : 401

