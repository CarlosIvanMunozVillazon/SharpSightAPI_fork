import json
from Scrapping import Search
from data import Results,ResultsAVL
import menu

def __init__():
    #menu.startMenu()
    #print(resulAVL_imp.orderListPrice())
    #Search.Search("Nintendo Switch")
    resulAVL_imp = ResultsAVL.results_AVL_imp()
    print(resulAVL_imp.preOrder_JSON())
    


__init__()
