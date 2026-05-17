# Classe do nó
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


# Classe da Árvore Binária de Busca (BST)
class BST:
    def __init__(self):
        self.raiz = None

    # INSERÇÃO
    def inserir(self, raiz, valor):
        if raiz is None:
            return No(valor)

        if valor < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = self.inserir(raiz.direita, valor)

        return raiz

    # BUSCA
    def buscar(self, raiz, valor):
        if raiz is None:
            return False

        if raiz.valor == valor:
            return True

        if valor < raiz.valor:
            return self.buscar(raiz.esquerda, valor)
        else:
            return self.buscar(raiz.direita, valor)

    # MENOR VALOR DA SUBÁRVORE (auxiliar para remoção)
    def menor_valor(self, raiz):
        atual = raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    # REMOÇÃO
    def remover(self, raiz, valor):
        if raiz is None:
            return raiz

        if valor < raiz.valor:
            raiz.esquerda = self.remover(raiz.esquerda, valor)

        elif valor > raiz.valor:
            raiz.direita = self.remover(raiz.direita, valor)

        else:
            # Caso 1: sem filho à esquerda
            if raiz.esquerda is None:
                return raiz.direita

            # Caso 2: sem filho à direita
            elif raiz.direita is None:
                return raiz.esquerda

            # Caso 3: dois filhos
            sucessor = self.menor_valor(raiz.direita)
            raiz.valor = sucessor.valor
            raiz.direita = self.remover(raiz.direita, sucessor.valor)

        return raiz

    # PERCURSO IN-ORDER
    def in_order(self, raiz):
        if raiz:
            self.in_order(raiz.esquerda)
            print(raiz.valor, end=" ")
            self.in_order(raiz.direita)


# TESTANDO O EXERCÍCIO

arvore = BST()

# Inserir na ordem: 50, 30, 70, 20, 40, 60, 80
valores = [50, 30, 70, 20, 40, 60, 80]

for valor in valores:
    arvore.raiz = arvore.inserir(arvore.raiz, valor)

# Buscar 60
if arvore.buscar(arvore.raiz, 60):
    print("Valor 60 encontrado.")
else:
    print("Valor 60 não encontrado.")

# Remover 30
arvore.raiz = arvore.remover(arvore.raiz, 30)

# In-order final
print("In-order final:")
arvore.in_order(arvore.raiz)
