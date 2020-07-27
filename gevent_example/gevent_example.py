import gevent
import time
from gevent import monkey
monkey.patch_all()


def foo_1(sleep_time):
    time.sleep(sleep_time)
    return {"qq": 1}


def foo_2(sleep_time):
    time.sleep(sleep_time)
    return {"qq": 2}


if __name__ == "__main__":
    start_time = time.time()
    gevent_list = []
    gevent_list.append(gevent.spawn(foo_1, 1))
    gevent_list.append(gevent.spawn(foo_2, 2))

    gevent.joinall(gevent_list)
    end_time = time.time()
    print(end_time-start_time)
    for i, data in enumerate(gevent_list):
        print(i, data.value)
