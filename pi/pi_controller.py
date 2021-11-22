import requests
import time
import random
from sense_hat import SenseHat
sense = SenseHat()


# Replace with your own function in Part 1
def get_direction():
    d_long = 0
    d_la = 0
    send_vel = False
    
    while True: 
        for event in sense.stick.get_events():
            print(event.direction, event.action)

            if event.action == "pressed":
                
                if event.direction == "up":
                    send_vel = True
                    d_long = 0
                    d_la = 1
                elif event.direction == "left":
                    send_vel = True
                    d_long = -1
                    d_la = 0
                
                elif event.direction == "right":
                    send_vel = True
                    d_long = 1
                    d_la = 0
                
                elif event.direction == "down":
                    send_vel = True
                    d_long = 0
                    d_la = -1
                else:
                    d_long = 0
                    d_la = 0
                    send_vel = False
                return d_long, d_la, send_vel

if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"
    while True:
        d_long, d_la, send_vel = get_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)
