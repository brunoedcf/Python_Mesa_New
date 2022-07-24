# Python Mesa Multi-Agent Simulation

Esse modelo de simulação feito no framework Mesa da linguagem Python propõe um experimento para observar a mudança da coloração de cada agente com base nas interações que fazem entre si. 
O modelo possui uma variável independente que descreve a chance de um agente influenciar o outro a mudar para a sua própria cor. Essa variável é manipulável na interface que permite modificar o seu valor, podendo variar de 0 a 100. 

Quanto maior o valor da variável independente, maior será a chance de, depois de uma quantidade de steps significativa, uma só cor ter prevalecido sobre todas as outras.
A hipótese a ser observada é que, com a valor da variável independente não ultrapassando o valor de 95, as cores que estão em menor quantidade não serão completamente sobrepostas pelas outras e a proporção da diversidade dos agentes sempre se manterá saudável.

No código utilizei um grid para posicionar os agentes, cada um com uma cor aleatória dentre as 5 possíveis dentro da simulação. Para cada step do modelo, um agente se move para uma célula no seu arredor e, de acordo com o valor da variável independente, interage com outro agente. Ao interagir com o outro agente ele o influencia a mudar para sua cor. Caso a interação não ocorra, o outro agente escolhe por si só uma cor aleatória dentre as disponíveis.

A interface possui dois gráficos principais, um que mostra a variação da quantidade presente de cada cor em específico ao longo do tempo e outro que mostra a proporção de cada cor em relação ao total de agentes.

Para executar a simulação é preciso instalar o framework MESA:

pip install mesa

Depois execute o arquivo main.py com o comando:

python main.py

