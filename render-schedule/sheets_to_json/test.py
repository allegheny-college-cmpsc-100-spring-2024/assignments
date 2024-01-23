"""This is a test file for testing the new codes added before adding it to the main file """

import json

def main():
    jsonFile = open("schedule.json")
    data = json.load(jsonFile)

    for key, value in data['due:'].items():
        print(key, value)






if __name__ == "__main__":
    main()
