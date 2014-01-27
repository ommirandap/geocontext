USEFULS QUERIES
===============

mysql -u omiranda -D breakingnews -p -e $QUERY > output_file.out

SELECT COUNT(Conteo.Suma) AS 'Numero de usuarios', Conteo.Suma AS 'Cantidad de Tweets' 
FROM (
		SELECT COUNT(user_id_id) AS Suma, user_id_id AS UserID 
 		FROM tweet 
 		GROUP BY UserID 
 		ORDER BY COUNT(UserID) DESC
 		) AS Conteo 
GROUP BY Conteo.Suma 
ORDER BY Conteo.Suma DESC

