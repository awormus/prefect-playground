import pandas as pd
from tabulate import tabulate
from json import loads, dumps
from prefect import task, flow, get_run_logger


''' 
Use pandas to download a csv file of capitals, and then convert it to json ensuring that 
all fields are converted to utf-8.

Then we will sort the capitals by the first letter of the name, and save them to a file.

We want to make sure that the file name is a valid windows file name.
'''

@task(name="Ingest Data")
def get_data(file_location, col_sep=','):
    df = pd.read_csv(file_location, sep=col_sep, encoding="UTF-8")

    ''' sort by name '''
    df = df.sort_values(by=['name'])

    return df


@task(name="Convert To JSON format")
def convert_to_json(data_frame):
    results_1 = data_frame.to_json(orient="records")
    parsed = loads(results_1)
    results_2 = dumps(parsed, indent=4)
    return results_2

@flow(name="Ingest Flat File")
def process_data(file_name, col_sep):
    data = get_data(file_name, col_sep)
    top_5 = data.head(1)
    json_dat = convert_to_json(top_5)
    return [top_5, json_dat]

if __name__ == '__main__':
    results = process_data(file_name='https://raw.githubusercontent.com/datasets/world-cities/master/data/world-cities.csv',
                           col_sep=',')

    flat_data = results[0]
    json_data = results[1]

    results_2 = flat_data.head()
    results_2_header = flat_data.columns
    print('---[This is the Flat Data]---')
    print(tabulate(results_2, headers=results_2_header))
    print('---[This is the JSON Data]---')
    print(json_data)