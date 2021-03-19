def opentpl(uuid, payload, rapidAPIKey):

    import json
    import requests

    call = {"uuid": uuid, "body": payload}

    call_json = json.dumps(call)

    try:

        tpl_url = 'https://opentpl1.p.rapidapi.com/dev/tplapi'
        header = {'Content-Type': 'application/json;charset=UTF-8',
                    'X-RapidAPI-Host': 'opentpl1.p.rapidapi.com',
                    'X-RapidAPI-Key': rapidAPIKey
        }

        response = requests.post(tpl_url, headers=header, data=call_json)

        data = response.json()

        return data

    except Exception as e:

        err_string = ('Error tpl call: '+e)

        print(err_string)
        print(call_json)
        print(e)

        error = {'error': err_string}

        return error