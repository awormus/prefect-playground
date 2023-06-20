from prefect import flow, task, logging
import requests
import csv
import os

'''
This script downloads a csv with the capitals of the world, and then saves them into alphabetical files.
'''

@task
def download_csv():
    """This function downloads the csv"""
    l = logging.get_logger()
    l.info("Downloading csv")

    url = "https://raw.githubusercontent.com/datasets/world-cities/master/data/world-cities.csv"
    r = requests.get(url)

    return r.text

@task
def convert_csv_to_json(csv_input):
    """This function converts the csv to json"""
    l = logging.get_logger()
    l.info("Converting csv to json")

    capitals = csv.DictReader(csv_input.splitlines())
    capitals = sorted(capitals, key=lambda x: x['name'])

    return capitals

@task
def sort_capitals(json):
    """This function sorts the capitals"""
    l = logging.get_logger()
    l.info("Sorting capitals")

    capitals = {}
    for capital in json:
        first_letter = capital['name'][0]

        ''' convert the first letter to utf-8, and then to lowercase '''
        first_letter = first_letter.encode('utf-8').lower()

        ''' make sure the first letter is a letter '''
        if first_letter not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']:
            first_letter = 'zz'


        if first_letter not in capitals:
            capitals[first_letter] = []

        capitals[first_letter].append(capital)

    l.info(capitals)

    return capitals

@task 
def save_capitals(sorted_capitals):
    """This function saves the capitals"""
    l = logging.get_logger()
    l.info("Saving capitals")

    if not os.path.exists("capitals"):
        os.mkdir("capitals")

    for letter, capitals in sorted_capitals.items():
        with open(f"capitals/{letter}.json", "w") as f:
            f.write(str(capitals))

@flow(name="Process Capitals")
def run_flow():
    csv_input = download_csv()
    json = convert_csv_to_json(csv_input)
    sorted_capitals = sort_capitals(json)
    saved = save_capitals(sorted_capitals)

if __name__ == "__main__":
    run_flow()


