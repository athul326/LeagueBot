import requests
import os

API = str(os.environ.get('RIOT_KEY'))
class LeagueBot:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update

    def requestsummonerid(userName):

        URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + userName + "?api_key=" + API
        response = requests.get(URL)

        return response.json()
    def requestrankeddata(ID):

        URL = "https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/" + ID + "?api_key=" + API
        response = requests.get(URL)
        return response.json()

    def requestchampdata(ID):

        URL = "https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + ID + "?api_key=" + API
        response = requests.get(URL)
        return response.json()
    def requestchampname(ID):
        URL = "https://na1.api.riotgames.com/lol/static-data/v3/champions/" + ID + "?locale=en_US&tags=info&api_key=" + API
        response = requests.get(URL)
        return response.json()

    def champname(ID):

        switcher = {

                    1:"Annie",

                    2:"Olaf",

                    3:"Galio",

                    4: "Twisted Fate",

                    5: "Xin Zhao",

                    6: "Urgot",

                     7: "LeBlanc",

                    8: "Vladimir",

                    9: "Fiddlesticks",

                    10: "Kayle",

                    11: "Master Yi",

                    12: "Alistar",

                    13:"Ryze",

                    14: "Sion",

                    15: "Sivir",

                    16: "Soraka",

                    17: "Teemo",

                    18: "Tristana",

                    19: "Warwick",

                    20: "Nunu",

                    21: "Miss Fortune",

                    22: "Ashe",

                    23:"Tryndamere",

                    24: "Jax",

                    25: "Morgana",

                    26: "Zilean",

                    27: "Singed",

                    28: "Evelynn",

                    29: "Twitch",

                    30: "Karthus",

                    31: "Cho'Gath",

                    32: "Amumu",

                    33:"Rammus",

                    34: "Anivia",

                    35: "Shaco",

                    36: "Dr. Mundo",

                    37: "Sona",

                    38: "Kassadin",

                    39:"Irelia",

                    40: "Janna",

                    41: "Gangplank",

                    42: "Corki",

                    43: "Karma",

                    44: "Taric",

                    45: "Veigar",

                    48: "Trundle",

                    50: "Swain",

                    51: "Caitlyn",

                    53: "Blitzcrank",

                    54: "Malphite",

                    55: "Katarina",

                    56: "Nocturne",

                    57: "Maokai",

                    58: "Renekton",

                    59: "Jarvan IV",

                    60: "Elise",

                    61: "Orianna",

                    62: "Wukong",

                    63: "Brand",

                    64: "Lee Sin",

                    67: "Vayne",

                    68: "Rumble",

                    69: "Cassiopeia",

                    72: "Skarner",

                    74: "Heimerdinger",

                    75: "Nasus",

                    76: "Nidalee",

                    77: "Udyr",

                    78: "Poppy",

                    79: "Gragas",

                    80: "Pantheon",

                    81: "Ezreal",

                    82:"Mordekaiser",

                    83: "Yorick",

                    84:"Akali",

                    85:"Kennen",

                    86:"Garen",

                    89: "Leona",

                    90: "Malzahar",

                    91:"Talon",

                    92: "Riven",

                    96: "Kog'Maw",

                    98: "Shen",

                    99:"Lux",

                    101: "Xerath",

                    102: "Shyvana",

                    103:"Ahri",

                    104: "Graves",

                    105:"Fizz",

                    106:"Volibear",

                    107: "Rengar",

                    110:"Varus",

                    111:"Nautilus",

                    112: "Viktor",

                    113:"Sejuani",

                    114:"Fiora",

                    115: "Ziggs",

                    117:"Lulu",

                    119: "Draven",

                    120:"Hecarim",

                    121:"Kha'Zix",

                    122:"Darius",

                    126: "Jayce",

                    127: "Lissandra",

                    131: "Diana",

                    133: "Quinn",

                    134: "Syndra",

                    136:"Aurelion Sol",

                    143:"Zyra",

                    154: "Zac",

                    157:"Yasuo",

                    161:"Vel'Koz",

                    163:"Taliyah",

                    164:"Camille",

                    201:"Braum",

                    202:"Jhin",

                    203:"Kindred",

                    222:"Jinx",

                    223:"Tahm Kench",

                    236:"Lucian",

                    238: "Zed",

                    240: "Kled",

                    245:"Ekko",

                    254: "Vi",

                    266:"Aatrox",

                    267: "Nami",

                    268: "Azir",

                    412:"Thresh",

                    420:"Illaoi",

                    421:"Rek'Sai",

                    427:"Ivern",
                    429: "Kalista",
                    432:"Bard",
                    497: "Rakan",
                    498:"Xayah"
        }
        return switcher.get(ID,"Unknown Champ")


token = str(os.environ.get('TEL_KEY'))
BetterLeagueBot = LeagueBot(token)



def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates= BetterLeagueBot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if 'ree' in first_chat_text:
                    BetterLeagueBot.send_message(first_chat_id, 'You forgot your pills today ' + first_chat_name)
                    new_offset = first_update_id + 1
                if '/user' in first_chat_text:
                    userName = first_chat_text[6:]
                    responseJSON = LeagueBot.requestsummonerid(userName)
                    ID = str(responseJSON['id'])

                    responseJSON2 = LeagueBot.requestrankeddata(ID)
                    rankTier = responseJSON2[1]['tier']
                    rankNum =  str(responseJSON2[1]['rank'])
                    winRate = str('%.2f'%(responseJSON2[1]['wins']/(responseJSON2[1]['wins']+responseJSON2[1]['losses'])*100))

                    rankTier2 = responseJSON2[0]['tier']
                    rankNum2 = str(responseJSON2[0]['rank'])
                    winRate2 = str('%.2f' % (responseJSON2[0]['wins'] / (responseJSON2[0]['wins'] + responseJSON2[0]['losses']) * 100))

                    responseJSON3 = LeagueBot.requestchampdata(ID)
                    responseJSON4 = LeagueBot.champname(responseJSON3[0]['championId'])
                    champion1 = responseJSON4
                    champion1Level = str(responseJSON3[0]['championLevel'])
                    champion1Points = str(responseJSON3[0]['championPoints'])

                    responseJSON5 = LeagueBot.champname(responseJSON3[1]['championId'])
                    champion2 = responseJSON5
                    champion2Level = str(responseJSON3[1]['championLevel'])
                    champion2Points = str(responseJSON3[1]['championPoints'])

                    responseJSON6 = LeagueBot.champname(responseJSON3[2]['championId'])
                    champion3 = responseJSON6
                    champion3Level = str(responseJSON3[2]['championLevel'])
                    champion3Points = str(responseJSON3[2]['championPoints'])

                    BetterLeagueBot.send_message(first_chat_id, 'User: '+userName+'\nRanked Solo: ' +rankTier+' '+rankNum+' '+ winRate +'% winrate\nRanked Flex: '+ rankTier2 +' '+rankNum2 +' '+winRate2 +"% winrate\n Most Played Champions: \n" + champion1 + " Mastery Level: "+champion1Level+" Mastery Points: "+champion1Points+"\n"+champion2 + " Mastery Level: "+champion2Level+" Mastery Points: "+champion2Points+"\n"+champion3 + " Mastery Level: "+champion3Level+" Mastery Points: "+champion3Points+"\n")
                    new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()