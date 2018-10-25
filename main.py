# -*- coding: utf-8 -*-
import os
import wx
from general import WorkFile, Start
from WriteScriptJs import JsWrite
from ConnectItol import VersItol



class MyFrameName(wx.Frame):


    def __init__(self, parent, id):

        # Récupère le chemin général du projet
        self.generalpath =__file__[0:len(__file__)-7]

        # Par default
        self.PathData = self.generalpath + os.sep + 'Data' + os.sep + 'tableafcm.csv'
        self.ChoixDist = "Labbe"
        self.ChoixRegroup = "Neigborjoin"
        self.Represent = "phylogram"
        self.Result = ""

        # Met en place la fenêtre initiale qui va être lancé par la MainLoop
        titre = 'Tree of Text !'
        wx.Frame.__init__(self, parent, id, title=titre, pos=(0, 0), size=(800, 800))

        self.panel = wx.Panel(self)

        # Choix du fichier de travail
        button1 = wx.Button(self.panel, label="Choix de votre fichier de travail", pos=(50, 10), size=(300, 40))
        self.Bind(wx.EVT_BUTTON, self.OnWorkFile, button1)
        self.custum1 = wx.StaticText(self.panel, -1, "Fichier en cours : " + self.PathData, (50, 50))


        # Choix de la distance
        self.custum2 = wx.StaticText(self.panel, -1,"Choix du calcul de la distance  : ", (50, 90))
        self.mylistDist = ['Labbe','Jaccard', 'JaccardBrunet']
        self.myListBox1 = wx.ListBox(self.panel, -1, (50, 110), (120, 80), self.mylistDist, wx.LB_SINGLE)
        self.myListBox1.SetSelection(0)
        self.ChoixDist = self.mylistDist[self.myListBox1.GetSelection()]


        # Choix du regroupement
        self.custum3 = wx.StaticText(self.panel, -1, "Choix du calcul de regroupement  : ", (50, 210))
        self.mylistRegroup = ["Neigborjoin","Ward","Ugpma"]
        self.myListBox2 = wx.ListBox(self.panel, -1, (50, 230), (120, 80), self.mylistRegroup, wx.LB_SINGLE)
        self.myListBox2.SetSelection(0)

        # Choix de la représentation
        self.custum4 = wx.StaticText(self.panel, -1, "Choix du mode de représentation : ", (50, 330))
        self.mylistRepresent = ["phylogram","radial"]
        self.myListBox3 = wx.ListBox(self.panel, -1, (50, 350), (120, 50), self.mylistRepresent, wx.LB_SINGLE)
        self.myListBox3.SetSelection(0)

        # Lancement du programme
        button2 = wx.Button(self.panel, label="Start", pos=(50, 420), size=(60, 60))
        self.Bind(wx.EVT_BUTTON, self.OnStart, button2)

        self.custum5 = wx.StaticText(self.panel, -1, "Result sous format Newick: ", pos=(180, 420))
        self.ResultInterface = wx.TextCtrl(self.panel, -1, "", pos=(180, 440), size=(600, 150),
                                           style=wx.TE_MULTILINE)



    def OnWorkFile(self, event):
        WorkFile(self)


    def OnStart(self, event):

        # Suivant ce que l'utilisateur a choisi
        self.ChoixDist = self.mylistDist[self.myListBox1.GetSelection()]
        self.ChoixRegroup = self.mylistRegroup[self.myListBox2.GetSelection()]
        self.Represent = self.mylistRepresent[self.myListBox3.GetSelection()]


        print("Vous avez choisi de travailler avec la distance de  :" + self.ChoixDist)
        print("Vous avez choisi de travailler avec la méthode de regroupement de  :" + self.ChoixRegroup)

        # LANCE LE PROGRAMME
        Start(self)

        # Lance l'interface JavaScript de visualisation
        JsWrite(self.Result,self.Represent)

        # Fait apparaitre nouveau bouton (vers Itol)
        button3 = wx.Button(self.panel, label="Vers \n Itol", pos=(50, 480), size=(60, 60))
        # https://wiki.wxpython.org/Passing%20Arguments%20to%20Callbacks
        button3.Bind(wx.EVT_BUTTON, lambda evt, temp=self.Result: self.OnItol(evt, temp))


    def OnItol(self, event, ResultNewick):
        pathgecko = self.generalpath + os.sep + 'geckodriver'
        VersItol(ResultNewick, pathgecko)



if __name__ == '__main__':

    # affichage graphique sous forme d'une MainLoop qui attend des évènements
    # utilise la librairie d'affichege wx.python
    app = wx.App()
    frame = MyFrameName(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
