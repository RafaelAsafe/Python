from asyncio import all_tasks, create_task, run, sleep, gather
from rich import print


async def olar(val, delay=1):
    print(f'Inicio da corrotina {val}')
    await sleep(delay)
    print(f'Meio da corrotina {val}')
    await sleep(delay)
    print(f'Fim da corrotina {val}')
    return val


async def main():
    tasks = gather(olar(30, 5), *[olar(n) for n in range(3)])

    print(f'Fila as tasks:{all_tasks()}')

    result = await tasks
    print(result)

    print(f'Fila as tasks:{all_tasks()}')

run(main())
