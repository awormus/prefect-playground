from prefect.blocks.system import JSON
from prefect import flow, task, get_run_logger

import json

data = {'hello': 'world'}

print(json.dumps(data))

''' Create a custom block with a value that you can then save'''
JSON(value=json.dumps(data)).save("my-json-block", overwrite=True)

loaded_block = JSON.load("my-json-block")