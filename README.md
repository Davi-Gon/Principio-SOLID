# Principio-SOLID
  SOLID são principios de programação orientada a objetos(POO) que servem para criar programas bem estruturados, robustos, flexiveis e de facil manutenção, em vista disso,
podemos dizer que SOLID é de extrema importancia para um bom desenvolvimento.
  A sigla SOLID repesenta cinco principios a serem seguidos:  
  
S - Single Responsibility Principle;  
O - Open/Closed Principle;  
L - Liskov Substitution Principle;  
I - Interface Segregation Principle;  
D- Dependency Inversion Principle.  

  Para esse trabalho foi escolhido os principios S, O, L e I para ser dissertado sobre.  
### SRP - Single Responsibility Principle(Principio de Responsabilidade Unica):  
Esse Principio dita que uma classe pode ter apenas uma responsabilidade, ou seja, executar uma unica tarefa dentro do código. É comum a existencia de GOD Class's,
Classes que fazem ou sabem demais, isso implica em um problema de manutenção e modificação, afinal é o mesmo que mexer em um emaranhado de fios, é confuso e as chances de  
dar errado é altissima, é ai que surje a SRP. A SRP impede a falta de coesão, o alto acoplamentro (muitas dependências), e a dificuldade que reaproveitar o código pois  
todos estão separados e exucutando a sua (única)função, melhorando até mesmo a legibilidade do código.

Código de soma normal.


### OCP - Open/Closed Principle(Principio Aberto/Fechado):  
O principio OCP diz que "Obejetos ou entidades devem estar abertas para extensão, mas fechadas para modificação", digamos que você precise criar uma nova ligação de energia,  
concordamos que é extremamente mais fácil fazer uma ligação/puxar de um ponto ja existente doque desmontar o quadro de energia inteiro para adicionala, afinal, quem garante  
que sera a ultima ligação a ser criada ? O principio OCP nos diz "exatamente" isso. 

Atendimento de PET Shop.
