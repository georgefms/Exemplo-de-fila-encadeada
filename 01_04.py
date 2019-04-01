#filas encadeadas
class Node():
    def __init__(self, i):
        self.info = i
        self.prox = None

class filaencad():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def inserir(self, node):
        if not self.primeiro:
            self.primeiro = node
            self.ultimo = node
            return

        self.ultimo.prox = node
        self.ultimo = node
        return

    def varrer(self):
        node = self.primeiro
        while node:
            print(node.info,end=" ")
            node = node.prox
        print()

    def acessar(self):
        if self.primeiro:
            return self.primeiro.info

    def excluir(self):
        if not self.primeiro:
                return
        j =  self.primeiro.prox
        self.primeiro.prox = None
        self.primeiro = j
        return






tst1 = Node(3)
tst2 = Node(7)
tst3 = Node(5)

fila = filaencad()

fila.inserir(tst1)
fila.inserir(tst2)
fila.inserir(tst3)

fila.varrer()
print(fila.acessar())
fila.excluir()
fila.varrer()