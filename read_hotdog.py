import boto3

REGION = "us-east-1"
TABLE_NAME = "HotDogRatings"

def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_hotdog(item):
    name = item.get("Name", "Unknown Name")
    calories = item.get("Calories", "Unknown Calories")
    rating = item.get("Rating", "Unknown Rating")

    print(f"Name: {name}")
    print(f"Calories: {calories}")
    print(f"Rating: {rating}")
    print()

def print_all_hotdogs():
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])

    if not items:
        print("No hot dogs found.")
        return

    print(f"Found {len(items)} hot dog(s):\n")

    for item in items:
        print_hotdog(item)

if __name__ == "__main__":
    print_all_hotdogs()