import pandas as pd
import openai as novaai

api_url = 'https://sdw-2023-prd.up.railway.app'
api_openai = 'YOUR_API_KEY_HERE'

novaai.api_base = 'https://api.nova-oss.com/v1'
novaai.api_key = api_openai

df = pd.read_csv('./data/ACCELERACERS.csv')

racers = {}

for index, row in df.iterrows():
    racers[index] = {
        "Id": row['ID'], 
        "Name": row['NAME'], 
        "Age": row['AGE'], 
        "Team": row['TEAM'], 
        "Car": row['CAR']
    }

def alert_new_kingdom(racers):

    completion = novaai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[  

            {
                "role": "system",
                "content": "You are a commander of racing pilots like Dr Tesla from the series Hot Wheels Acceleracers."
            },
            {
                "role": "user", 
                "content": f"Create an personalized alert for {racers['Name']} of a new racing realm that is about to open saying that her/him is selected to run with his/her{racers['Car']}  (max 200 caracters)"
            }

        ]
    )

    print(completion.choices[0].message.content)

for index in racers:
   alert_new_kingdom(racers[index])
