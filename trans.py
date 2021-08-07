import requests
import key

url = "https://microsoft-translator-text.p.rapidapi.com/translate"

querystring = {"api-version": "3.0", "to": "ar",
               "textType": "plain", "profanityAction": "NoAction"}


def translate(subtitle):
    payload = "[\r\n    {\r\n        \"Text\": \""
    payload2 = "\"\r\n    }\r\n]"
    payload = payload+subtitle+payload2
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': key.key,
        'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com"
    }
    response = requests.request(
        "POST", url, data=payload, headers=headers, params=querystring)

    text = response.text
    start = text.find('"text":"')
    end = text.find('","to"')
    text = text[start+len('"text":"'):end]
    return text


translated = []
finished = False
with open("<YOUR INPUT FILE HERE>") as f:
    for line in f:
        if line[0:1].lower() in "abcdefghijklmnopqrstuvwxyz":
            line = translate(line.replace("\n", " "))
            translated.append(line)
            print(line)
        else:
            translated.append(line.replace("\n", " "))
    finished = True

if finished:
    with open("<YOUR OUT PUT FILE HERE>", "w", encoding="utf-8") as f:
        for line in translated:
            line.encode("utf-8")
            f.write(line)
            f.write("\n")
