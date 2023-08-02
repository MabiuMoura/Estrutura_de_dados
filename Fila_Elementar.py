class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None


                #SEGUNDA QUESTAO

    def insert(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node


                #TERCEIRA QUESTAO
    def remove(self):
        if self.head:
            removed = self.head.data
            self.head = self.head.next

            if self.head is None or self.head.next is None:
                self.tail = self.head
            return removed
        else:
            return None
            
            
    def mostrar(self):
        if self.tail is not None and self.head is not None:
            print(f'O valor da cauda da fila é {self.tail.data} e o valor da cabeça é {self.head.data}')
        else:
            print("A fila esta vazia")

            
            
                  #QUARTA QUESTAO  
    def first(self):
        first_node = self.remove()
        if first_node:
            aux_queue = Queue()
            print(f"O primeiro item da Fila é {first_node}")
            aux_queue.insert(first_node)
            #while (aux = self.remove()) is not None:
            while True:
                aux = self.remove()
                if aux is not None:
                    aux_queue.insert(aux)
                else:
                    break

            while True:
                aux = aux_queue.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
        else:
            print("A fila esta vazia")



                #QUINTA QUESTAO
    def isEmpty(self):
        test_node = self.remove()
        if test_node:
            aux_queue = Queue()
            aux_queue.insert(test_node)
            #while (aux = self.remove()) is not None:
            while True:
                aux = self.remove()
                if aux is not None:
                    aux_queue.insert(aux)
                else:
                    break

            while True:
                aux = aux_queue.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
        
            return False
        else:
            return True



                    #SEXTA QUESTAO
    def len(self):
        lentgh = 0
        aux = self.remove()
        if aux is not None:
            lentgh = lentgh + 1
            aux_queue = Queue()
            aux_queue.insert(aux)
            while True:
                aux = self.remove()
                if aux is not None:
                    lentgh = lentgh + 1
                    aux_queue.insert(aux)
                else:
                    break
            while True:
                aux = aux_queue.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
        print(f"O tamanho da fila elementar é {lentgh}")
            
            
            

                            #SETIMA QUESTAO
    def last(self):
        aux = self.remove()
        if aux is not None:
            aux_queue = Queue()
            aux_queue.insert(aux)
            last = aux
            while True:
                aux = self.remove()
                if aux is not None:
                    aux_queue.insert(aux)
                    last = aux
                else:
                    break
            print(f"O ultimo elemento da fila é {last}")
            while True:
                aux = aux_queue.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
        else:
            print("A fila nao possui nenhum elemento")
            
            
                    #OITAVA QUESTAO
    def getValueByIndex(self,idx):
        aux = self.remove()
        if aux is not None:
            i = 0
            value = None
            aux_queue = Queue()
            aux_queue.insert(aux)
            while True:
                if i == idx:
                    value = aux
                aux = self.remove()
                if aux is not None:
                    aux_queue.insert(aux)
                else:
                    break
                i += 1
            while True:
                aux = aux_queue.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
            if value is not None:    
                print(f"O elemento na posição {idx} é :{value}")
            else:
                print("A pilha tao possui essa posição")
                
                
                
                #NONA QUESTAO
    def getIndexByValue(self,value):
        value = str(value)
        aux = self.remove()
        if aux is not None:
            count = 0
            index = []
            aux_queue = Queue()
            aux_queue.insert(aux)
            if aux == value:
                index.append(count)
                while True:
                    aux = self.remove()
                    if aux is not None:
                        aux_queue.insert(aux)
                    else:
                        break
            else:
                count += 1
                while True:
                    aux = self.remove()
                    if aux is not None:
                        aux_queue.insert(aux)
                        if aux == value:
                            index.append(count)  
                        count += 1      
                    else: break
            while True:
                aux = aux_queue.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
                
            print(f"O valor {value} se encontra na posição {index[0]}")
        else:
            print("O valor não se encontra na fila")
            
                        #NOVAS


                                    #TREZE
    def removeAll(self):
        aux = self.remove()
        if aux is not None:
            while aux is not None:
                aux = self.remove()
            print("A fila foi esvaziada")
        else:
            print("A fila ja estava vazia")
    
    
                                    #CATORZE
    def removeByIndex (self,idx):
        aux = self.remove()
        if aux is not None:
            count = 0
            removed = []
            aux_queue = Queue()
            if count == idx:
                removed.append(aux)
                aux = self.remove()
            aux_queue.insert(aux)
            count += 1
            while True:
                if count == idx:
                    removed.append(aux)
                    aux = self.remove()
                else:
                    aux = self.remove()
                if aux is not None:
                    aux_queue.insert(aux)
                else:
                    break
                count += 1
            while True:
                aux = aux_queue.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
            if removed is not None:
                print(f"O valor {removed[0]} que estava na posição {idx} foi removido")
            else:
                print("A fila nao possui essa posição")
                
                
                
                            #QUINZE
    def removeByValue (self,value):
        value = str(value)
        aux = self.remove()
        if aux is not None:
            removed = None
            aux_queue = Queue()
            if aux == value:
                removed = aux
                aux = self.remove()
            aux_queue.insert(aux)
            while True:
                aux = self.remove()
                if aux == value:
                    if removed is None:
                        removed = aux
                        aux = self.remove()
                if aux is not None:
                    aux_queue.insert(aux)
                else:
                    break
        
            while True:
                aux = aux_queue.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
                
            print(f"O valor {removed} foi removido")
        else:
            print("O valor não se encontra na fila")
            
            
            #QUESTAO 16
    def removeAllByValue(self,value):
        value = str(value)
        aux = self.remove()
        if aux is not None:
            removed = []
            aux_queue = Queue()
            if aux == value:
                removed.append(aux)
                aux = self.remove()
            aux_queue.insert(aux)
            while True:
                aux = self.remove()
                if aux == value:
                    removed.append(aux)
                    aux = self.remove()
                if aux is not None:
                    aux_queue.insert(aux)
                else:
                    break
        
            while True:
                aux = aux_queue.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
                
            print(f"Os valores {removed} foram removidos")
        else:
            print("O valor não se encontra na fila")
            
            
                    #QUESTAO 18
    def removeAllBySlice (self,inicio,fim):
        aux = self.remove()
        if aux is not None:
            count = 0
            test = []
            aux_queue = Queue()
            if count == inicio:
                while count != fim:
                    test.append(self.remove())
                    count += 1
                    if test is None:
                        break
                aux = self.remove()
            aux_queue.insert(aux)
            count += 1
            while True:
                aux = self.remove()
                if count == inicio:
                    while count != fim:
                        test.append(self.remove())
                        count += 1
                        if test is None:
                            break
                if aux is not None:
                    aux_queue.insert(aux)
                else:
                    break
            
            while True:
                aux = aux_queue.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
                
            print(f"Os valores entre {inicio} e {fim} removidos foram {test}")
        else:
            print("A fila ta vazia")