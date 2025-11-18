Este ejercicio se corresponde con las sesiones de **tutoría** correspondientes a los temas tratados en las primeras semanas, sobre los ***datos primitivos***, ***operadores*** y e***structuras de control***

``` markdown
1.  inicio
2. 
3.  // Arranca el programa
4.  //ESCRIBIR "Bienvenido a nuestro Club"
5.  (decide, x(3)[a-z],[BS])
6.  ESCRIBIR "¿desea ingresar?"
7.  LEER decide
8. 
9.  // Verificar si la condicion se cumple
10. SI decide == "si" O decide == "yes" ENTONCES
11. 
12.      // inicia el ciclo While
13.      MIENTRAS True
14.         // ingresan los datos
15.         (nombre, x(20)[a-z],[A;E;I;O;U],[BS])
16.         ESCRIBIR "¿cual es su nombre?"
17.         LEER nombre
18.         (edad, i[1-n])
19.         ESCRIBIR "¿cual es su edad?"
20.         LEER edad
21.         
22.         // comienzan las validaciones
23.         SI edad < 18 ENTONCES
24.             (pase, d[0-n]) <-- edad *2 / 100
25.             ESCRIBIR "lo sentimos " +nombre+ "no puede pasar, pero le daremos $ " +pase+ "para el bus"
26. 
27.         DE LO CONTRARIO
28.             SI edad >= 18 Y edad <= 59 ENTONCES
29.                 (pase, d[0-n]) <-- edad * 2 / 10 * 15 / 100
30.                 ESCRIBIR "felicidades " +nombre+ ", puede pasar, son $ " +pase+
31.             
32.            DE LO CONTRARIO
33.                 SI edad > 59 ENTONCES
34.                     (pase, d[0-n]) <-- edad * 2 / 100
35.                     ESCRIBIR "Ok " +nombre+ ", puede pasar pero debe pagar $ " +pase+
36. 
37.                 FIN SI
38.             FIN SI
39.         
40.         FIN SI
41. 
42.         
43.                 //validar si el ciclo del programa se sigue repitiendo
44.         (repetir, x(3)[a-z],[BS]) <-- ESCRIBIR "¿desea ingresar otra vez?"
45.         LEER repetir
46. 
47.         SI repetir == "si" O repetir == "yes" ENTONCES
48.             CONTINUAR
49. 
50. 
51.         DE LO CONTRARIO
52.             INTERRUMPIR 
53.        
54.         FIN SI
55.     FIN MIENTRAS
56. 
57. FIN SI
58. 
59. 
60. // mensaje de término del programa
61. ESCRIBIR "Gracias por su visita"
62. 
63. Fin del programa

```
---

> **IMPORTANTE**
> - Revisar el archivo **algoritmo-ejercicio-1.svg** para comprender el flujo del programa y entender gráficamente esta miniespecificación.
> - Puedes hacer pruebas y modificaciones en el flujo de esta miniespecificación y compararlo con el código del archivo **codigo-ejercicio-1.py** para visualizar su funcionamiento y adquirir una comprensión más profunda de los temas implicados.

---