import numpy as np #numpy é um lib que tem recursos matemáticos

gamma = 0.75 #Penalidade
alpha = 0.9

location_to_state = {'A':0,
                     'B':1,
                     'C':2,
                     'D':3,
                     'E':4,
                     'F':5,
                     'G':6,
                     'H':7,
                     'I':8,
                     'J':9,
                     'K':10,
                     'L':11}
  
action = [0,1,2,3,4,5,6,7,8,9,10,11]

R = np.array([[0,1,0,0,0,0,0,0,0,0,0,0],#Matrix
              [1,0,1,0,0,1,0,0,0,0,0,0],
              [0,1,0,0,0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0,0],
              [0,0,0,0,0,0,0,0,1,0,0,0],
              [0,1,0,0,0,0,0,0,0,1,0,0],
              [0,0,1,0,0,0,1,1,0,0,0,0],
              [0,0,0,1,0,0,1,0,0,0,0,1],
              [0,0,0,0,1,0,0,0,0,1,0,0],
              [0,0,0,0,0,1,0,0,1,0,0,0],
              [0,0,0,0,0,0,0,0,0,1,0,1],
              [0,0,0,0,0,0,0,1,0,0,1,0]])

    
# PARTE 3 - Resultados (Entrando em Produção)
state_to_location = {state: location for location, state in location_to_state.items()} 
    # aqui converteremos as posições em letras
    
def route(starting_location, ending_location):
    R_new = np.copy(R) # solução da tarefa
    ending_state = location_to_state[ending_location]
    R_new[ending_state, ending_state] = 1000
    
    # PARTE 2 CONSTRUÇÃO DA SOLUÇÃO DE IA COM Q-LEARNING
    Q = np.array(np.zeros([12,12]))# Zerando os valores das colunas e linhas

    for i in range(1000):
        current_state = np.random.randint(0,12) # Numeros aleátoris entre 1 e 11
        playable_actions = [] #Ações possiveis
        for j in range(12):#vai ser percorrida linha por linha do array que é 12 linhas e 12 colunas
            if R[current_state, j] > 0: #Recompensa que são  maiores que zero
                playable_actions.append(j) #Ações posiveis
        
        next_state = np.random.choice(playable_actions)#Dentre as opções selecionadas o programa vai escolher sozinho qual vai seguir
        
        #Com base no estado atual, a I.A vai decidir pra qual estado ela vai fazer.
        #TD diferença temporal
        
        TD = R[current_state, next_state] + gamma * Q[next_state, np.argmax(Q[next_state,])] - Q[current_state, next_state]
        Q[current_state, next_state] = Q[current_state, next_state] + alpha * TD #Atualização
    
        #Entenda o Q como o conciente da máqui, onde vai ficar o que ela aprendeu.
        
    route = [starting_location]
    next_location = starting_location
    
    while(next_location != ending_location): #Só usamos o While quando NÃO SABEMOS O NUMERO DE VEZES VAMOS PRECISAR PRA USAR O LOOP
        
        starting_state = location_to_state[starting_location]
        next_state = np.argmax(Q[starting_state])
        next_location = state_to_location[next_state]
        route.append(next_location)
        starting_location = next_location
        
    return route

print('Route:')

print(route('K', 'G'))


#TAREFA 
# Adicione um recurso que nos dê a opção de ir para o local intermediário antes de ir para o local
# de prioridade máxima. Como em nossa classisificação de locais prioritários, o segundo
# local de prioridade máxima é o local K e, para otimizar ainda mais os fluxos de armazém, o robô
# autonomo deve passar pelo local K para coletar os produtos até o local de prioridade
#máxima G. Uma maneira de fazer isso é ter a opção de ir por qualquer localização intermediária
# qualquer localização intermediária no processo de nosso função route()

def best_route(starting_location, intermediary_location, ending_location):
    return route(starting_location, intermediary_location) + route(intermediary_location, ending_location)[1:]
best_route('E', 'K', 'G')

