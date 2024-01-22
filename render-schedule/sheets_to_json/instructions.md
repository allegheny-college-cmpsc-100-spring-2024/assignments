# Sheets to JSON

## Potential Libraries

The libraries I have found to achieve this are:

- [Google's API](https://developers.google.com/sheets/api/quickstart/python)
- [gsheets wrapper for above](https://pypi.org/project/gsheets/)

I haven't worked with these libraries myself so this will be a bit of a new adventure! If it turns out they don't work too great, you can let me know. There are some alternative options. You can also research other libraries yourself. 

Your goal is to edit `main.py` so that it turns [this Google sheet](https://docs.google.com/spreadsheets/d/104OkqDtqq2ghhPYb01ct3KtmoegtOU3iLnL3DVIXOvo/edit?usp=sharing) into a file called `schedule.JSON` that is formatted as follows.

Note that if no time is specified for an assignment's assign date, you should set it to midnight (00:00). If no time is specified for its due date, you should set it for 8:00 (20:00).

```
[{"name": "paper-coordinates", "category": "exercises", "assigned":	"2024-01-18T00:00",	"due":"2024-01-18T20:00", "link":	"https://classroom.github.com/a/iYUubKEG"}, 
{"name": "helix-variations", "category": "exercises", "assigned":	"2024-01-16T00:00",	"due":"2024-01-16T20:00", "link":	"https://classroom.github.com/a/tOox8MQP"}]
```