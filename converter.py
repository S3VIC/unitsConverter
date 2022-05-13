import PySimpleGUI as sg 

def convertDistance(units, value):
    return {
        'km' : value * 1E-3,
        'nm' : value * 1E9
    }.get(units[1], "Error!")


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