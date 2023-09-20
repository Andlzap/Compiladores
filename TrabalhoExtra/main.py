import regrasProducao
import pilha
import numpy as np

regrasP = regrasProducao.RegrasProduct()

regrasP.criarRegra()

entrada = "( id + id * id ) $"

palavras = entrada.split()

st = pilha.Stack()
st.push("$")
st.push("E")
print(f'Stack: {st.show()}')

while palavras[0] != "$" or st.top() != "$":
    
    teste = st.pop()

    if teste == "E" or teste=="T":
        for i in range (len(regrasP.regras[teste])-1, -1, -1):
            st.push(regrasP.regras[teste][i])

    else:
        for i in range (len(regrasP.regras[teste][0])-1, -1, -1):
         st.push(regrasP.regras[teste][0][i])

    if(palavras[0] == "$"): 
        while st.top() != "$":
            st.pop()

    if st.top() == "id" or st.top() == "*" or st.top() == "+" or st.top() == "(" or st.top() == ")":
       st.pop()
       if palavras[0] == "id" or palavras[0] == "*" or palavras[0] == "+" or palavras[0] == "(" or palavras[0] == ")":
          palavras.pop(0)
          
    print(f'Entrada: {palavras}')    
    print(f'Stack: {st.show()}')
    