import os.path, datetime
import PySimpleGUI as sg

def editWindow():
    editLayout = [
        [sg.Text("Customer name: "), sg.Input(k="-CxName-")],
        [sg.Text("Customer phone:"), sg.Input(k="-CxPhone-")],
        [sg.Text("Customer email: "), sg.Input(k="-CxEmail-")],
        [sg.Text("Case number:    "), sg.Input(k="-CxCase-")],
        [sg.HSep()],
        [sg.Text("Problem Description:")],
        [sg.Multiline(k="-CxProblem-", size=(60,10))],
        [sg.HSep()],
        [sg.Text("Actions Taken:")],
        [sg.Multiline(k="-Actions-", size=(60,10))],
        [sg.HSep()],
        [sg.Text("Next Steps:")],
        [sg.Multiline(k="-Steps-", size=(60,10))],
        [sg.Button("Save"), sg.Button("Preview"), sg.Button("Clear fields")]
    ]

    editWindow = sg.Window(" ", editLayout)

    while True:
        eventEdit, valuesEdit = editWindow.read()
        if eventEdit == sg.WIN_CLOSED or eventEdit == "Exit":
            break

        if eventEdit == "Save":
            cwd = os.getcwd()
            if str(datetime.date.today().year) not in os.listdir():
                os.mkdir(str(datetime.date.today().year))
            os.chdir(str(datetime.date.today().year))

            if datetime.date.today().strftime("%B") not in os.listdir():
                os.mkdir(datetime.date.today().strftime("%B"))
            os.chdir(datetime.date.today().strftime("%B"))

            if str(datetime.date.today()) not in os.listdir():
                os.mkdir(str(datetime.date.today()))
            os.chdir(str(datetime.date.today()))

            if "{i}.txt".format(i=valuesEdit["-CxCase-"]) not in os.listdir():
                if inputFieldCheck(valuesEdit["-CxCase-"]) is False:
                    file = open("{i}.txt".format(i=valuesEdit["-CxCase-"]), "w")
                    file.write("Customer name: {i} \
                    \nCustomer phone: {j} \nCustomer email: {k} \
                    \nCase number: {l}\n__________________________________________________\
                    \nProblem Description:\
                    \n{m}__________________________________________________\
                    \nActions Taken:\
                    \n{n}__________________________________________________\
                    \nNext Steps:\
                    \n{o}__________________________________________________"\
                    .format(i=valuesEdit["-CxName-"], j=valuesEdit["-CxPhone-"],
                    k=valuesEdit["-CxEmail-"], l=valuesEdit["-CxCase-"],
                    m=valuesEdit["-CxProblem-"], n=valuesEdit["-Actions-"],
                    o=valuesEdit["-Steps-"]))
                    file.close()
                    sg.Popup("File saved", title=" ")

            elif "{i}.txt".format(i=valuesEdit["-CxCase-"]) in os.listdir():
                fileSaveYesNo = sg.popup_yes_no("File already exists, confirm rewrite?", title="")
                if fileSaveYesNo == "Yes":
                    file = open("{i}.txt".format(i=valuesEdit["-CxCase-"]), "w+")
                    file.write("Customer name: {i} \
                    \nCustomer phone: {j} \nCustomer email: {k} \
                    \nCase number: {l}\n__________________________________________________\
                    \nProblem Description:\
                    \n{m}__________________________________________________\
                    \nActions Taken:\
                    \n{n}__________________________________________________\
                    \nNext Steps:\
                    \n{o}__________________________________________________"\
                    .format(i=valuesEdit["-CxName-"], j=valuesEdit["-CxPhone-"],
                    k=valuesEdit["-CxEmail-"], l=valuesEdit["-CxCase-"],
                    m=valuesEdit["-CxProblem-"], n=valuesEdit["-Actions-"],
                    o=valuesEdit["-Steps-"]))
                    file.close()
                    sg.Popup("File saved", title=" ")

                elif fileSaveYesNo == "No":
                    fileSaveYesNo = sg.WIN_CLOSED
            os.chdir(cwd)

        if eventEdit == "Preview":
            previewWindow(valuesEdit["-CxName-"], valuesEdit["-CxPhone-"],
            valuesEdit["-CxEmail-"], valuesEdit["-CxCase-"], valuesEdit["-CxProblem-"],
            valuesEdit["-Actions-"], valuesEdit["-Steps-"])

        if eventEdit == "Clear fields":
            cwd = os.getcwd()
            os.chdir(str(datetime.date.today().year)+"/"+datetime.date.today().strftime("%B")+"/"+str(datetime.date.today()))
            if str(valuesEdit["-CxCase-"])+".txt" not in os.listdir():
                answer = sg.popup_yes_no("Confirm clear fields without saving:", title="")
                if answer == "Yes":
                    editWindow["-CxName-"].update("")
                    editWindow["-CxPhone-"].update("")
                    editWindow["-CxEmail-"].update("")
                    editWindow["-CxCase-"].update("")
                    editWindow["-CxProblem-"].update("")
                    editWindow["-Actions-"].update("")
                    editWindow["-Steps-"].update("")

                if answer == "No":
                    answer = sg.WIN_CLOSED

            else:
                editWindow["-CxName-"].update("")
                editWindow["-CxPhone-"].update("")
                editWindow["-CxEmail-"].update("")
                editWindow["-CxCase-"].update("")
                editWindow["-CxProblem-"].update("")
                editWindow["-Actions-"].update("")
                editWindow["-Steps-"].update("")
            os.chdir(cwd)

def previewWindow(name, phone, email, case, problem, actions, next):
    previewLayout = [
    [sg.Text("NOTE: Any changes made here will NOT be saved!")],
    [sg.Multiline("Customer name: {i} \
    \nCustomer phone: {j} \nCustomer email: {k} \
    \nCase number: {l}\n__________________________________________________\
    \nProblem Description:\
    \n{m}__________________________________________________\
    \nActions Taken:\
    \n{n}__________________________________________________\
    \nNext Steps:\
    \n{o}__________________________________________________"\
    .format(i=name, j=phone,
    k=email, l=case,
    m=problem, n=actions,
    o=next), size=(50,40))]
    ]

    previewWindow = sg.Window(" ", previewLayout)

    while True:
        previewEdit, previewEdit = previewWindow.read()
        if previewEdit == sg.WIN_CLOSED or previewEdit == "Exit":
            break

def inputFieldCheck(inputField):
    if inputField.isnumeric() is False or len(inputField) != 8:
        sg.Popup("Case number can only be numeric", title=" ")
        return True
    return False

if __name__ == '__main__':
    editWindow()
