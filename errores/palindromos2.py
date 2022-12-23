def palindromos(cadena):
    assert len(cadena) > 1, 'No se puede ingresar una cadena vacía.'
    return cadena == cadena[::-1]

print(palindromos('non')) # -> True
print(palindromos(''))    # -> AssertionError: No se puede ingresar una cadena vacía.