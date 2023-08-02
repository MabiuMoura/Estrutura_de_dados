                                     #DIVERSA
                    #PRIMEIRA QUESTAO
class Pilha:
    def __init__(self):
        self.top = None
        self.datas = [] 
        
        
                    #SEGUNDA QUESTAO
    def push(self,data):
        self.top = data
        self.datas.append(data)
            

                    #TERCEIRA QUESTAO
    def pop(self):
        if self.datas:
            index = (len(self.datas) - 1)
            self.datas.pop(index)
            if self.datas:
                self.top = self.datas[index-1]
            else:
                self.top = None
        else:
            print("A pilha esta vazia,entao não da para fazer um pop")

        
        
    def mostrar(self):
        if self.datas:
            print(f"O topo da pilha é {self.top}")
            print(f"A pilha toda é {self.datas}")
            
            
            
            
                        #QUARTA QUESTAO
    def peek(self):
        if self.datas:
            print(f"o primeiro elemento é : {self.top}")
        else:
            print("A pilha esta vazia")
            
            
            
            
                        #QUINTA QUESTAO
    def isEmpty(self):
        if self.datas:
            print("A pilha não esta vazia")
        else:
            print("A pilha esta vazia")
            
            
            
                        #SEXTA QUESTAO
    def len(self):
        lentgh = len(self.datas)
        print(f"O tamanha da pilha diversa é {len(self.datas)}")
            
            
            
            
                        #SETIMA QUESTAO
    def last(self):
        if self.datas is not None:
            print(f"O ultimo elemento da pilha é {self.datas[0]}")
        else:
            print("A pilha nao possui nenhum elemento")
            
            
            
                        #OITAVA QUESTAO
    def getValueByIndex(self,idx):
        x = (len(self.datas) - 1)
        if idx > x:
            print("O valor digitado é maior que o tamanho da pilha")
        else:
            print(f"O valor da pilha na posição {idx} é :{self.datas[idx]}")
            return self.datas[idx]
            
            

                        #NONA QUESTAO
    def getIndexByValue(self,value):
        value = str(value)
        if self.datas is not None:
            print(f"O valor {value} se encontro na index {self.datas.index(value)}")
        else:
            print("O valor não se encontra na pilha")
            
                #NOVAS
                        
                            #TREZE
    def removeAll(self):
        if self.datas is not None:
            self.datas.clear()
            print("A pilha foi esvaziada")
        else:
            print("A pilha ja estava vazia")



                            #CATORZE
    def removeByIndex(self,idx):
        if self.datas is not None:
            aux = self.datas.pop(idx)
            if aux is not None:
                print(f"O valor {aux} que estava na posição {idx} foi removido")
            else:
                print("A pilha nao tem esse index")
        else:
            print("A pilha ta vazia")
            
            
            
                    #QUINZE
    def removeByValue (self,value):
        value = str(value)
        if self.datas is not None:
            self.datas.remove(value)
            print(f"O valor {value} foi removido")
        else:
            print("A pilha ta vazia")
        
            #QUESTAO 16
    def removeAllByValue(self,value):
        value = str(value)
        if self.datas is not None:
            while True:
                idx = self.datas.index(value)
                if idx is not None:
                    self.datas.pop(idx)
                else:
                    break
            print("valor removido")
        else:
            print("a pilha ta vazia")