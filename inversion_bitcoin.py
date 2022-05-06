## en este fichero, crearemos una funición capaz de avisarnos cuando
# el valor de los bitcoin caiga por debajo de 30.000€


#función que te convierte tus bitcoins a euros
def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    #bitcoin_amount cantidad de bitcoins que se posee
    #bitcoin_value_euros la conversión de bitcoin a euros

    euros_value=bitcoin_amount*bitcoin_value_euros

    return euros_value

