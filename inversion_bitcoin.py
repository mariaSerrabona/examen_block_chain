## en este fichero, crearemos una funición capaz de avisarnos cuando
# el valor de los bitcoin caiga por debajo de 30.000€


#función que te convierte tus bitcoins a euros
def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    #bitcoin_amount cantidad de bitcoins que se posee
    #bitcoin_value_euros la conversión de bitcoin a euros

    euros_value=bitcoin_amount*bitcoin_value_euros

    return ('Tienes un total de: '+euros_value+' tras haber hecho el cambio de Bitcoin')


#en esta fucnión se quiere que se avise a partir de un límite
def UnderLimit(limit, bitcoin_value_euros):

    if(bitcoin_value_euros<limit):
        return('En este momento, Bitcoin ha bajado y tiene un valor de: '+limit)


    else:
        pass


#creamos un main que nos ejecute el fichero
if __name__ == "__main__":

