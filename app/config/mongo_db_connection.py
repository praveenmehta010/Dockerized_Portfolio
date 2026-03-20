import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from the .env file (if present)
load_dotenv()

# Access environment variables as if they came from the actual environment
# SECRET_KEY = os.getenv('SECRET_KEY')
# DATABASE_URL = os.getenv('DATABASE_URL')

# # Example usage
# print(f'SECRET_KEY: {SECRET_KEY}')
# print(f'DATABASE_URL: {DATABASE_URL}')



uri = os.getenv('MONGO_URI')
# mongo database connection
client = MongoClient(uri)

# try:
#     database = client.get_database("sample_mflix")
#     movies = database.get_collection("movies")

#     # Query for a movie that has the title 'Back to the Future'
#     query = { "title": "Back to the Future" }
#     movie = movies.find_one(query)

#     print(movie)

#     client.close()

# except Exception as e:
#     raise Exception("Unable to find the document due to the following error: ", e)

# document connection
try:
    database = client.get_database("portfolio")
except Exception as e:
    raise Exception("Unable to find the Database due to the following error: ", e)

# Contact collection connection
try:
    contacts = database.get_collection("contacts")

except Exception as e:
    raise Exception("Unable to find the Collection of contacts due to the following error: ", e)

# Contact collection connection
try:
    projects = database.get_collection("projects")

except Exception as e:
    raise Exception("Unable to find the Collection of Projects due to the following error: ", e)