#o número primo é aquele que só é divisível por ele mesmo e por 1. ou seja, ele só pode ser dividido por dois números. em outras palavras, ele só tem dois múltiplos. os números não primos são divisíveis por mais de dois números (por exemplo, 4 é divisível por 4, por 2 e por 1, ou seja, não é primo)
#resumo do código: vamos pegar todos os números de 1 a 500 e dividir, um por um, por todos os números de 1 a 500. nós só vamos acionar o contador quando um número for divisível pelo outro. se não for, ignora. pra cada número que eu testei, quero saber só daqueles que são divisíveis por 2 números, ele mesmo e 1.
n=500 #esse é o número máximo do intervalo

for A in range(1,n): #pegue todos os números de 1 a 500, daí coloca 1 por vez na caixinha A.
  contador = 0 #zera o contador.
  for B in range(1,n): #agora pega um outro número de 1 a 500, um por vez também, põe na caixinha B. como esse laço tá dentro do anterior, ele vai testar 500 opções de B para cada A
    resto = A % B #divide o número que tá na caixa A pelo que tá na caixa B, me fala o resto da divisão. 
    if (resto == 0): #se for zero, o A é divisível pelo B, e portanto o B é múltiplo de A
      contador = contador + 1 #a cada vez que isso acontecer, tu adiciona um número nesse contador, assim ele vai indicar quantos múltiplos o A tem. quando vc terminar de testar todos os números em B, zera o contador e vamos botar o próximo número do intervalo na caixa A, e dividir ele por todos os número possíveis em B, e contar quantas vezes essa divisão tem resto zero
  if (contador == 2): #o número primo só tem dois múltiplos: ele mesmo e 1. descarta todos os números em A que têm mais de dois múltiplos, ou seja, que o contador somou mais de 2, eles não são primos. pega só os que têm dois múltiplos
    print(A, 'é primo') #imprime quais são esses números
