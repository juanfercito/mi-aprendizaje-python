Este ejercicio se corresponde con las sesiones de **tutoría** correspondientes a los temas tratados en las primeras semanas, sobre los ***datos primitivos***, ***operadores*** y e***structuras de control***

``` markdown
1.  inicio

2.  // Arranca el programa
3.  //ESCRIBIR "Bienvenido a nuestro Club"
4.  (decide, x(3)[a-z],[BS]) <-- ESCRIBIR "¿desea ingresar?"
5.  LEER decide

6.  // Verificar si la condicion se cumple
7.  SI decide == "si" O decide == "yes" ENTONCES

8.      // inicia el ciclo While
9.      MIENTRAS True
10.         // ingresan los datos
11.         (nombre, x(20)[a-z],[A;E;I;O;U],[BS]) <-- ESCRIBIR "¿cual es su nombre?"
12.         LEER nombre
13.         (edad, i[1-n]) <-- ESCRIBIR "¿cual es su edad?"
14.         LEER edad
15.         
16.         // comienzan las validaciones
17.         SI edad < 18 ENTONCES
18.             (pase, d[0-n]) <-- edad *2 / 100
19.             ESCRIBIR "lo sentimos " +nombre+ "no puede pasar, pero le daremos $ " +pase+ "para el bus"
20. 
21.         DE LO CONTRARIO
22.             SI edad >= 18 Y edad <= 59 ENTONCES
23.                 (pase, d[0-n]) <-- edad * 2 / 10 * 15 / 100
24.                 ESCRIBIR "felicidades " +nombre+ ", puede pasar, son $ " +pase+
25.             
26.            DE LO CONTRARIO
27.                 SI edad > 59 ENTONCES
28.                     (pase, d[0-n]) <-- edad * 2 / 100
29.                     ESCRIBIR "Ok " +nombre+ ", puede pasar pero debe pagar $ " +pase+
30. 
31.                 FIN SI
32.             FIN SI
33.         
34.         FIN SI
35. 
36.         
37.                 //validar si el ciclo del programa se sigue repitiendo
38.         (repetir, x(3)[a-z],[BS]) <-- ESCRIBIR "¿desea ingresar otra vez?"
39.         LEER repetir
40. 
41.         SI repetir == "si" O repetir == "yes" ENTONCES
42.             CONTINUAR
43. 
44. 
45.         DE LO CONTRARIO
46.             INTERRUMPIR 
47.        
48.         FIN SI
49.     FIN MIENTRAS
50. 
51. FIN SI

52. 
53. // mensaje de término del programa
54. ESCRIBIR "Gracias por su visita"
55. 
56. Fin del programa

```
---

> **IMPORTANTE**
> - Revisar el archivo **algoritmo-ejercicio-1.svg** para comprender el flujo del programa y entender gráficamente esta miniespecificación.
> - Puedes hacer pruebas y modificaciones en el flujo de esta miniespecificación y compararlo con el código del archivo **codigo-ejercicio-1.py** para visualizar su funcionamiento y adquirir una comprensión más profunda de los temas implicados.

---