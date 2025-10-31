# ======================================================================
# DEMONSTRAÇÃO VISUAL DA DIFERENÇA ENTRE ESCOPO DE VARIÁVEL
# Variáveis Global vs. Local em Python
# ======================================================================

# ----------------------------------------------------------------------
# 1. Variável Global
# Uma variável definida fora de qualquer função. Acessível em qualquer lugar.
# ----------------------------------------------------------------------
VAR_GLOBAL = "Eu sou GLOBAL (Escopo Principal)"
print(f"1. FORA DA FUNÇÃO (GLOBAL): {VAR_GLOBAL}")

# ----------------------------------------------------------------------
# 2. Função para Variável Local e Acesso Global
# ----------------------------------------------------------------------
def demonstrar_escopo_local():
    # Variável Local:
    # 'VAR_LOCAL' só existe DENTRO desta função.
    VAR_LOCAL = "Eu sou LOCAL (Dentro da função)"
    
    print("\n2. DENTRO DA FUNÇÃO (Escopo Local):")
    
    # Acessando a variável LOCAL (sucesso)
    print(f"   Acessando VAR_LOCAL: {VAR_LOCAL}")
    
    # Acessando a variável GLOBAL (sucesso - leitura permitida)
    print(f"   Acessando VAR_GLOBAL: {VAR_GLOBAL}")
    
    # ATENÇÃO: Esta linha cria uma nova variável LOCAL chamada VAR_GLOBAL 
    # que 'mascara' a global, mas não a modifica.
    VAR_GLOBAL = "AGORA sou LOCAL (Criei uma nova variável só aqui dentro)"
    print(f"   Nova VAR_GLOBAL (Local) ATRIBUÍDA: {VAR_GLOBAL}")

# Chamando a função
demonstrar_escopo_local()

# ----------------------------------------------------------------------
# 3. Tentativa de Acesso Local (Falha)
# A variável VAR_LOCAL não pode ser acessada aqui fora.
# ----------------------------------------------------------------------
print("\n3. FORA DA FUNÇÃO (Tentativa de acesso à Local):")
try:
    # Este comando falhará, pois VAR_LOCAL foi destruída ao sair da função
    print(f"   Tentando acessar VAR_LOCAL: {VAR_LOCAL}")
except NameError as e:
    print(f"   ERRO CAPTURADO: {e}")
    print("   Isso ocorre porque VAR_LOCAL só existe DENTRO da função onde foi definida.")

# ----------------------------------------------------------------------
# 4. Impacto da Modificação (Visualizando a Global original)
# A atribuição dentro da função (ponto 2) não alterou a VAR_GLOBAL original.
# ----------------------------------------------------------------------
print("\n4. FORA DA FUNÇÃO (Visualizando a Global novamente):")
print(f"   O valor de VAR_GLOBAL continua sendo: {VAR_GLOBAL}")
print("   *Isso prova que a atribuição no Ponto 2 criou uma variável LOCAL separada com o mesmo nome, e não alterou a GLOBAL original.")

# ----------------------------------------------------------------------
# 5. Modificando a Global (O jeito certo)
# Usando a palavra-chave 'global'
# ----------------------------------------------------------------------
def modificar_global_corretamente():
    # Declaramos que queremos usar a VAR_GLOBAL que existe no escopo exterior
    global VAR_GLOBAL
    VAR_GLOBAL = "Eu fui MODIFICADA de dentro da função (usando 'global')"
    print(f"\n5. DENTRO DA FUNÇÃO (Modificando a Global CORRETAMENTE):")
    print(f"   VAR_GLOBAL modificada para: {VAR_GLOBAL}")

modificar_global_corretamente()

print("\n6. FORA DA FUNÇÃO (Após modificação correta):")
print(f"   O novo valor de VAR_GLOBAL é: {VAR_GLOBAL}")