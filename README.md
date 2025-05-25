# Principio-SOLID
  SOLID são principios de programação orientada a objetos(POO) que servem para criar programas bem estruturados, robustos, flexiveis e de facil manutenção, em vista disso, podemos dizer que SOLID é de extrema importancia para um bom desenvolvimento.
  A sigla SOLID repesenta cinco principios a serem seguidos:  
  
S - Single Responsibility Principle;  
O - Open/Closed Principle;  
L - Liskov Substitution Principle;  
I - Interface Segregation Principle;  
D- Dependency Inversion Principle.  

  Para esse trabalho foi escolhido os principios S, O, L e I para ser dissertado sobre.  
### SRP - Single Responsibility Principle(Principio de Responsabilidade Unica):  
Esse Principio dita que uma classe pode ter apenas uma responsabilidade, ou seja, executar uma unica tarefa dentro do código. É comum a existencia de GOD Class's, Classes que fazem ou sabem demais, isso implica em um problema de manutenção e modificação, afinal é o mesmo que mexer em um emaranhado de fios, é confuso e as chances de dar errado é altissima, é ai que surje a SRP. A SRP impede a falta de coesão, o alto acoplamentro (muitas dependências), e a dificuldade que reaproveitar o código pois todos estão separados e exucutando a sua (única)função, melhorando até mesmo a legibilidade do código.

Código de soma normal.




### OCP - Open/Closed Principle(Principio Aberto/Fechado):  
O principio OCP diz que "Obejetos ou entidades devem estar abertas para extensão, mas fechadas para modificação", digamos que você precise criar uma nova ligação de energia,  concordamos que é extremamente mais fácil fazer uma ligação/puxar de um ponto ja existente doque desmontar o quadro de energia inteiro para adicionala, afinal, quem garante que sera a ultima ligação a ser criada ? O principio OCP nos diz "exatamente" isso. 

Atendimento de PET Shop.

### LSP - Liskov Substitution Principle(Principio da Substituição de Liskov):  
"Uma classe derivada deve ser substituivel por sua classe base" em um breve resumo, caso eu precise usar um componente que tem sua origem de outro componente, a maquina deve funcionar da mesma forma, sem precisar fazer modificações, afinal, um componente veio de outro. Esse principio para ser sequido de forma correta é precisso de outros principios de SOLID como o OCP.  

Não sei ainda.  

### ISP - Interface Segregation Principle(Principio da Segregação da Interface):  
Esse principio visa a não inutilidade "Uma classe não deve ser forçada a implementar interfaces e métodos que não irão utilizar", as interfaces devem ser especificas ao invés de genéricas. Quando criamos uma interface de comportamento por exemplo, podemos abstrair de forma que "todos os seres teram os mesmo comportamentos", porém é nitido que a classe pessoa não vai ter o mesmo comportamento que a classe cachorro, porém pode haver semelhanças, logo, alguns comportamentos não seram utilizados em uma classe, assim sendo -> inutil.  
