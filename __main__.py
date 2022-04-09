# import serial
import voicemeeter

# Can be 'basic', 'banana' or 'potato'

kind = 'potato'

# Ensure that Voicemeeter is launched
# voicemeeter.launch(kind)

with voicemeeter.remote(kind) as vmr:
    def get_ver():
        ver = ''
        for i in range(4):
            ver += str(vmr.version[i])
            ver += '.'
        ver = ver[:-1]
        return ver

    vmr.apply({
        'in-0': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True),
        'in-1': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True),
        'in-2': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True),
        'in-3': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True),
        'in-4': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True),
        'in-5': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True),
        'in-6': dict(A1=True, A2=True, A3=True, A4=True, A5=True, B1=True,
                     B2=True, B3=True)
    })

    vmr.apply({
        'in-0': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False),
        'in-1': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False),
        'in-2': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False),
        'in-3': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False),
        'in-4': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False),
        'in-5': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False),
        'in-6': dict(A1=False, A2=False, A3=False, A4=False, A5=False, B1=False,
                     B2=False, B3=False)
    })

    parameter = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'Mute', 'Mono', 'Solo']

    for j in range(len(parameter)):
        for i in range(8):
            print('Strip[' + str(i) + '].' + parameter[j])
            vmr.set('Strip[' + str(i) + '].' + parameter[j], 1)
    for j in range(len(parameter)):
        for i in range(8):
            print('Strip[' + str(i) + '].' + parameter[j])
            vmr.set('Strip[' + str(i) + '].' + parameter[j], 0)
