from prefect.client import get_client
import asyncio

async def main():
    async with get_client() as client:
        # set a concurrency limit of 10 on the 'small_instance' tag
        limit_id = await client.create_concurrency_limit(
            tag="concurrent_5", 
            concurrency_limit=5
        )


if __name__ == "__main__":
    asyncio.run(main())