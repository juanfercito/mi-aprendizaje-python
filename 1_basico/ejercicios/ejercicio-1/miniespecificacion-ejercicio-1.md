Este ejercicio se corresponde con las sesiones de **tutoría** correspondientes a los temas tratados en las primeras semanas, sobre los ***datos primitivos***, ***operadores*** y e***structuras de control***

``` markdown
inicio

// Arranca el programa
ESCRIBIR "Bienvenido a nuestro Club"
(decide, x(3)[a-z],[BS]) <-- ESCRIBIR "¿desea ingresar?"
LEER decide

// Verificar si la condicion se cumple
SI decide == "si" O decide == "yes" ENTONCES

    // inicia el ciclo While
    MIENTRAS True
        // ingresan los datos
        (nombre, x(20)[a-z],[A;E;I;O;U],[BS]) <-- ESCRIBIR "¿cual es su nombre?"
        LEER nombre
        (edad, i[1-n]) <-- ESCRIBIR "¿cual es su edad?"
        LEER edad

        // comienzan las validaciones
        SI edad < 18 ENTONCES
            (pase, d[0-n]) <-- edad *2 / 100
            ESCRIBIR "lo sentimos " +nombre+ "no puede pasar, pero le daremos $ " +pase+ "para el bus"

        DE LO CONTRARIO
            SI edad >= 18 Y edad <= 59 ENTONCES
                (pase, d[0-n]) <-- edad * 2 / 10 * 15 / 100
                ESCRIBIR "felicidades " +nombre+ ", puede pasar, son $ " +pase+

            DE LO CONTRARIO
                SI edad > 59 ENTONCES
                    (pase, d[0-n]) <-- edad * 2 / 100
                    ESCRIBIR "Ok " +nombre+ ", puede pasar pero debe pagar $ " +pase+

                FIN SI
            FIN SI
        FIN SI

        //validar si el ciclo del programa se sigue repitiendo
        (repetir, x(3)[a-z],[BS]) <-- ESCRIBIR "¿desea ingresar otra vez?"
        LEER repetir

        SI repetir == "si" O repetir == "yes" ENTONCES
            CONTINUAR
        DE LO CONTRARIO
            INTERRUMPIR 
        
        FIN SI
    FIN MIENTRAS

FIN SI

// mensaje de término del programa
ESCRIBIR "Gracias por su visita"

Fin del programa

```
---

> **IMPORTANTE**
> - Revisar el archivo **algoritmo-ejercicio-1.svg** para comprender el flujo del programa y entender gráficamente esta miniespecificación.
> - Puedes hacer pruebas y modificaciones en el flujo de esta miniespecificación y compararlo con el código del archivo **codigo-ejercicio-1.py** para visualizar su funcionamiento y adquirir una comprensión más profunda de los temas implicados.

---