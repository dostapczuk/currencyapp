# CurrencyApp

##Overview
CurrencyApp is an Django and Django Rest Framework based web app that lets the user check the latest currency rates for every currency 
included RSS from https://www.ecb.europa.eu/home/html/rss.en.html. Logged users can follow currency and get notifications
when rate changes. Additionally user is able to see historical rates of followed currency.

##Quickstart
To run app you need to install all requirements included in requirements.txt

    pip install -r requirements.txt

Make sure that your OS is configured to work with Docker and Docker-compose.

##Run server
To run server use this command inside docker-compose.yml directory:

    docker-compose up

##API
To check rate of given currency using API endpoint:

    /currency/<short-currency-name>/

To check historical rates of given currency using API endpoint:

    /currency/<short-currency-name>/history/
    
##Web App
To follow currency you need to select it on user info edit form which is available on:

    /user/edit/
    
To see historical and current rates of followed currency enter the home page which is under:

    /home/

##Contributors
Daria Ostapczuk @dostapczuk 