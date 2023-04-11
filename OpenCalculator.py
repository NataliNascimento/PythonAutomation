#this project will open calulator.
#the positions of click will change according your window distribuition.

import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#wait computer response.
tempoEspera.sleep(1)

#move mouse to the Window button, it's not necessary to move the mouse button because the click function automatically move the mouse button.
#posicaoMouse.moveTo(680, 1058)

#wait computer response.
#tempoEspera.sleep(1)

#clicking windows button. This position changes according your computer.
#To get the position of your Windows button use print(posicaoMouse.position()) command.
posicaoMouse.click(680, 1058)

#wait computer response.
tempoEspera.sleep(1)

#writing application name, in this case calculator.
posicaoMouse.typewrite('calculadora')

#wait computer response.
tempoEspera.sleep(2)

#clicking calculator application.
posicaoMouse.click(696, 481)
