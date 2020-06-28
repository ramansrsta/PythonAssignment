def characterExChanger(str):
    firstletter = str[0]
    lastletter = str[-1]
    remainingletter = str[1:-1]

    print(lastletter+remainingletter+firstletter)

characterExChanger('Ninja')
characterExChanger('Shroud')
characterExChanger('Dynamo')