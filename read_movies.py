import boto3

REGION = "us-east-1"
TABLE_NAME = "Movies"

def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_movie(movie):
    title = movie.get("Title", "Unknown Title")
    year = movie.get("Year", "Unknown Year")
    ratings = movie.get("Ratings", "No ratings")

    print(f"Title: {title}")
    print(f"Year: {year}")
    print(f"Ratings: {ratings}")
    print()

def print_all_movies():
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])

    print(f"Found {len(items)} movie(s):\n")

    for movie in items:
        print_movie(movie)

if __name__ == "__main__":
    print_all_movies()