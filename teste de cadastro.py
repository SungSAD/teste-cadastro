print ('Olá, irei ajudar com seu cadastro')
nome = (input('Digite seu nome:' ))
print ('certo, agora preciso saber sua idade')
idade = int(input ('digite sua idade:' ))
print ('muito bem!, confira os dados para mim por favor:')
print ('nome:', (nome))
print ('idade:', (idade))
(input ('Caso esteja correto, digite ok:'))
if idade > 18:
    print ('Já estamos na metade do caminho, então prosseguirei com o cadastro de endereço')
else:
    print ('sinto muito, mas não poderei prosseguir com seu cadastro por ser menor de idade')