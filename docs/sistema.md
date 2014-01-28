SISTEMA COMPLETO
=================

Input 	-> Base de Datos

Output 	-> Location de los tweets relacionados a un evento

* Paso 1 : Obtener info de un evento

Input: 	(Evento, Keywords, Datetime)
Output: ([{Tweets con coordenadas -> Location from DSTK}, {Tweets sin coordenadas -> User ID}])
Doist:
	[X] Obtener los IDs de los eventos del día
		db-interactions::getLastEventDateTime
		db-interactions::getEventsBetweenTwoDateTimes
		db-interactions::getTweetsIDByEvent
	[ ] IDs eventos del día 		-> IDs Usuarios que twitearon
	[ ] IDs eventos del día 		-> Lista de tweets con coordinates
	[ ] IDs Usuarios que twitearon 	-> Location field de esos usuarios

* Paso 2.1 : 

* Paso 2 : Procesar los Location
	[ ] Eliminar los que no me sirven (only-symbols)
	[ ] 