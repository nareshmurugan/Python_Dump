import json
with open('users.json') as data:
    users=json.load(data)['users']
    initial_data=users[len(users)-1]['userid']
    print(initial_data)
    print("ENTER THE EMAIL ID")
    email_id=input()
    print("ENTER THE PASSWORD")
    password=input()

    users.append({"userid":initial_data+1,"email_id":email_id,"password":password})
    with open('users.json','w') as json_file:
        json.dump({'users':users},json_file)
        
