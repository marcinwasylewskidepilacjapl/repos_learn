import asyncio
from random import randint

async def counting_from_a_to_b(a,b):
    print(f"W zalozeniu licze od {a} do {b}")
    for i in range(a,b):
        print(i)
        await asyncio.sleep(0.25)
    return "All done!"
async def some_pause_sentence(text, sleep_time):
    print(f"W zalozeniu bede czekac {sleep_time} sekund na wyswietlenie przeslanego tekstu")
    await asyncio.sleep(sleep_time)
    print(text)
    return "some_pause"

async def main():
    task1 = asyncio.create_task(counting_from_a_to_b(1,randint(10,50)))
    task2 = asyncio.create_task(some_pause_sentence("Tralalala",randint(0,10)))

    print("W create task polecenia od razu sie włączają")
    # print("Teraz main zakonczy dzialanie jak wykona oba zadania bo do obu zadan jest await")
    # value = await task2
    # print(value)
    # value2 = await task1
    # print(value2)
    #
    print("Teraz main zakonczy dzialanie kiedy wykona task2, a z kolei task1 tyle ile da rade")
    value = await task2
    print(value)

    # print("Teraz main zakonczy dzialanie kiedy wykona task1, a z kolei task2 tyle ile da rade")
    # value2 = await task1
    # print(value2)


asyncio.run(main())

