"""
Problema
Existem 5 motoboys, cada motoboy ganha uma comissão diferente por pedido coletado, e alguns motoboys possuem exclusividade com algumas lojas na qual fazem coletas.

Os motoboys não podem reclamar que ficaram sem pedidos.

Os motoboys que possuem exclusividade com as lojas, possuem prioridade.

Os motoboys podem ter exclusividade com as lojas, mas as lojas não possuem exclusividade com os motoboys.

Hoje existem 10 pedidos para serem retirados em 3 lojas.

Quando eu executar o script passando apenas o motoboy ou não passando nenhum motoboy, preciso ver:
Quem é o motoboy e quantos pedidos terá?
De qual loja é?
Quanto vai ganhar?

Dados do teste

Motoboys
Moto 1 - cobra R$2 reais por entrega e atende todas as lojas
Moto 2 - cobra R$2 reais por entrega e atende todas as lojas
Moto 3 - cobra R$2 reais por entrega e atende todas as lojas
Moto 4 - cobra R$2 reais por entrega e atende apenas a loja 1
Moto 5 - cobra R$3 reais por entrega e atende todas as lojas

Lojas
Loja 1 - 3 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$50) e paga 5% do valor pedido por entrega fora o valor fixo. 
Loja 2 - 4 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$50, PEDIDO 4 R$50) e paga 5% do valor pedido por entrega fora o valor fixo.
Loja 3 - 3 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$100) e paga 15% do valor pedido por entrega fora o valor fixo.

O Moto 1 atende todas as lojas
O Moto 2 atende todas as lojas
O Moto 3 atende todas as lojas
O Moto 4 atende apenas a loja 1
O Moto 5 atende todas as lojas

"""


class Pedido:
    def __init__(self, valor, loja):
        self.valor = valor
        self.loja = loja


class Motoboy:
    def __init__(self, name, valor_fixo):
        self.name = name
        self.valor_fixo = valor_fixo
        self.pedidos = []
        self.lojas = []
    
    def adicionar_loja(self, loja):
        self.lojas.append(loja)


    def pedidos_atendidos(self, *pedidos):
        
        if self.lojas:
            for pedido in pedidos:
                if pedido.loja in self.lojas:
                    self.pedidos.append(pedido)
        else:        
            for pedido in pedidos:
                self.pedidos.append(pedido) 
    
    def __repr__(self):
        return self.name  
        
class Loja:
    def __init__(self, name, comissao):
        self.name = name
        self.comissao = comissao
    
    def calcular_valor_comissao(self, valor):
        return (valor / 100) * self.comissao

    def __repr__(self):
        return self.name          
        

class Zax:
    def __init__(self):
        self.lojas = []
        
    def adicionar_lojas(self, *lojas):
        [self.lojas.append(loja) for loja in lojas]
        
    def pedidos_motoboy(self, motoboy=None):
        if motoboy:
            lojas = self.lojas_que_atendeu(motoboy)
            pedidos = self.qtd_pedidos(motoboy)
            valor_entrega = self.valor_entrega(motoboy)
            return "motoboy: {} => lojas: {} => pedidos: {} => frete: {}".format(motoboy, lojas, pedidos, valor_entrega)
        return "lojas: 0 => pedidos: 0 => frete: 0"
    
    def lojas_que_atendeu(self, motoboy):
        lojas = []
        for item in motoboy.pedidos:
            lojas.append(item.loja)
        
        return list(set(lojas))

    def qtd_pedidos(self, motoboy):
        return len(motoboy.pedidos)
        
    def valor_entrega(self, motoboy):
        valor = 0
        for pedido in motoboy.pedidos:
            valor = valor + pedido.loja.calcular_valor_comissao(pedido.valor) + motoboy.valor_fixo
        return valor

loja_1 = Loja(name="loja 1", comissao=5.00)
loja_2 = Loja(name="loja 2", comissao=5.00)
loja_3 = Loja(name="loja 3", comissao=15.00)

pedido_1 = Pedido(50.00, loja_1)
pedido_2 = Pedido(50.00, loja_1)
pedido_3 = Pedido(50.00, loja_1)
pedido_4 = Pedido(50.00, loja_2)    
pedido_5 = Pedido(50.00, loja_2)
pedido_6 = Pedido(50.00, loja_2)
pedido_7 = Pedido(50.00, loja_2)
pedido_8 = Pedido(50.00, loja_3)
pedido_9 = Pedido(50.00, loja_3)
pedido_10 = Pedido(100.00, loja_3)


motoboy_1 = Motoboy(name="motoboy 1", valor_fixo=2.00)
motoboy_1.pedidos_atendidos(pedido_1, pedido_2)

motoboy_2 = Motoboy(name="motoboy 2", valor_fixo=2.00)
motoboy_2.pedidos_atendidos(pedido_3, pedido_4)

motoboy_3 = Motoboy(name="motoboy 3", valor_fixo=2.00)
motoboy_3.pedidos_atendidos(pedido_5, pedido_6)

motoboy_4 = Motoboy(name="motoboy 4", valor_fixo=2.00)
motoboy_4.adicionar_loja(loja_1)
motoboy_4.pedidos_atendidos(pedido_7, pedido_8)


motoboy_5 = Motoboy(name="motoboy 5", valor_fixo=3.00)
motoboy_5.pedidos_atendidos(pedido_9, pedido_10)
    

zax = Zax()
zax.adicionar_lojas(loja_1, loja_2, loja_3)


print(zax.pedidos_motoboy(motoboy_1))
print(zax.pedidos_motoboy(motoboy_2))
print(zax.pedidos_motoboy(motoboy_3))
print(zax.pedidos_motoboy(motoboy_4))
print(zax.pedidos_motoboy(motoboy_5))