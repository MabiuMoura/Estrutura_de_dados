class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
        
                #SEGUNDA QUESTAO
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top       
        self.top = new_node


                #TERCEIRA QUESTAO
    def pop(self):
        if self.top:
            poped_node = self.top.data 
            self.top = self.top.next
            return poped_node
        else:
            return None


                #QUARTA QUESTAO
    def peek(self):
        peek_node = self.pop()
        if peek_node:
            print(f"o primeiro item é {peek_node}")
            self.push(peek_node)
        else:
            print("A pilha esta vazia")
            
            
    def mostrar(self):
        if self.top:
            print(f'O valor do nó atual é {self.top.data}')
        else:
            print("A pilha esta vazia")



                #QUINTA QUESTAO
    def isEmpty(self):
        test_node = self.pop()
        if test_node:
            self.push(test_node)
            return False
        else:
            return True
        
        
                
                #SEXTA QUESTAO  
    def len(self):
        aux = self.pop()
        lentgh = 0
        if aux is not None:
            aux_stack = Stack()
            aux_stack.push(aux)
            lentgh = lentgh + 1
            while True:
                aux = self.pop()
                if aux is not None:
                    aux_stack.push(aux)
                    lentgh = lentgh + 1
                else:
                    break
            while True:
                aux = aux_stack.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break
        print(f"O tamanho da fila elementar é {lentgh}")
        
        
        
                    #SETIMA QUESTAO
    def last(self):
        aux = self.pop()
        if aux is not None:
            aux_stack = Stack()
            aux_stack.push(aux)
            last = aux
            while True:
                aux = self.pop()
                if aux is not None:
                    aux_stack.push(aux)
                    last = aux
                else:
                    break
            print(f"O ultimo elemento da pilha é {last}")
            while True:
                aux = aux_stack.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break
        else:
            print("A pilha não possui nenhum elemento")
            
            
            
            
            
                    #OITAVA QUESTAO
    def getValueByIndex(self,idx):
        aux = self.pop()
        if aux is not None:
            i = 0
            value = None
            aux_stack = Stack()
            aux_stack.push(aux)
            while True:
                if i == idx:
                    value = aux    
                aux = self.pop()
                if aux is not None: 
                    aux_stack.push(aux)  
                else:
                    break
                i += 1
                
            while True:
                aux = aux_stack.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break
            if value is not None:    
                print(f"O elemento na posição {idx} é :{value}")
            else:
                print("A pilha tao possui essa posição")
                
                
                
                    #NONA QUESTAO
    def getIndexByValue (self,valor):
        valor = str(valor)
        aux = self.pop()
        if aux is not None:
            count = 0
            index = []
            aux_stack = Stack()
            aux_stack.push(aux)
            if aux == valor:
                index.append(count)
            while True:
                aux = self.pop()
                count += 1
                if aux is not None:
                    aux_stack.push(aux)
                    if aux == valor:
                        index.append(count)
                else:
                    break
            while True:
                aux = aux_stack.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break
            print(f"O valor {valor} se encontra na posição :{index[0]}")
        else:
            print("O valor não se encontra na pilha")
            
            

                            #DECIMA QUESTAO
    def getAllIndexByValue (self, valor):
        valor = str(valor)
        aux = self.pop()
        if aux is not None:
            count = 0
            index = []
            aux_stack = Stack()
            aux_stack.push(aux)
            if aux == valor:
                index.append(count)
            while True:
                aux = self.pop()
                count += 1
                if aux is not None:
                    aux_stack.push(aux)
                    if aux == valor:
                        index.append(count)
                else:
                    break
            while True:
                aux = aux_stack.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break
            print(f"O valor {valor} se encontra nas posições :{index}")
        else:
            print("A pilha esta vazia")
            
                        #NOVAS
            
            
            
                    #TREZE
    def removeAll (self):
        aux = self.pop
        if aux is not None:
            while aux is not None:
                aux = self.pop
            print("A pilha foi esvaziada")
        else:
            print("A pilha ja estava vazia")
 
 
                    #CATORZE
    def removeByIndex(self,idx):
        aux = self.pop()
        if aux is not None:
            aux_stack = Stack()
            count = 0
            removed = []
            if count == idx:
                removed.append(aux)
                aux = self.pop()
            aux_stack.push(aux)
            count += 1
            while True:
                aux = self.pop()
                if aux is not None:
                    if count == idx:
                        removed.append(aux)
                        aux = self.pop()
                        if aux is None:
                            break
                    aux_stack.push(aux)
                    count += 1
                else:
                    break
            while True:
                aux = aux_stack.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break
            if removed is not None:    
                print(f"O elemento da posição {idx} que foi removido é :{removed[0]}")
            else:
                print("A pilha tao possui essa posição")    
                
                
                
                    #QUINTA
    def removeByValue (self,valor):
        valor = str(valor)
        aux = self.pop()
        if aux is not None:
            removed = None
            aux_stack = Stack()
            if aux == valor:
                removed = aux
                aux = self.pop()
            aux_stack.push(aux)
            while True:
                aux = self.pop()
                if aux == valor:
                    if removed is None:
                        removed = aux
                        aux = self.pop()
                if aux is not None:
                    aux_stack.push(aux)
                else:
                    break
            
            while True:
                aux = aux_stack.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break
            print(f"O valor {removed} foi removido")
        else:
            print("O valor não se encontra na pilha")
            
            
            
            #QUESTAO 16
    def removeAllByValue(self,value):
        valor = str(valor)
        aux = self.pop()
        if aux is not None:
            removed = []
            aux_stack = Stack()
            if aux == valor:
                removed.append(aux)
                aux = self.pop()
            aux_stack.push(aux)
            while True:
                aux = self.pop()
                if aux == valor:
                    removed.append(aux)
                    aux = self.pop()
                if aux is not None:
                    aux_stack.push(aux)
                else:
                    break
            
            while True:
                aux = aux_stack.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break
            print(f"O valor {removed[0]} foi removido")
        else:
            print("O valor não se encontra na pilha")
            
            
            
                    #QUESTAO 18
    def removeAllBySlice (self,inicio,fim):
        aux = self.pop()
        if aux is not None:
            count = 0
            test = []
            aux_stack = Stack()
            if count == inicio:
                while count != fim:
                    test.append(self.pop())
                    count += 1
                    if test is None:
                        break
                aux = self.pop()
            aux_stack.push(aux)
            count += 1
            while True:
                aux = self.pop()
                if count == inicio:
                    while count != fim:
                        test.append(self.pop())
                        count += 1
                        if test is None:
                            break
                if aux is not None:
                    aux_stack.push(aux)
                else:
                    break
            
            while True:
                aux = aux_stack.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break
                
            print(f"Os valores entre {inicio} e {fim} removidos foram {test}")
        else:
            print("A pilha ta vazia")
                
                
                

                