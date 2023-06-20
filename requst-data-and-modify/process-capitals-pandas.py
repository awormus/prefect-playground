from prefect import flow, task, get_run_logger
import pandas as pd
import os

''' 
Use pandas to download a csv file of capitals, and then convert it to json ensuring that 
all fields are converted to utf-8.

Then we will sort the capitals by the first letter of the name, and save them to a file.

We want to make sure that the file name is a valid windows file name.
'''

@task
def download_csv_with_pandas():
    ''' This function downloads a csv file using pandas '''
    l = get_run_logger()
    l.info("Downloading csv with pandas")

    df = pd.read_csv("https://raw.githubusercontent.com/datasets/world-cities/master/data/world-cities.csv", encoding='UTF-8')

    l.info(df.head(1))
    return df

@task
def save_capitals(df: pd.DataFrame):
    ''' This function saves the capitals to a file '''
    l = get_run_logger()
    print("Saving capitals to file")

    ''' sort by name '''
    df = df.sort_values(by=['name'])
    l.info("Saving to file: ")
    l.info(df.head(1))

    return df


@flow(name="Process Capitals with Pandas")
def run_flow():

    ''' This should return a pandas dataframe'''
    csv_input = download_csv_with_pandas()
    saved_capitals = save_capitals(csv_input)


if __name__ == '__main__':
    run_flow()
