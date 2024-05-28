# Introducción al aprendizaje por refuerzo
El aprendizaje por refuerzo, RL, se considera uno de los paradigmas básicos del aprendizaje automático, junto al aprendizaje supervisado y el aprendizaje no supervisado. RL se trata de decisiones: tomar las decisiones correctas o al menos aprender de ellas.

Imagine que tiene un entorno simulado como el mercado de valores. ¿Qué pasa si impones una determinada regulación? ¿Tiene un efecto positivo o negativo? Si sucede algo negativo, es necesario aprovechar este refuerzo negativo , aprender de ello y cambiar de rumbo. Si se trata de un resultado positivo, es necesario aprovechar ese refuerzo positivo .

![alt text](image.png)

> ¡Peter y sus amigos necesitan escapar del lobo hambriento! Imagen de Jen Looper

Tema regional: Pedro y el lobo (Rusia)
[Pedro y el lobo](https://en.wikipedia.org/wiki/Peter_and_the_Wolf) es un cuento de hadas musical escrito por el compositor ruso [Sergei Prokofiev](https://en.wikipedia.org/wiki/Sergei_Prokofiev). Es una historia sobre el joven pionero Peter, quien valientemente sale de su casa al claro del bosque para perseguir al lobo. En esta sección, entrenaremos algoritmos de aprendizaje automático que ayudarán a Peter a:

* Explore los alrededores y cree un mapa de navegación óptimo
* Aprende a usar una patineta y a mantener el equilibrio sobre ella para moverte más rápido.

[![Peter and the Wolf](https://img.youtube.com/vi/Fmi5zHg4QSM/0.jpg)](https://www.youtube.com/watch?v=Fmi5zHg4QSM)

> 🎥 Haz clic en la imagen de arriba para escuchar Peter and the Wolf de Prokofiev

## Aprendizaje reforzado
En secciones anteriores, ha visto dos ejemplos de problemas de aprendizaje automático:

* **Supervisado** , donde tenemos conjuntos de datos que sugieren soluciones de muestra al problema que queremos resolver. La clasificación y la regresión son tareas de aprendizaje supervisadas.
* **No supervisado** , en el que no tenemos datos de entrenamiento etiquetados. El principal ejemplo de aprendizaje no supervisado es el Clustering.

En esta sección, le presentaremos un nuevo tipo de problema de aprendizaje que no requiere datos de entrenamiento etiquetados. Hay varios tipos de tales problemas:

* **Aprendizaje semisupervisado** , donde tenemos una gran cantidad de datos sin etiquetar que se pueden usar para entrenar previamente el modelo.
* **Aprendizaje por refuerzo** , en el que un agente aprende a comportarse realizando experimentos en algún entorno simulado.

### Ejemplo: juego de computadora
Supongamos que desea enseñarle a una computadora a jugar un juego, como ajedrez o Super Mario . Para que la computadora pueda jugar, necesitamos que prediga qué movimiento realizar en cada uno de los estados del juego. Si bien esto puede parecer un problema de clasificación, no lo es, porque no tenemos un conjunto de datos con estados y acciones correspondientes. Si bien es posible que tengamos algunos datos, como partidas de ajedrez existentes o registros de jugadores que juegan Super Mario, es probable que esos datos no cubran suficientemente una cantidad suficiente de estados posibles.

En lugar de buscar datos existentes del juego, el aprendizaje por refuerzo (RL) se basa en la idea de hacer que el ordenador juegue muchas veces y observar el resultado. Así, para aplicar el Aprendizaje por Refuerzo, necesitamos dos cosas:

Un entorno y un simulador que nos permiten jugar muchas veces. Este simulador definiría todas las reglas del juego así como posibles estados y acciones.

Una función de recompensa , que nos diría qué tan bien lo hicimos durante cada jugada o partida.

La principal diferencia entre otros tipos de aprendizaje automático y RL es que en RL normalmente no sabemos si ganamos o perdemos hasta que terminamos el juego. Por lo tanto, no podemos decir si un determinado movimiento por sí solo es bueno o no: solo recibimos una recompensa al final del juego. Y nuestro objetivo es diseñar algoritmos que nos permitan entrenar un modelo en condiciones inciertas. Aprenderemos sobre un algoritmo RL llamado Q-learning .

### Desarrollo de las lecciones
1. [Introducción al aprendizaje por refuerzo y Q-Learning](./1-QLearning/)
2. [Usando un entorno de simulación de gimnasio](./2-Gym/)

### Créditos
"Introducción al aprendizaje por refuerzo" fue escrita con ♥️ por Dmitri Sóshnikov