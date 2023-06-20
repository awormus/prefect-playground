from prefect.blocks.system import Secret
from prefect import flow, task, get_run_logger

import json

data = {'hello': 'robert'}

print(json.dumps(data))

''' Create a custom block with a value that you can then save'''
Secret(value=json.dumps(data)).save("robert-secret-block", overwrite=True)

loaded_block = Secret.load("robert-secret-block")
print(loaded_block.get())