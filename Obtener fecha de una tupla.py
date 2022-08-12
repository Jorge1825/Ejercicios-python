 # Ejercicio 9: Mostrar la fecha de un evento almacenada en une tupla.
fecha_evento = (2823, 9, 14)


print('El evento programado será para la fecha:', fecha_evento)
print('El evento programado será para la fecha: %i/%i/%i' % fecha_evento)
agnio, mes, dia = fecha_evento
print('El evento programado será para la fecha: {}/{}/{}'.format(agnio, mes, dia))