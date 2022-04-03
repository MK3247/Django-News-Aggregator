# Django News Aggregator

**Link**: [AllNewx](https://allnewx.herokuapp.com/)

![image](https://github.com/MK3247/Django-News-Aggregator/blob/main/Home.png)

## Motivation 

This project was motivated by the need to create a web application that consolidates the latest news updates across the globe into one place. Today, news updates are released almost every minute. However, this information is scattered all over the world. As a result, it is overwhelming and time-consuming to visit different news sites to get all these updates. This web application aims at reducing this hustle by gathering the latest news updates from leading news websites across the world into one place.

## Built With

* [Python 3.9.11](https://www.python.org/) - Programming Language 
* [Django](https://www.djangoproject.com/) - Framework Used
* [Bootstrap](https://getbootstrap.com/) - Frontend 
* [NewsAPI](https://newsapi.org/) - The API used to collect news from various sites

## Feature

- Aggregates the latest news updates from news sites across the world.

## Code Example

```python
for i in range(len(l)):
    f = l[i]
    news.append(f['title'])
    url.append(f['url'])
```
 
 ## Prerequisites
  
 What things you need to install, the software, and how to install them
 
 * **python 3**
 
 Linux:
 
```
 sudo apt-get install python3.9.11
```
 Windows:
 
 You can get it from [python.org](https://www.python.org/downloads/windows/)
 
 Mac OS:
 
 ```
 brew install python3
 ```
 
 * **pip**
 
 Linux and Mac OS
 
 ```
 pip install -U pip
 ```
 Windows:
 
 ```
 python -m pip install -U pip
 ```
* **news-api**

```
pip install newsapi-python
```

## Installation

Clone this repository

```
git clone https://github.com/MK3247/Django-News-Aggregator.git
```

Open the folder

```
cd Django-News-Aggregator
```

Install all the requirements

```
python -m pip install -r requirements.txt
```

## Running the demo

```
python manage.py runserver
```

## Contributions

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Bug / Feature Request

In case you find a bug, kindly open an issue [here](https://https://github.com/MK3247/Django-News-Aggregator/issues/new). Include your query and your expected results.

## Author 

* **[Charles Wafula](https://https://github.com/MK3247)** 

[![github follow](https://img.shields.io/github/followers/MK3247?label=Follow_on_GitHub)](https://github.com/MK3247)
[![twitter follow](https://img.shields.io/twitter/follow/codeveterun?style=social)](https://twitter.com/codeveterun)

## Credits 

- [Data Flair](https://data-flair.training/blogs/django-project-ideas/) - Reference
- [GeeksforGeeks](https://www.geeksforgeeks.org/fetching-top-news-using-news-api/?ref=lbp) - Reference

