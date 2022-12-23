def palindromos(cadena):
    try:
        if len(cadena) == 0:
            raise ValueError('No se puede ingresar una cadena vacía.')
        else:
            palindromo = cadena == cadena[::-1]
            print(palindromo)
    except ValueError as ve:
        print(ve)
        return False
    else:
        print('El programa se ejecutó sin errores')
    finally:
        print('Gracias por usar palindromos.py')
    
try:
    print(palindromos('lool'))
except TypeError:
    print('Sólo se pueden ingresar strings.')