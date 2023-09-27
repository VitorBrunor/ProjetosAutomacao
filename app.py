import pyautogui
from time import sleep

pyautogui.click(974,540,duration=2)
pyautogui.write('VitorBrunor')

pyautogui.click(977,567,duration=2)
pyautogui.write('110202')

pyautogui.click(872,595,duration=2)

with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(669,529,duration=2)
        pyautogui.write(produto)

        pyautogui.click(677,555,duration=2)
        pyautogui.write(quantidade)

        pyautogui.click(596,742,duration=2)
        pyautogui.write(preco)

        pyautogui.click(591,741,duration=2)

        sleep(1)

        # Tem um problema. Ele registra o produto após ter digitado somente o produto e a quantidade. e ainda coloca o preço no lugar da q  quantidade e registra de novo

