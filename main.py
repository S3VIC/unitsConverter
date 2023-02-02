import PySimpleGUI as sg
import params.params as par
import src.convert as conv

def convertEnergy(units, value):
    energyUnitsDict = {
    'eV':1, 'J':1, 'kJ':1, 'MJ':1, 'GJ':1, 'nm':1, '1/cm':1,
    }
    return 0

                            ##### MAIN #####
# Creating app layout
#Each nested list defines a row in layout
layout = [
    [
    sg.Text('Distance convertion')
    ],
    [
    sg.Text('Convert from:'),
    sg.Spin(['pm', 'A', 'nm', 'um', 'mm', 'cm', 'dm', 'm', 'km'], key = '-SPIN1-'),
    sg.Text('To:'),
    sg.Spin(['pm', 'A', 'nm', 'um', 'mm', 'cm', 'dm', 'm', 'km'], key = '-SPIN2-')
    ],
    [sg.Button('Convert', key = '-BUTTON1-')],

    [sg.Text('Mass convertion')],
    [
    sg.Text('Convert from:'),
    sg.Spin(['pg', 'ng', 'ug', 'mg', 'g', 'dag', 'kg', 't'], key = '-SPIN3-'),
    sg.Text('To:'),
    sg.Spin(['pg', 'ng', 'ug', 'mg', 'g', 'dag', 'kg', 't'], key = '-SPIN4-')
    ],
    [sg.Button('Convert', key = '-BUTTON2-')],
    [sg.Input(key = '-INPUT1-')],
    [sg.Text('Converted values will appear here.', key = '-TEXT3-')] ]

# Creating window
window = sg.Window('Python converter', layout)

# Checking for events (ex. button press) in loop
while True:
    event, values = window.read()

# Making sure app will exit loop and finish its working after closing it
    if event == sg.WIN_CLOSED:
        break

# Handling distance and mass convertion, waiting for button being pressed
# and checking whether input string value is convertable to numeric one
    if event == '-BUTTON1-':
        inputValue = values['-INPUT1-']
        if inputValue.isnumeric():
            window['-TEXT3-'].update(conv.convertDistance([values['-SPIN1-'], values['-SPIN2-']], float(inputValue)))

    if event == '-BUTTON2-':
        inputValue = values['-INPUT1-']
        if inputValue.isnumeric():
            window['-TEXT3-'].update(conv.convertMass([values['-SPIN3-'], values['-SPIN4-']], float(inputValue)))

# Closing after exiting loop window
window.close()
