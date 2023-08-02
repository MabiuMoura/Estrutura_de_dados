                        #FILA
                        #PRIMEIRA QUESTAO
class Fila:
    def __init__(self):
        self.tail = None
        self.head = None
        self.datas = []
        
        
                        #SEGUNDA QUESTAO
    def InsertWithArray(self,data):
        self.datas.append(data)
        if self.head:
            index = (len(self.datas) -1)
            self.tail = self.datas[index]
        else:
            self.head = data
            self.tail = data
            
            
            
                        #TERCEIRA QUESTAO
    def remove(self):
        if self.datas:
            self.datas.pop(0)
            if self.datas:
                self.head = self.datas[0]
                index = (len(self.datas) -1)
                self.tail = self.datas[index]
            else:
                self.head = None
                self.tail = None
            
            
    def mostrar(self):
        if self.head:
            print(f"O primeiro item da fila é: {self.head} e o ultimo item é: {self.tail}")
            print(f"a fila toda é {self.datas}")
            
    
    
                      #QUARTA QUESTAO
    def first(self):
        if self.datas:
            print(f"O primeira elemento da fila é {self.head}")
        else:
            print("A fila esta vazia")
        
        
        
                    #QUINTA QUESTAO
    def isEmpty(self):
        if self.datas:
            print("A fila não esta vazia")
        else:
            print("A fila esta vazia")


                    #SEXTA QUESTAO  
    def len(self):
        lentgh = len(self.datas)
        print(f"O tamanha da Fila diversa é {len(self.datas)}")




                    #SETIMA QUESTAO
    def last(self):
        if self.datas is not None:
            print(f"O ultimo elemento da Fila é {self.tail}")
        else:
            print("A fila nao possui elementos")
            
            
            
                    #OITAVA QUESTAO
    def getValueByIndex(self,idx):
        x = (len(self.datas) - 1)
        if idx > x:
            print("O valor digitado é maior que o tamanho da Fila")
        else:
            print(f"O valor da Fila na posição {idx} é :{self.datas[idx]}")
            
            
                    #NONA QUESTAO
    def getIndexByValue (self ,value):
        value = str(value)
        if self.datas is not None:
            print(f"O valor {value} se encontro na index {self.datas.index(value)}")
        else:
            print("O valor não se encontra na Fila")
            
                        #NOVAS
            
            
                    #TREZE
    def removeAll(self):
        if self.datas is not None:
            self.datas.clear()
            print("A fila foi esvaziada")
        else:
            print("A fila ja estava vazia")
            
            
                #CATORZE
    def removeByIndex (self,idx):
        if self.datas is not None:
            aux = self.datas.pop(idx)
            if aux is not None:
                print(f"O valor {aux} que estava na posição {idx} foi removido")
            else:
                print("A fila nao tem essa posição")
        else:
            print("A fila ta vazia")        

                
                #QUINZE
    def removeByValue (self,value):
        value = str(value)
        if self.datas is not None:
            self.datas.remove(value)
            print(f"O valor {value} foi removido")
        else:
            print("A fila ta vazia ")
            
            
                #questao 16
    def removeAllbyValue (self,value):
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
            print("a fila ta vazia")