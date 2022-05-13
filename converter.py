import PySimpleGUI as sg 

def convertDistance(units, value):
    match units[0]:
        case 'pm':
            return 0
        case 'nm':
            return 0
        case 'um':
            return 0
        case 'mm':
            return 0
        case 'cm':
            return 0
        case 'dm':
            return 0
        case 'm':
            match units[1]:
                case 'km':
                    return value / 1E3
        case 'km':
            return 0
        case 'ly':
            return 0



layout = [
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
        window['-TEXT3-'].update(convertDistance([values['-SPIN1'], values['-SPIN2-']], float(values['-INPUT1-'])))

window.close()
