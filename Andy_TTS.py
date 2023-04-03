import PySimpleGUI as sg


sg.theme("GreenTan")
font = ('Monaco',18)

layout = [
         [sg.Text('INPUT YOUR TEXT')],
          [sg.Input(key= '-INPUT-')],
          [ sg.Text('Adjust Speed'),sg.Slider(range=(150, 400), 
                orientation='h', size=(50, 10), enable_events=True, key = '-SPEED-', default_value= 150) ],
          [sg.Button('Speak', bind_return_key=True), sg.Button('EXIT')],
          [sg.Text('Select Voice Type'),sg.Radio('MALE VOICE', "RADIO1", default=False, key="-R1-"),sg.Radio('FEMALE VOICE', "RADIO1", default=True, key="-R2-")],
           
          ]
 
window = sg.Window("TEXT TO SPEECH APP", layout,font=font)

while True:
    event, values =window.read()

    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event == 'Speak'and values["-R1-"] == True :
        import pyttsx3
        tts=pyttsx3.init()
        input_value = values['-INPUT-']
        rate= values['-SPEED-']
        tts.setProperty('rate',rate)
        voices = tts.getProperty('voices')
        tts.setProperty('voice', voices[0].id)
        tts.say(input_value)
        tts.runAndWait()
    elif event == 'Speak'and values["-R2-"] == True:
        import pyttsx3
        tts=pyttsx3.init()
        input_value = values['-INPUT-']
        rate= values['-SPEED-']
        tts.setProperty('rate',rate)
        voices = tts.getProperty('voices')
        tts.setProperty('voice', voices[1].id)
        tts.say(input_value)
        tts.runAndWait()
    

window.close()
       




