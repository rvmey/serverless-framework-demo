import json, os, random

def handler(event, context):
    if os.environ['STAGE'] == 'dev':
        print(json.dumps(event))

    colors = ['red','blue','green']
    random_color = random.choice(colors)
    print("Random color from list is: ", random_color)

    response = {
        "color": random_color
    }

    return response

