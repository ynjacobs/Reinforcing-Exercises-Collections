rooms = {
     'data': {
          'rooms': [ { 'id': 1, 'room_number': "201", 'capacity': 50}, { 'id': 2, 'room_number': "301", 'capacity': 200 }, { 'id': 3, 'room_number': "1B", 'capacity': 100}
    ],
          'events': [
                { 'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75 },
                { 'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25 },
                { 'id': 3, 'room_id': 2, 'start_time': 10, 'end_time': 18, 'attendees': 20 },
                { 'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56 },
    ]
  }
}

capacity = rooms['data']['rooms'][0]['capacity']
z_room = rooms['data']['rooms'][0]
print(capacity)
 
for event in rooms['data']['events'] :
    if event['room_id'] == z_room['id']:
        if event['attendees'] <= z_room['capacity']:
            print('ok room {} capacity of {} will fit event {} attendes'.format(z_room['id'], z_room['capacity'], event['id']))