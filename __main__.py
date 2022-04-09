import serial
import time
import voicemeeter

# Can be 'basic', 'banana' or 'potato'

kind = 'potato'

# Ensure that Voicemeeter is launched
# voicemeeter.launch(kind)

with voicemeeter.remote(kind) as vmr:

    arduino = serial.Serial(port='COM15', baudrate=115200, timeout=0.1)

    def get_ver():
        ver = ''
        for i in range(4):
            ver += str(vmr.version[i])
            ver += '.'
        ver = ver[:-1]
        return ver


    def get_input_gain():
        gain = []
        for i in range(4):
            gain.append(vmr.get('Strip[' + str(i+3) + '].Gain'))
        return gain


    def write_read(x):
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
        data = arduino.readline()
        return data

    while True:
        num = input("enter a number: ")
        value = write_read(num)
        print(value)

    while 1:
        if vmr.dirty:
            print(get_input_gain())

    vmr.apply({
        'in-0': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True, mono=True, solo=True, mute=True),
        'in-1': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True, mono=True, solo=True, mute=True),
        'in-2': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True, mono=True, solo=True, mute=True),
        'in-3': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True, mono=True, solo=True, mute=True),
        'in-4': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True, mono=True, solo=True, mute=True),
        'in-5': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True, mono=True, solo=True, mute=True),
        'in-6': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True, mono=True, solo=True, mute=True),
        'in-7': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True, mono=True, solo=True, mute=True)
    })

    vmr.apply({
        'in-0': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False, mono=False, solo=False, mute=False),
        'in-1': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False, mono=False, solo=False, mute=False),
        'in-2': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False, mono=False, solo=False, mute=False),
        'in-3': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False, mono=False, solo=False, mute=False),
        'in-4': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False, mono=False, solo=False, mute=False),
        'in-5': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False, mono=False, solo=False, mute=False),
        'in-6': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False, mono=False, solo=False, mute=False),
        'in-7': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False, mono=False, solo=False, mute=False)
    })

    parameter = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1',
                 'B2', 'B3', 'Mono', 'Solo', 'Mute']

    for j in range(len(parameter)):
        for i in range(8):
            # print('Strip[' + str(i) + '].' + parameter[j])
            vmr.set('Strip[' + str(i) + '].' + parameter[j], 1)
    print(vmr.get('Strip[1].A1', False))

    for j in range(len(parameter)):
        for i in range(8):
            # print('Strip[' + str(i) + '].' + parameter[j])
            vmr.set('Strip[' + str(i) + '].' + parameter[j], 0)
    print(vmr.get('Strip[1].A1', False))
    for i in range(8):
        for j in range(len(parameter)):
            # print('Strip[' + str(i) + '].' + parameter[j])
            vmr.set('Strip[' + str(i) + '].' + parameter[j], 1)
    print(vmr.get('Strip[1].A1', False))
    for i in range(8):
        for j in range(len(parameter)):
            # print('Strip[' + str(i) + '].' + parameter[j])
            vmr.set('Strip[' + str(i) + '].' + parameter[j], 0)
    print(vmr.get('Strip[1].A1', False))
    '''for i in range(8):
        for j in range(len(parameter)):
            # print('Strip[' + str(i) + '].' + parameter[j])
            vmr.set('Strip[' + str(i) + '].' + parameter[j], 1)'''

