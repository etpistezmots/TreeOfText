import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By


def InterfaceMinimale():
    '''
    Sert juste a arreter le programme proprement
    Attention vraiment old school
    Interface apparaît en bas à droite'''
    root = tk.Tk()

    # POUR AFFICHAGE EN BAS A DROITE
    # plus pratique pour travailler sur ITOL par la suite
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    coordx= str(ws-200)
    coordy = str(hs - 50)
    root.geometry("200x50+" + coordx + "+" + coordy)

    frame = tk.Frame(root)
    frame.pack()


    button = tk.Button(frame,
                   text="FIN DU PROGRAMME",
                   fg="red",
                   command=root.destroy)
    button.pack(side=tk.TOP)
    root.mainloop()


def VersItol(result,pathgecko):
    '''
    Execute le driver et va faire le boulot
    En entrée : resultat du programme sous forme str (format Newick)
              : pathgecko necessaire pour faire marcher le driver sous firefox
    En sortie : le driver pour l'arrêtre proprement par la suite.
    '''
    driver = webdriver.Firefox(executable_path=pathgecko)
    driver.get("https://itol.embl.de")
    driver.find_element(By.XPATH, ".//a[contains(@href,'upload.cgi')]").click()
    element = driver.find_element(By.ID, "tree_text")
    element.send_keys(result)
    driver.find_element(By.XPATH, ".//input[contains(@value,'Upload')]").click()
    return driver

