# Estudia los solucionadores

## Instrucciones

En esta lección aprendiste acerca de diferentes solucionadores que emparejan algoritmos con un proceso de aprendizaje automático para crear un modelo preciso. Revisa los solucionadores listados en la lección y elige dos. En tus propias palabras, compara y contrasta estos dos solucionadores. ¿Qué clase de problema abordan? ¿Cómo funcionan con varias estructuras de datos? ¿Porqué elegirías uno por encima de otro?

### Solucionadores Scikit-Learn
Scikit-learn es una biblioteca de aprendizaje automático en Python que proporciona una variedad de algoritmos para abordar diferentes problemas. Vamos a comparar dos solucionadores específicos de scikit-learn: **SGDClassifier** y **LogisticRegression**.

**SGDClassifier:**
1. Clase de Problemas:
    * Problemas de Clasificación Binaria y Multiclase: SGDClassifier es un clasificador lineal que puede manejar tanto problemas de clasificación binaria como multiclase.

2. Funcionamiento con Estructuras de Datos:
    * Eficiencia con Grandes Conjuntos de Datos: SGDClassifier es especialmente útil para conjuntos de datos grandes debido a su capacidad para realizar la optimización mediante descenso de gradiente estocástico. Puede manejar datos sparse (dispersos) y es eficiente en términos de memoria.

3. Elección del Algoritmo:
    * Optimización Estocástica: SGDClassifier utiliza el descenso de gradiente estocástico para optimizar la función de pérdida, lo que lo hace adecuado para conjuntos de datos grandes y problemas donde la eficiencia computacional es crucial.

**LogisticRegression:**
1. Clase de Problemas:
    * Problemas de Clasificación Binaria y Multiclase: LogisticRegression es otro clasificador lineal que puede manejar tanto problemas de clasificación binaria como multiclase.

2. Funcionamiento con Estructuras de Datos:
    * Adecuado para Conjuntos de Datos Moderados: LogisticRegression es eficiente para conjuntos de datos de tamaño moderado. Se beneficia de tener datos bien condicionados y es más adecuado para conjuntos de datos que caben en la memoria.

3. Elección del Algoritmo:
    * Regularización: LogisticRegression permite la regularización, lo que puede ser útil para controlar el sobreajuste en problemas con una gran cantidad de características. Puedes elegir entre regularización L1 y L2 según las características de tus datos.

**Elección entre SGDClassifier y LogisticRegression:**
* Tamaño del Conjunto de Datos:
    * Si trabajas con un conjunto de datos grande y quieres eficiencia computacional, considera SGDClassifier.
    * Para conjuntos de datos moderados, LogisticRegression puede ser más apropiado.
* Eficiencia con Datos Sparse:
    * Si tus datos son dispersos (sparse), SGDClassifier es más eficiente en términos de memoria.
* Regularización:
    * Si la regularización es importante para controlar el sobreajuste, LogisticRegression ofrece opciones de regularización que puedes ajustar.
* Interpretación del Modelo:
    * LogisticRegression proporciona coeficientes directamente relacionados con las probabilidades, lo que facilita la interpretación.

En resumen, la elección entre SGDClassifier y LogisticRegression depende de factores como el tamaño del conjunto de datos, la eficiencia computacional, la necesidad de regularización y la interpretabilidad del modelo. Ambos son útiles en diferentes situaciones, y la elección debería basarse en las características específicas del problema y de los datos.
## Rúbrica

| Criterio | Ejemplar                                                                                      | Adecuado                                         | Necesita mejorar            |
| -------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------- |
|          | Se presentó un archivo .doc con dos párrafos, uno de cada solucionador, comparándolos seriamente. | Se presentó un archivo .doc con sólo un párrafo | La asignación está incompleta |

#### Esta es la evidencia que corresponde a la <a href="https://github.com/microsoft/ML-For-Beginners/blob/main/4-Classification/2-Classifiers-1/translations/assignment.es.md">tarea</a> de la lección <a href="https://github.com/microsoft/ML-For-Beginners/blob/main/4-Classification/2-Classifiers-1/translations/README.es.md">Clasificadores de cocina 1</a> del curso <a href="https://github.com/microsoft/ML-For-Beginners/tree/main"> MACHINE LEARNING FOR BEGINNERS</a> de Microsoft.