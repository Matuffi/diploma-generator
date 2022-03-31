import PySimpleGUI as sg

sg.theme("Dark Amber")
#
# layout = [
# [sg.Text("Filename")],
# [sg.Input(), sg.FileBrowse()],
# [sg.OK(), sg.Button("Exit")]
# ]
#
# window = sg.Window("Title", layout)
#
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == "Exit":
#         break
#     print(event, values)
#
# window.close()
#
# sg.Popup(event,values[0])

##############################

layout = [
[sg.Text("Your typed: "), sg.Text(size=(12,1), key="-OUT-")],
[sg.Input(key="-IN-")],
[sg.Text(key="file1"), sg.FileBrowse(key="-BROWSE-", target="file1")],
[sg.Button("Show"), sg.Button("Exit")]
]

window = sg.Window("Title", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    if event == "Show":
        window["-OUT-"].update(values["-IN-"])
        print(values["-BROWSE-"])

window.close()
