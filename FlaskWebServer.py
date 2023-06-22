from flask import Flask, request
from drone_program import Connect_vehicle

app = Flask(__name__)

droneObj=Connect_vehicle()

def convertToIncValue(val):
    return int((val*500)+1500)

def convertToDecValue(val):
    return int(((val+1)*500)+1000)

@app.route('/arm', methods=['POST'])
def Receive_and_send_commands_arm():
    data = request.json
    print(data)
    if(data["message"]=="ArmDrone"):
        droneObj.armDrone()
    else:
        return {'message':'Invalid input'}
    return data

@app.route('/throttle', methods=['POST'])
def Receive_and_send_commands_throttle():
    data = request.json
    print(data['body'])
    print(type(data['body']))
    if(data['body']=="IncThrottle"):
        droneObj.changeThrottle(10)
    elif(data['body']=="DecThrottle"):
        droneObj.changeThrottle(-10)
    else:
        return {'message':'Invalid input'}
    return data
    


@app.route('/rudder', methods=['POST'])
def Receive_and_send_commands_rudder():
    data = request.json
    print(data['body'])
    print(type(data['body']))
    try:
        rudder = float(data['body'])
        if(rudder>0 and rudder<=1):
            droneObj.changeRudder(convertToIncValue(rudder))
        elif(rudder<=0 and rudder>=-1):
            droneObj.changeRudder(convertToDecValue(rudder))
        else:
            return {'message': 'Invalid input, only float values between -1 and 1 accepted'}
        return data
    except ValueError:
        return {'message':'Invalid input, only float values between -1 and 1 accepted'}


@app.route('/elevator', methods=['POST'])
def Receive_and_send_commands_elevator():
    data = request.json
    print(data)
    try:
        elevator = float(data['body'])
        if(elevator>0 and elevator<=1):
            droneObj.changeElevation(convertToIncValue(elevator))
        elif(elevator<=0 and elevator>=-1):
            droneObj.changeElevation(convertToDecValue(elevator))
        else:
            return {'message': 'Invalid input, only float values between -1 and 1 accepted'}
        return data
    except ValueError:
        return {'message':'Invalid input, only float values between -1 and 1 accepted'}

@app.route('/aileron', methods=['POST'])
def Receive_and_send_commands_aileron():
    data = request.json
    print(data['body'])
    print(type(data['body']))
    try:
        aileron = float(data['body'])
        if(aileron>0 and aileron<=1):
            droneObj.changeAileron(convertToIncValue(aileron))
        elif(aileron<=0 and aileron>=-1):
            droneObj.changeAileron(convertToDecValue(aileron))
        else:
            return {'message': 'Invalid input, only float values between -1 and 1 accepted'}
        return data
    except ValueError:
        return {'message':'Invalid input, only float values between -1 and 1 accepted'}
    
