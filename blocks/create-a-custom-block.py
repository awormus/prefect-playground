from prefect.blocks.core import Block

''' Create a custom block with a value that you can then save'''
class Custom(Block):
    message: str

Custom(message="Hello!").save("my-custom-block-2", overwrite=True)

loaded_block = Custom.load("my-custom-block-2")

print(loaded_block.message)