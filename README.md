Conforme Marques & Arenales 2002, cortar objetos grandes (por exemplo, bobinas, placas, paralelepípedos) para a produção de itens menores em quantidades bem definidos, ou empacotar itens pequenos dentro de espaços bem definidos são problemas idênticos, considerando que um item cortado de uma certa posição pode ser visto como ocupando aquela posição (daí a referência na literatura a Problemas de Corte e Empacotamento). O número de combinações possíveis dos itens dentro de um objeto (cada combinação possível é chamada padrão de corte) é, em geral, muito grande e, a tentativa de enumerá-las completamente é inviável do ponto de vista prático. Uma função objetivo pode ser definida medindo, por exemplo, perdas no caso do problema de corte, ou vazios no caso de empacotamento, ou custos, ou número de objetos usados, etc. Um problema de corte e empacotamento consiste em determinar um padrão de corte que minimize a função objetivo.



Dentro desta categoria de problemas estão vários clássicos da ciência da computação, tais como os problemas da mochila, dentre outros, os quais são, em geral, NP-completo. Várias técnicas de resolução têm sido desenvolvidas, em geral especializando procedimentos consagrados da Pesquisa Operacional. Há, na literatura, um grande número de problemas de corte e empacotamento e podemos classificá-los conforme algumas características. Em particular, uma primeira característica consiste nas dimensões relevantes do processo de corte. Assim, podemos ter os problemas de corte unidimensionais, com apenas uma dimensão relevante para o processo de corte, como por exemplo, o corte de bobinas (de papel, aço, tecidos, plásticos, etc) e barras. O clássico problema da mochila pode ser visto como um problema de corte unidimensional. Outros problemas bidimensionais, onde duas dimensões são relevantes, têm aplicações diversas, como por exemplo, o corte de placas de madeira, chapas de aço, placas de vidro, tecido, etc.

Este trabalho será em um outro domínio que não o de corte.  Assim, você deve recuperar o código visto na Aula 3 para desenvolver um aplicativo que gerencia a logística de dockagem diária de navios em um grande terminal portuário. 

Cada navio a dockar tem um comprimento ln e transporta m containers. Supondo que o comprimento total do cais  seja L >> ln, o app deve fornecer em uma lista de N navios que aguardam para dockarem, quais serão escolhidos de forma a maximizar o número diário de transbordo de containers.

Assim, desenvolva o código para este aplicativo partindo dos seguintes parâmetros:

- numero de navios, N,  aguardando dockagem no dia;

- comprimento  ln e número de container m de cada navio (gerar aleatóriamente isso); e

- comprimento máximo do cais, L

A saída deve ser quais navios estarão atracando no dia.

O código base DEVE ser o código da mochila apresentado. 



Encaminhe um pdf com Relatório Técnico que descreva: 1.Introducao do problema, 2. Método adotado, 3. Testes e Validação (modifique os parâmetros e analise os resultados), 4. Considerações Finais, 5. Material Consultado, 6. Código comentado, 7. Link para vídeo onde será gravada tela e audio, explicando cada trecho de código e mostrando resultados do código rodando, a exemplo da aulas gravadas.
