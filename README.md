# Confiabilidad-Métricas
Una de las características de calidad de software es la Confiabilidad: es cual es la "capacidad del software de mantener su nivel de ejecución bajo condiciones normales en un periodo de tiempo establecido"

En este ejercicio simularemos un servidor el cual nos devolverá un booleano que representa si el servidor responde o no.

Imaginaremos que existe un minuto de diferencia entre cada llamada que realicemos al servidor.

Utiliza la funcion "serverMock", el cual recibe opcionalmente como parámetro el numero de veces máximo que nos permitirá mandarlo a llamar. En nuestro caso sera de 90 (equivalente a 1:30hr)

## Objetivos
Modifica la funcion main para obtener las siguientes métricas de confiabilidad:
1. Nivel de madurez: Tiempo medio entre fallas
2. Capacidad de recuperación: Tiempo medio desde que se presenta una falla hasta restablecerle.
3. Disponibilidad: Cantidad / porcentaje de tiempo fuera de servicio

## Resultados
Crea un archivo "SOLUTIONS.md" el cual deberá incluir:
- Resultados obtenidos
- Análisis
- Métricas de confiabilidad (Madurez, recuperación, disponibilidad)
- Conclusiones

Ademas, contesta las siguientes preguntas:
- ¿Falta alguna característica de confiabilidad? En caso de que si, mencionala y analiza si es que podemos obtenerla.
- ¿Hay algún error/bug en el servidor de prueba? Si es asi, ¿cual es, y como lo corregirías?