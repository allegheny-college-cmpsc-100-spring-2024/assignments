
#C:\Users\kaiba\OneDrive\Asztali gép\assignments\render-schedule\sheets_to_json\test.py
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from rich.console import Console

def main():
    #https://docs.google.com/spreadsheets/d/104OkqDtqq2ghhPYb01ct3KtmoegtOU3iLnL3DVIXOvo/edit#gid=0
    #https://spreadsheets.google.com/feeds
    console = Console()
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('test.json', scope)
    gc = gspread.authorize(credentials)

    current_directory = os.path.dirname(os.path.abspath(__path__))
    json_file_path = os.path.join(current_directory, 'src', 'sheets_to_json', 'test.json')
    full_path = ServiceAccountCredentials.from_json_keyfile_name(json_file_path, scope)
    gc = gspread.authorize(full_path)

    mySheet = gc.open('CMPSC-100 Assignment Schedule')
    worksheet = mySheet.worksheet('Sheet1')
    #print(worksheet)
    console.print(worksheet)
    
    #looking for errors in the json file 
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_path, scope)
    except json.decoder.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")


if __name__ == "__main__":
    main()
