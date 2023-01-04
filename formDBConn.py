import os
from getpass import getpass
from mysql.connector import connect, Error
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests, re

load_dotenv(os.path.join(os.getcwd(), ".env")) # take environment variables from .env

try:
    with connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        database=os.environ.get("DB_NAME"),
    ) as connection:
        '''colleges = []
        towns = []
        source = requests.get("https://en.wikipedia.org/wiki/List_of_colleges_and_universities_in_New_Jersey").text
        soup = BeautifulSoup(source, "lxml")

        
        # Get all tr's, under public and private universites, then scrape all info you need 
        
        public_college_towns_in_nj = soup.find_all("table")[1].find_all("a", href=re.compile("\/wiki\/\w+,\w+"))
        private_college_towns_in_nj = soup.find_all("table")[2].find_all("a", href=re.compile("\/wiki\/\w+,\w+"))
        college_towns_in_nj = public_college_towns_in_nj + private_college_towns_in_nj
        for college_town_in_nj in college_towns_in_nj:
            town = college_town_in_nj.text
            town_university = college_town_in_nj.parent.parent.find("td").text
            town_src = college_town_in_nj["href"]
            town_link = f'https://en.wikipedia.org{town_src}'
            town_source = requests.get(town_link).text
            soup = BeautifulSoup(town_source, "lxml")
            town_area = float(soup.find_all("th",string=re.compile("Total"))[0].next_sibling.text.split()[0])
            town_population = int(soup.find_all("th",string=re.compile("Total"))[1].next_sibling.text.replace(',',''))
            town_water_area = soup.find("th", class_="infobox-label", string=re.compile("Water")).next_sibling.text.split()[0]
            matched_things =  soup.find_all("td", class_="infobox-data", string=re.compile("m\)"))
            town_elevation = None
            if len(matched_things) > 0:
                town_elevation = int(matched_things[0].text.split()[0])
            # t_e could be None
            town_land_area = float(soup.find("th", class_="infobox-label", string=re.compile("Land")).next_sibling.text.split()[0])
            # town_area_code = soup.find("th", class_="infobox-label", string=re.compile("Land")).next_sibling.text

            college_row = (town_university, town)
            town_row = (town, town_population, town_area, town_water_area, town_land_area, town_elevation)
            colleges.append(college_row)
            towns.append(town_row)
        '''
        '''create_movies_table_query = """
        CREATE TABLE movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR(4),
            genre VARCHAR(100),
            collection_in_mil INT
        )
        """
        create_reviewers_table_query = """
        CREATE TABLE reviewers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100)
        )
        """
        create_ratings_table_query = """
        CREATE TABLE movieratings (
            movie_id INT,
            reviewer_id INT,
            rating DECIMAL(2,1),
            FOREIGN KEY(movie_id) REFERENCES movies(id),
            FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
            PRIMARY KEY(movie_id, reviewer_id)
        )
        """
        show_table_query = "DESCRIBE movies"
        alter_table_query = """
        ALTER TABLE movies
        MODIFY COLUMN collection_in_mil DECIMAL(4,1)
        """
        insert_movies_query = """
        INSERT INTO movies (title, release_year, genre, collection_in_mil)
        VALUES
            ("Forrest Gump", 1994, "Drama", 330.2),
            ("3 Idiots", 2009, "Drama", 2.4),
            ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
            ("Good Will Hunting", 1997, "Drama", 138.1),
            ("Skyfall", 2012, "Action", 304.6),
            ("Gladiator", 2000, "Action", 188.7),
            ("Black", 2005, "Drama", 3.0),
            ("Titanic", 1997, "Romance", 659.2),
            ("The Shawshank Redemption", 1994, "Drama",28.4),
            ("Udaan", 2010, "Drama", 1.5),
            ("Home Alone", 1990, "Comedy", 286.9),
            ("Casablanca", 1942, "Romance", 1.0),
            ("Avengers: Endgame", 2019, "Action", 858.8),
            ("Night of the Living Dead", 1968, "Horror", 2.5),
            ("The Godfather", 1972, "Crime", 135.6),
            ("Haider", 2014, "Action", 4.2),
            ("Inception", 2010, "Adventure", 293.7),
            ("Evil", 2003, "Horror", 1.3),
            ("Toy Story 4", 2019, "Animation", 434.9),
            ("Air Force One", 1997, "Drama", 138.1),
            ("The Dark Knight", 2008, "Action",535.4),
            ("Bhaag Milkha Bhaag", 2013, "Sport", 4.1),
            ("The Lion King", 1994, "Animation", 423.6),
            ("Pulp Fiction", 1994, "Crime", 108.8),
            ("Kai Po Che", 2013, "Sport", 6.0),
            ("Beasts of No Nation", 2015, "War", 1.4),
            ("Andadhun", 2018, "Thriller", 2.9),
            ("The Silence of the Lambs", 1991, "Crime", 68.2),
            ("Deadpool", 2016, "Action", 363.6),
            ("Drishyam", 2015, "Mystery", 3.0)
        """
        insert_reviewers_query = """
        INSERT INTO reviewers
        (first_name, last_name)
        VALUES ( %s, %s )
        """
        reviewers_records = [
            ("Chaitanya", "Baweja"),
            ("Mary", "Cooper"),
            ("John", "Wayne"),
            ("Thomas", "Stoneman"),
            ("Penny", "Hofstadter"),
            ("Mitchell", "Marsh"),
            ("Wyatt", "Skaggs"),
            ("Andre", "Veiga"),
            ("Sheldon", "Cooper"),
            ("Kimbra", "Masters"),
            ("Kat", "Dennings"),
            ("Bruce", "Wayne"),
            ("Domingo", "Cortes"),
            ("Rajesh", "Koothrappali"),
            ("Ben", "Glocker"),
            ("Mahinder", "Dhoni"),
            ("Akbar", "Khan"),
            ("Howard", "Wolowitz"),
            ("Pinkie", "Petit"),
            ("Gurkaran", "Singh"),
            ("Amy", "Farah Fowler"),
            ("Marlon", "Crafford"),
        ]
        
        insert_ratings_query = """
        INSERT INTO movieratings
        (rating, movie_id, reviewer_id)
        VALUES ( %s, %s, %s)
        """
        ratings_records = [
            (6.4, 17, 5), (5.6, 19, 1), (6.3, 22, 14), (5.1, 21, 17),
            (5.0, 5, 5), (6.5, 21, 5), (8.5, 30, 13), (9.7, 6, 4),
            (8.5, 24, 12), (9.9, 14, 9), (8.7, 26, 14), (9.9, 6, 10),
            (5.1, 30, 6), (5.4, 18, 16), (6.2, 6, 20), (7.3, 21, 19),
            (8.1, 17, 18), (5.0, 7, 2), (9.8, 23, 3), (8.0, 22, 9),
            (8.5, 11, 13), (5.0, 5, 11), (5.7, 8, 2), (7.6, 25, 19),
            (5.2, 18, 15), (9.7, 13, 3), (5.8, 18, 8), (5.8, 30, 15),
            (8.4, 21, 18), (6.2, 23, 16), (7.0, 10, 18), (9.5, 30, 20),
            (8.9, 3, 19), (6.4, 12, 2), (7.8, 12, 22), (9.9, 15, 13),
            (7.5, 20, 17), (9.0, 25, 6), (8.5, 23, 2), (5.3, 30, 17),
            (6.4, 5, 10), (8.1, 5, 21), (5.7, 22, 1), (6.3, 28, 4),
            (9.8, 13, 1)
        ]
        create_towns_table_query = """
        CREATE TABLE scraped_towns(
            town VARCHAR(100) PRIMARY KEY,
            population INT,
            area_in_sq_mi DECIMAL(10, 2),
            water_area VARCHAR(100),
            land_area DECIMAL(10, 2),
            elevation_in_ft INT
        )"""
        create_colleges_table_query = """
        CREATE TABLE scraped_colleges(
            college VARCHAR(100) PRIMARY KEY, 
            town VARCHAR(100),
            FOREIGN KEY(town) REFERENCES scraped_towns(town)
        )"""

        insert_scraped_colleges_query = """
        INSERT INTO scraped_colleges
        (college, town)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE
        town = VALUES(town)
        """
        insert_scraped_towns_query = """
        INSERT INTO scraped_towns
        (town, population, area_in_sq_mi, water_area, land_area, elevation_in_ft)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        population = VALUES(population),
        area_in_sq_mi = VALUES(area_in_sq_mi),
        water_area = VALUES(water_area),
        land_area = VALUES(land_area),
        elevation_in_ft = VALUES(elevation_in_ft)
        """
        '''
        # TRUNCATE college table here 
        delete_colleges_table_query = """
            DELETE FROM scraped_colleges
        """
        # ALTER college table here 
        alter_colleges_table_query = """
            ALTER TABLE scraped_colleges
            DROP COLUMN town
        """
        add_column_to_colleges_table_query = """
            ALTER TABLE scraped_colleges
            ADD COLUMN town VARCHAR(100)
        """
        show_table_query = "SELECT CONSTRAINT_NAME from INFORMATION_SCHEMA.TABLE_CONSTRAINTS where TABLE_NAME = 'scraped_colleges'"
        with connection.cursor() as cursor:
            '''cursor.execute(create_movies_table_query)
            cursor.execute(create_reviewers_table_query)
            cursor.execute(create_ratings_table_query)
            cursor.execute(insert_movies_query)
            cursor.executemany(insert_reviewers_query, reviewers_records)
            cursor.executemany(insert_ratings_query, ratings_records)
            cursor.execute(create_towns_table_query)
            cursor.execute(create_colleges_table_query)
            cursor.executemany(insert_scraped_towns_query, towns)
            cursor.executemany(insert_scraped_colleges_query, colleges)
            # A transaction in MySQL is a sequential group of statements, queries, or operations such as select, insert, update or delete to perform as a one single work unit that can be committed or rolled back
            # commit or rollback the transaction
            cursor.execute(delete_colleges_table_query)'''
            #cursor.execute(alter_colleges_table_query)
            '''connection.commit()'''
            cursor.execute(add_column_to_colleges_table_query)
            '''cursor.execute(show_table_query)
            # cursor.execute(select_query)
            result = cursor.fetchall()
            # print("Movie Table Schema after alteration:")
            for row in result:
                print(row)
                '''
        
except Error as e:
    print(e)