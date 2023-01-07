### Project Summary: This project involves building a web scraper that extracts information about towns in New Jersey from Wikipedia. The scraper will specifically target data points such as the names of colleges located in each town, the population size, and the land and water areas. The collected information will be processed and stored by the scraper. Once the data has been scraped and organized, it will be displayed to the user through a Django-powered web application. The purpose of this project is to provide a simple and convenient way for users to access and view information about towns in New Jersey, with the data being sourced from Wikipedia.

[X] Milestone 1: Intro & Getting Used to `mysql-connector`
  - Set up remote MySQL via VSCode 
  - Learn how to connect to mysql DB with python `mysql-connector`
  - Pull requests

[X] Milestone 2: Getting Used to Beautiful Soup & Backend 
  - Scrape Info on towns in NJ from Wikipedia
  - Scrape Colleges (private, public, & for-profit) in NJ from Wikipedia
  - Pull requests
  
[X] Milestone 3: Frontend
  - Set up Django developement environment
  - Create a model for the `scraped_towns` and `scraped_colleges` mysql tables
  - Display colleges which are in the towns populated inside the `scraped_towns` table and additional town info alongside the `scraped_colleges.college` and `scraped_colleges.town`
    - Use an INNER JOIN on `scraped_towns` and `scraped_colleges`
  - Display nj towns and number of colleges in each town 
    - Use GROUP BY clause on `scraped_colleges`
  - Pull requests

