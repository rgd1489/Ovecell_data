# app/main.py
import argparse
import os
import json
import csv
from database import Database

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

def insert_user_record(db, user):
    db.execute("""
        INSERT INTO users (first_name, last_name, email, gender, ip_address, dob, country, game)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """, (
        user.get('first_name', ''),
        user.get('last_name', ''),
        user.get('email', ''),
        user.get('gender', ''),
        user.get('ip_address', ''),
        user.get('dob', None),
        user.get('country', ''),
        user.get('game', ''),
    ))

def import_data(db, data_directory, game, date):
    file_path = os.path.join(data_directory, game, date)
    if game == 'wwc':
        json_files = [f for f in os.listdir(file_path) if f.endswith('.json')]
        for json_file in json_files:
            data = read_json_file(os.path.join(file_path, json_file))
            for user in data:
                insert_user_record(db, user)
    elif game == 'hb':
        csv_files = [f for f in os.listdir(file_path) if f.endswith('.csv')]
        for csv_file in csv_files:
            data = read_csv_file(os.path.join(file_path, csv_file))
            for user in data:
                insert_user_record(db, user)
    else:
        print(f"Unsupported game: {game}")

def main():
    parser = argparse.ArgumentParser(description="Ovicell Data Pipeline")
    parser.add_argument("game", choices=["wwc", "hb"], help="Game name ('wwc' or 'hb')")
    parser.add_argument("date", help="Date in the format 'YYYY-MM-DD'")
    args = parser.parse_args()

    db = Database()

    # Create database schema
    db.execute_script('create_schema.sql')

    # Import user accounts
    data_directory = 'data'
    import_data(db, data_directory, args.game, args.date)

if __name__ == "__main__":
    main()
