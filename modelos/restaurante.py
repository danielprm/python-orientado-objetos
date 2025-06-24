class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'praca'
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurante()

Restaurantes = [restaurante_praca,
restaurante_pizza]

print(Restaurantes)
