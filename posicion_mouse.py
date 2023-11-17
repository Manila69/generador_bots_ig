ok = input('cuando toques la Q luego de 5 seg se tomara la ubicacion: ')
if ok == 'q':
    time.sleep(5)
    current_position = pyautogui.position()
print(f"Posición actual del mouse: {current_position}"
