import consul
import json
import sys
import pymongo

folder_name = sys.argv[1]
result_file_name = 'result.json'
consul_key = 'MongoDb/' + str(folder_name)
master = consul.Consul(host='10.222.185.238', port=8500, token='0426c021-bbad-832d-1f9d-ed5cbf59077c',
                       dc='dc1')
index, data = master.kv.get(consul_key)
result = (data['Value'])
print(result)
json_result = (json.loads(result))
if json_result['mongo']['username'] == "none":
    auth_required = False
    username = None
    password = None
else:
    auth_required = True



if auth_required:
    username = json_result['mongo']['username']
    password = json_result['mongo']['password']
    for each_server in json_result['mongo']['host']:
        print(each_server)
        conn_string = ("mongodb://%s") % (each_server)
        conn = pymongo.MongoClient("%s" % (conn_string))
        print(conn)
        authenabled = conn.admin.authenticate(username, password)
        if conn.is_primary:
            primary_server = each_server

else:
    for each_server in json_result['mongo']['host']:
        conn_string = ("mongodb://%s") % (each_server)
        conn = pymongo.MongoClient("%s" % (conn_string))
        try:
            if conn.is_primary:
                primary_server = each_server
        except Exception as network_unreachable:
            pass


print(primary_server)
with open(result_file_name, 'w+') as result_file:
    # result_string = '{"result":{"primary_server":'+str(primary_server)+',"username":'+str(username)+',"paassword":'+str(password)+',"auth_required":'+str(auth_required)'}}'
    final_json_string = {
        "result": {
            "primary_server": str(primary_server),
            "username": str(username),
            "password": str(password)
        }
    }
    final_string = json.dumps(final_json_string)
    # print(final_string)
    result_file.write(json.dumps(final_json_string))
    result_file.close()