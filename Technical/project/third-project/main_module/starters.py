
# Local Imports ...
from main_module.inputs.text_input import datainput
from main_module.datas.data import functionallty
from main_module.llm_module.similar_search import get_key


def starter():
     while True:
          query =  datainput()
          if query == "0":
               return
          key = get_key(query)
          functionallty[key]()
           
