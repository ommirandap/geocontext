Journal
=======

### Week 1
	- Objetivos principales
		- Familiarización con los datos y su formato
		- Seleccionar que técnica aplicar 

### Day 1 - Lunes 6 Enero 2014

- Exploración de datos
	- Script para analizar el JSON entregado
		- [X] Pasar los datos a un archivo con 1 linea - 1 tweet
		- [X] Listar los keywords de cada archivo bajo un directorio
		- [ ] Hacer un script completo que pase los datos a 1 linea - 1 tweet, para todos los archivos bajo un directorio
			- `Importante` Acotación de Vanessa: Mantener el formato JSON

### Day 2 - Martes 7 Enero 2014

- Daily Meeting
	* Muestra del trabajo del día anterior
	* Feedback con respecto a mantener las cosas en formato JSON **válido** o texto
- Reunion (Profe)
	- Esta semana de exploración
	- Hablar con Jheser y Eduardo sobre lo que hacen ellos
	- [ ] Revisar Google Analizar
	- [ ] BigQuery las posibilidades y hacer un plan para las semanas sgtes
	- [ ] Sacar estadísticas (usuarios/lugares que se repiten)
	- [ ] Buscar BD grandes con ubicaciones (*DSTK, Geonames, etc*)
	- `Idea de la profe:` Hacer matching y el resto clasificación

- Exploración de datos
	- Analizar los JSON y sacar *solamente* las cosas importantes de cada tweet


### Day 3 - Miércoles 8 Enero 2014

- Daily Meeting
	* Notamos que tal vez haya un error en la recolección ya que a priori hay tweets que se repiten
	* Seguir con el trabajo de exploración para corroborar si es un error de recolección o error mío
	* [ ] Esperar alguna info sobre la recolección en cuboid

- Daily Work
	* Analizar el código que procesa y extrae los campos importantes (**Posible error de programación o de datos**)
	* Correr el código anterior sobre todos los datos (*Generar una carpeta aparte con JSON que contengan sólo los datos importantes*)
	* Obtener estadísticas de los datos procesados
	- **Trabajar con 1 objeto JSON por línea por mientras. Es mas sencillo hacer sort | uniq y otras cosas**

### Day 15 - Lunes 20 Enero 2014

- Daily Meeting
	* Se analizó lo que se tenía hasta el momento, para comenzar a armar el sistema completo
	* Se está bajando e instalando la maquina virtual de DSTK

- Daily Work
	* El archivo db-interactions.py incluye retrieval desde la DB para obtener los eventos del día y sus tweets asociados


### Day 20 - Lunes 27 Enero 2014

- Daily Meeting	
	* Se pensaron maneras de armar la BD de lugares considerando las distintas jerarquías de cada país

- Daily Work
	* Se trabaja en una BD de los dumps de GeoNames, que consta de 3 tablas (Pais, Jerarquía 2, Jerarquía 3)
	* Se subió el trabajo a [GitHub](http://www.github.com/ommirandap/geocontext)

### Day 21 - Martes 28 Enero 2014
- Reunión Diaria
	* Se tomó el consenso de sólo tener una tabla que asocie el TweetID con la Locacion

- Daily Work

