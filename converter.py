import PySimpleGUI as sg

def convertDistanceDict(units, value):
    unitsDict = {
    'pm':1E12,
    'A' :1E10,
    'nm':1E9,
    'um':1E6,
    'mm':1E3,
    'cm':1E2,
    'dm':1E1,
    'm':1,
    'km':1E-3
    }
    multipliers = []
    for keys in unitsDict:
        if keys == units[0]:
            multipliers.append(unitsDict[keys])
        if keys == units[1]:
            multipliers.append(unitsDict[keys])
    return value * multipliers[1] / multipliers[0]


layout = [
    [
    sg.Text('Distance convertion')
    ],
    [
    sg.Text('First value'),
    sg.Spin(['m', 'g'], key = '-SPIN1'),
    sg.Text('Second value'),
    sg.Spin(['km', 'kg'], key = '-SPIN2-')
    ],

    [sg.Button('Convert', key = '-BUTTON1-')],
    [sg.Input(key = '-INPUT1-')],
    [sg.Text('Converted values will appear here.', key = '-TEXT3-')] ] #Each nested lists  defines a row in layout


window = sg.Window('Python converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        window['-TEXT3-'].update(convertDistanceDict([values['-SPIN1'], values['-SPIN2-']], float(values['-INPUT1-'])))

window.close()
