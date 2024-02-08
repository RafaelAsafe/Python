from httpx import AsyncClient
from asyncio import run, gather
from aiometer import run_all
from pokes import pokes as pokemons
from functools import partial
from rich import print

async def evolves(poke):
    async with AsyncClient(base_url='https://pokeapi.co/api/v2/') as client:

        print(f'[b][blue]request 1:{poke}[/]')
        response = await client.get(f'/pokemon/{poke}')
        poke_id = response.json().get('id')

        print(f'[r][red]request 2:{poke}[/]')
        response = await client.get(f'/pokemon-species/{poke_id}')
        evolution_chain = response.json().get('evolution_chain').get('url')

        response = await client.get(evolution_chain)

        print(f'[g][green] request 3:{poke}[/]')
        evolution_name = response.json().get('chain').get(
            'evolves_to')[0].get('species').get('name')


async def main():
   
    result = run_all(
        [partial(evolves, poke) for poke in pokemons], max_per_second=100)
    await result

run(main())
