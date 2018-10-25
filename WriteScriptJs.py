# -*- coding: utf-8 -*-

import os

def JsWrite(result,choix):

    textresultchoix1=""
    textresultchoix2=""

    if choix == "phylogram":
        textresultchoix1 = ''' d3.phylogram.build('#phylogram', newick, {
          width: 800,
          height: 600
        }); '''

        textresultchoix2 = ''' <h1>Phylogram</h1>
         <div id='phylogram'></div> '''

    if choix == "radial":
        textresultchoix1 = ''' d3.phylogram.buildRadial('#radialtree', newick, {
          width: 800,
          height: 600
        }); '''

        textresultchoix2 = ''' <h1>Circular Dendrogram</h1>
         <h2>Test</h2>
         <div id='radialtree'></div> '''


    txt = '''<!DOCTYPE html>
<html lang='en' xml:lang='en' xmlns='http://www.w3.org/1999/xhtml'>
  <head>
    <meta content='text/html;charset=UTF-8' http-equiv='content-type'>
    <title>Right-angle phylograms and dendrograms with d3</title>
    <script src="http://d3js.org/d3.v3.min.js" type="text/javascript"></script>
    <script src="newick.js" type="text/javascript"></script>
    <script src="d3.phylogram.js" type="text/javascript"></script>
    <script>
      function load() {
        var newick = Newick.parse(" ''' + result + '''")
        var newickNodes = []
        function buildNewickNodes(node, callback) {
          newickNodes.push(node)
          if (node.branchset) {
            for (var i=0; i < node.branchset.length; i++) {
              buildNewickNodes(node.branchset[i])
            }
          }
        }
        buildNewickNodes(newick)
        ''' + textresultchoix1 + '''}
    </script>
    <style type="text/css" media="screen">
      body { font-family: "Helvetica Neue", Helvetica, sans-serif; }
    </style>
  </head>
  <body onload="load()">'''\
      + textresultchoix2 + '''
  </body>
</html>
'''

    AdresseJsFile = os.getcwd() + os.sep + 'Js' + os.sep + 'index.html'

    Html_file= open(AdresseJsFile,"w")
    Html_file.write(txt)
    Html_file.close()

    os.system("firefox " + AdresseJsFile)

