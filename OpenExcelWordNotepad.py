# this project will open excel, word or notepad according selection.
# the positions of click will change according your window distribuition.
# to get the position of your Windows button use print(choiceOption.position()) command.

import pyautogui as choiceOption

option = choiceOption.confirm('Select the application that you want to open.',
                              buttons=['Excel', 'Word', 'Notepad'])

choiceOption.hotkey('win', 'r')
choiceOption.sleep(1)

if option == 'Excel':

    choiceOption.typewrite('excel')
    choiceOption.sleep(1)
    choiceOption.press('enter')
    choiceOption.sleep(2)
#   print(choiceOption.position())
    choiceOption.click(x=241, y=223)
    choiceOption.sleep(2)
    choiceOption.typewrite('Excel option selected.')
    choiceOption.sleep(1)
    choiceOption.hotkey('enter')
    choiceOption.sleep(1)
    closeExcel = choiceOption.getActiveWindow()
    closeExcel.close()
    choiceOption.sleep(2)
#   print(choiceOption.position())
    choiceOption.click(x=1023, y=640)


elif option == 'Word':

    choiceOption.typewrite('winword')
    choiceOption.sleep(1)
    choiceOption.press('enter')
    choiceOption.sleep(2)
#   print(choiceOption.position())
    choiceOption.click(x=294, y=204)
    choiceOption.sleep(2)
    choiceOption.typewrite('Word option selected.')
    choiceOption.sleep(1)
    closeWord = choiceOption.getActiveWindow()
    closeWord.close()
    choiceOption.sleep(2)
#   print(choiceOption.position())
    choiceOption.click(x=1023, y=640)

else:

    choiceOption.typewrite('notepad')
    choiceOption.sleep(1)
    choiceOption.press('enter')
    choiceOption.sleep(3)
    choiceOption.typewrite('Notepad option selected.')
    choiceOption.sleep(1)
    closeNotepad = choiceOption.getActiveWindow()
    closeNotepad.close()
    choiceOption.sleep(2)
    choiceOption.hotkey('tab')
    choiceOption.sleep(1)
    choiceOption.hotkey('enter')

print('End of workflow')

