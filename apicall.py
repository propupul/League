import requests
from helperfuncs.validationregex import pattern_check

def main():
    try:
        user_name = input("Please enter the username: ")
        name_check = pattern_check(user_name)
        if name_check:       
            call = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/'+name_check+'?api_key=your_API_KEY_GOES_HERE')
            summoner_name = call.json().get(name_check)
            for key, value in summoner_name.items():
                print(key,':', value)
        else:
            print('Please enter a valid username')
    except:
        print('That is not a valid username.')

if __name__ == '__main__':
    main()
