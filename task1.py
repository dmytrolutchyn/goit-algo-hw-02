import queue
import time
import random

queue = queue.Queue()


def generate_request():
    request_id = random.randint(1000, 9999)
    queue.put(request_id)
    print(f"Request {request_id} was added to the queue")
    print(f"Queue contents: {list(queue.queue)}")


def process_request():
    if not queue.empty():
        request_id = queue.get()
        print(f"Request {request_id} was processed")
    else:
        print("Queue is empty, nothing to process")


try:
    while True:
        process_request()
        generate_request()
        generate_request()
        generate_request()
        process_request()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nKeybord interrupt")
