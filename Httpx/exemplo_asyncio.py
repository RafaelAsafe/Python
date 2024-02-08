from asyncio import all_tasks, create_task, run, sleep
from rich import print


async def olar(val, delay=1):
    print(f'Inicio da corrotina {val}')
    await sleep(delay)
    print(f'Meio da corrotina {val}')
    await sleep(delay)
    print(f'Fim da corrotina {val}')


async def main():
    task1 = create_task(olar(1, 10))
    task2 = create_task(olar(2))
    task2 = create_task(olar(3))
    task2 = create_task(olar(4))
    print(f'Fila as tasks:{all_tasks()}')

    await task1

    await task2

    await task3

    await task4

    print(f'Fila as tasks:{all_tasks()}')

run(main())
