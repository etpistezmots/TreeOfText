# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By


def VersItol(result,pathgecko):
    '''
    Execute le driver et va faire le boulot
    En entrée : resultat du programme sous forme str (format Newick)
              : pathgecko necessaire pour faire marcher le driver sous firefox
    '''
    driver = webdriver.Firefox(executable_path=pathgecko)
    driver.get("https://itol.embl.de")
    driver.find_element(By.XPATH, ".//a[contains(@href,'upload.cgi')]").click()
    element = driver.find_element(By.ID, "tree_text")
    element.send_keys(result)
    driver.find_element(By.XPATH, ".//input[contains(@value,'Upload')]").click()

