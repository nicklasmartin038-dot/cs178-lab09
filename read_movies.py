import boto3
from boto3.dynamodb.conditions import Attr

REGION = "us-east-1"
TABLE_NAME = "Movies"

def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_movie(movie):
    title = movie.get("Title", "Unknown Title")
    year = movie.get("Year", "Unknown Year")
    ratings = movie.get("Ratings", "No ratings")
    genre = movie.get("Genre", "Unknown Genre")

    print(f"Title: {title}")
    print(f"Year: {year}")
    print(f"Ratings: {ratings}")
    print(f"Genre: {genre}")
    print()

def print_all_movies():
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])

    print(f"Found {len(items)} movie(s):\n")

    for movie in items:
        print_movie(movie)

def get_movie_by_title():
    title = input("Enter movie title: ")

    table = get_table()
    response = table.scan(
        FilterExpression=Attr("Title").eq(title)
    )

    items = response.get("Items", [])

    if items:
        print("\nMovie found:\n")
        print_movie(items[0])
    else:
        print("\nMovie not found")

if __name__ == "__main__":
    get_movie_by_title()