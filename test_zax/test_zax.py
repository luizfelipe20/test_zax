class Motoboy:
    def __init__(self, name, valor_fixo):
        self.name = name
        self.valor_fixo = valor_fixo


class Pedido:
    def __init__(self, valor):
        self.valor = valor
        
        
class Loja:
    def __init__(self, name, comissao):
        self.name = name
        self.comissao = comissao
        self.motoboys = []
        self.pedidos = []
    
    def adicionar_motoboy(self, motoboy):
        self.motoboys.append(motoboy)
        
    def adicionar_pedidos(self, *pedidos):
        [self.pedidos.append(pedido) for pedido in pedidos]
    
    def calcular_comissao(self, motoboy):
        total_pedidos = sum(pedido.valor for pedido in self.pedidos)         
        return ((total_pedidos / 100) * self.comissao) + (len(self.pedidos) * motoboy.valor_fixo)

    def __repr__(self):
        return self.name          
        

class Zax:
    def __init__(self):
        self.lojas = []
        
    def adicionar_lojas(self, *lojas):
        [self.lojas.append(loja) for loja in lojas]
        
    def calcula_frete(self, motoboy):
        lojas = self.lojas_que_atende(motoboy)
        pedidos = self.qtd_pedidos(lojas, motoboy)
        valor_frete = self.valor_frete(lojas, motoboy)
        
        return "lojas: {} => pedidos: {} => frete: {}".format(lojas, pedidos, valor_frete)
                
    def lojas_que_atende(self, motoboy):
        lojas = []
        for loja in self.lojas:
            if motoboy in loja.motoboys:
                lojas.append(loja)
        if lojas:
            return lojas
        else:
            return self.lojas

    def qtd_pedidos(self, lojas, motoboy):
        qtd_pedidos = 0

        for loja in lojas:
            qtd_pedidos = qtd_pedidos + len(loja.pedidos)

        return qtd_pedidos
        
    def valor_frete(self, lojas, motoboy):
        valor = 0
        for loja in lojas:
            valor = valor + loja.calcular_comissao(motoboy)
        return valor


motoboy_1 = Motoboy(name="motoboy 1", valor_fixo=2.00)
motoboy_2 = Motoboy(name="motoboy 2", valor_fixo=2.00)
motoboy_3 = Motoboy(name="motoboy 3", valor_fixo=2.00)
motoboy_4 = Motoboy(name="motoboy 4", valor_fixo=2.00)
motoboy_5 = Motoboy(name="motoboy 5", valor_fixo=3.00)

pedido_1 = Pedido(50.00)
pedido_2 = Pedido(50.00)
pedido_3 = Pedido(50.00)
pedido_4 = Pedido(50.00)    
pedido_5 = Pedido(50.00)
pedido_6 = Pedido(50.00)
pedido_7 = Pedido(50.00)
pedido_8 = Pedido(50.00)
pedido_9 = Pedido(50.00)
pedido_10 = Pedido(100.00)
    
    
loja_1 = Loja(name="loja 1", comissao=5.00)
loja_1.adicionar_motoboy(motoboy_4)
loja_1.adicionar_pedidos(pedido_1, pedido_2, pedido_3)

loja_2 = Loja(name="loja 2", comissao=5.00)
loja_2.adicionar_pedidos(pedido_4, pedido_5, pedido_6, pedido_7)

loja_3 = Loja(name="loja 3", comissao=15.00)
loja_3.adicionar_pedidos(pedido_8, pedido_9, pedido_10)

zax = Zax()
zax.adicionar_lojas(loja_1, loja_2, loja_3)

print(zax.calcula_frete(motoboy_1))
print(zax.calcula_frete(motoboy_2))
print(zax.calcula_frete(motoboy_3))
print(zax.calcula_frete(motoboy_4))
print(zax.calcula_frete(motoboy_5))