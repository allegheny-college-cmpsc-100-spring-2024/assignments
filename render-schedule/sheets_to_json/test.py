
#C:\Users\kaiba\OneDrive\Asztali gép\assignments\render-schedule\sheets_to_json\test.py
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def main():
    #https://docs.google.com/spreadsheets/d/104OkqDtqq2ghhPYb01ct3KtmoegtOU3iLnL3DVIXOvo/edit#gid=0
    #https://spreadsheets.google.com/feeds
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('test.json', scope)
    gc = gspread.authorize(credentials)
    mySheet = gc.open('CMPSC-100 Assignment Schedule')
    worksheet = mySheet.worksheet('Sheet1')
    print(worksheet)




if __name__ == "__main__":
    main()
