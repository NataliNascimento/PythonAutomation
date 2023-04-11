import pyautogui as posicaoAbreArquivos

#send hotkey win+r
posicaoAbreArquivos.hotkey('win', 'r')

#wait computer response.
posicaoAbreArquivos.sleep(1)

#writing notepad in execution window.
posicaoAbreArquivos.typewrite('Notepad')

#wait computer response.
posicaoAbreArquivos.sleep(1)

#press enter
posicaoAbreArquivos.press('enter')

#waitcomputer response.
posicaoAbreArquivos.sleep(2)

#write message in notepad
posicaoAbreArquivos.write('Notepad open with Python.')

#wait computer response.
posicaoAbreArquivos.sleep(4)

#get active window
fecharBlocoDeNotas = posicaoAbreArquivos.getActiveWindow()

#wait computer response.
posicaoAbreArquivos.sleep(1)

#close notepad
fecharBlocoDeNotas.close()

#wait computer response.
posicaoAbreArquivos.sleep(1)

#press tab
posicaoAbreArquivos.press('tab')

#press enter
posicaoAbreArquivos.press('enter')
