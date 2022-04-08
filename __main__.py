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
        'in-5': dict(A1=True)
    })

    print(get_ver())

    # Resets all UI elements to a base profile
    # vmr.reset()
