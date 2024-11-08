class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)

    def _agregar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._agregar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._agregar_recursivo(nodo.derecha, valor)

    def calcular_nivel(self, nodo, valor, nivel=0):
        if nodo is None:
            return -1
        if nodo.valor == valor:
            return nivel
        nivel_izq = self.calcular_nivel(nodo.izquierda, valor, nivel + 1)
        if nivel_izq != -1:
            return nivel_izq
        return self.calcular_nivel(nodo.derecha, valor, nivel + 1)

    def calcular_altura(self, nodo):
        if nodo is None:
            return -1
        altura_izq = self.calcular_altura(nodo.izquierda)
        altura_der = self.calcular_altura(nodo.derecha)
        return max(altura_izq, altura_der) + 1

    def calcular_peso(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.calcular_peso(nodo.izquierda) + self.calcular_peso(nodo.derecha)

# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolBinario()
    valores = [10, 5, 15, 3, 7, 12, 18]
    for valor in valores:
        arbol.agregar(valor)

    valor_a_buscar = 18
    nivel = arbol.calcular_nivel(arbol.raiz, valor_a_buscar)
    altura = arbol.calcular_altura(arbol.raiz)
    peso = arbol.calcular_peso(arbol.raiz)

    print(f"Nivel del nodo {valor_a_buscar}: {nivel}")
    print(f"Altura del árbol: {altura}")
    print(f"Peso del árbol: {peso}")