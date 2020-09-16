#-- Método que não recebe parâmetros e não possui retorno --#
def imprimirPi():
    print( "Valor do Pi:" )
    print( 3.14 )


# Executando o método
imprimirPi()

#-------------------------------------------------------#

#-- Método que não recebe parâmetros e possui retorno --#
def getSalario():
    return 1045.0

print( getSalario() )

#----------------------------------------------------#

#-- Método que recebe parâmetros e não possui retorno
def calcular_imprimir_area(largura, comprimento):
    area = float(largura) * float(comprimento)
    print( area )

calcular_imprimir_area( 2 , 3 )

# ------------------------------------------------------#

# -- Métodos que recebem parâmetros e possuem retorno --#
def calcular_area( largura, comprimento ):
    area = float(largura) * float(comprimento)
    return area

altura = 5
volume = altura * calcular_area( 4 , 6 )
print( volume )



def calcular_volume( largura, comprimento, altura ):
    volume = float(largura) * float(comprimento) * float( altura )
    return volume

def calcular_volume2( largura, comprimento, altura ):
    volume = calcular_area( largura, comprimento ) * float( altura )
    return volume

def calcular_volume3( altura, area ):
    volume = altura * area
    return volume

print( calcular_volume3( 5 , calcular_area( 2 , 4 ) ) ) 

def calcular_volume4(altura):
    volume = altura * calcular_area(4,6)
    return volume


# ----------------------------------------------------#

# -- Trabalhando com Array ---------------------------#

carros = [ "Doblo" , "Novo Uno" , " Sandero" ]
print( carros )

print( carros[1] )



# ----------------------------------------------------#

# -- Método recursivo --------------------------------#    

def abrirPortas( portas ):
    if portas > 0:
        print( portas )
        portas = portas - 1
        abrirPortas( portas )

abrirPortas( 3 )