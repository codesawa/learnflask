""" A ------ > B ------- C
    if B fails ----- D


    Message Queues 
"""
from redis import Redis
from rq import Queue
from job import expensive_call, on_success_count, do_something_else

redis_db_connection = Redis(host="localhost", port=6379)

job_queue = Queue(connection=redis_db_connection)



"""

    job_timeout
    result_ttl
    ttl
    failure_ttl
    depends_on
    job_id
    at_front
    description >> message describing what the function does
    on_success >>
    on_failure >>
    on_stopped >>

    args, 

    kwargs >>
"""
job= job_queue.enqueue(
    expensive_call,
    args=("https://www.google.com",),
    on_success = on_success_count
)

job_2 = job_queue.enqueue(do_something_else, depends_on = job)