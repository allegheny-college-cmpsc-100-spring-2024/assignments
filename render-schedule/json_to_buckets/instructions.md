# JSON to Buckets

Your job is take the schedule.JSON file and split the assignments into three JSON files:

`current.JSON`
`upcoming.JSON`
`past.JSON`

Running `main.py` will put these three files in folder `buckets`.

This is how you will decide which file an assignment goes into:

| assignment type                | due date                     | assigned date                 | file     |
| ------------------------------ | ---------------------------- | ----------------------------- | -------- |
| **problem-sets or exercises** | today is before due date + 7 | today is after assigned date  | current  |
|                                | today is after due date + 7  | any                           | past     |
|                                | any                          | today is before assigned date | upcomng  |
| **everything else**           | today is before due date     | today is after assigned date  | current  |
|                                | today is after due date      | any                           | past     |
|                                | any                          | today is before assigned date | upcoming |
