#!/usr/bin/env python3

from typing import List
import asyncio
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Execute task_wait_random and returns sorted list of delay'''
    spawn_ls = []
    delay_ls = []
    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delay_ls.append(x.result()))
        spawn_ls.append(delayed_task)

    for spawn in spawn_ls:
        await spawn

    return delay_ls
