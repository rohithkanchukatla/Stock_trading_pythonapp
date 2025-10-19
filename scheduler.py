import schedule

import time

from script import run_job

from datetime import datetime

def test_job():
    print("job started at: ",datetime.now())

test_job()

schedule.every().second.do(run_job)


while True:
    schedule.run_pending()
    time.sleep(1)