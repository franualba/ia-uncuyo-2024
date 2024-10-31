## A. Preprocesamiento de Datos

### 1. Limpieza Inicial
- Se eliminaron comillas dobles de todos los campos
- Se factorizaron variables categóricas:
  - 'altura' con niveles: "Bajo (2 - 4 mts)", "Medio (4 - 8 mts)", "Alto (> 8 mts)"
  - 'diametro_tronco' con niveles: "Chico", "Mediano", "Grande"
- Se convirtió la clase 'inclinacion_peligrosa' a tipo lógico
### 2. Feature Engineering

#### 2.1 Nuevas Variables Creadas
- **Características de ubicación**:
  - 'dist_centro_seccion': Distancia al centro de la sección calculada usando coordenadas long/lat
  - 'densidad_arboles': Número de árboles por área de sección
  - 'ratio_arboles_peligrosos': Proporción de árboles peligrosos por sección
#### 2.2 Transformaciones
- **One-Hot Encoding**:
  - Se aplicó a la variable 'especie'
  - Se manejaron especies no vistas en entrenamiento asignándolas a categoría "OTHER"
#### 2.3 Normalización
Se normalizaron las siguientes variables numéricas usando estandarización (media 0, desviación estándar 1):
- long (longitud)
- lat (latitud)
- area_seccion
- dist_centro_seccion
- densidad_arboles
- ratio_arboles_peligrosos
### 3. Preparación Final
- Se separaron las características (X) de la variable objetivo (Y)
- Se convirtieron todas las variables lógicas a numéricas
- Se crearon matrices para el entrenamiento del modelo

## B. Resultado obtenido sobre el conjunto de validación

El resultado de la métrica AUC-ROC sobre el conjunto de validación fue de 0.739

## C. Resultado obtenido en Kaggle

El resultado de la métrica AUC-ROC indicado por Kaggle fue de 0.69445

## D. Funcionamiento del Algoritmo

### 1. Arquitectura del Modelo
- Se implementó un modelo LightGBM (Light Gradient Boosting Machine)
- Se utilizó una arquitectura de stacking para mejorar el rendimiento
### 2. Proceso de Entrenamiento
1. **Validación Cruzada**:
   - Se utilizó una validación cruzada de 5 folds
   - Se implementó una búsqueda de hiperparámetros sobre:
     - número mínimo de observaciones por nodo (min_n)
     - profundidad del árbol (tree_depth)
     - tasa de aprendizaje (learn_rate)

2. **Hiperparámetros Base**:
   - Número de árboles: 100
   - Otros parámetros se optimizaron mediante grid search

3. **Stacking**:
   - Se combinaron múltiples modelos LightGBM con diferentes configuraciones
   - Se utilizó blending para las predicciones finales
### 3. Optimización del Modelo
- Se implementó optimización de umbral usando el estadístico J de Youden
- Se balanceó la sensibilidad y especificidad para encontrar el punto óptimo de clasificación
- Se generaron dos tipos de predicciones:
  - Probabilidades continuas
  - Clasificaciones binarias basadas en el umbral optimizado
### 4. Evaluación
- Métrica principal: AUC-ROC
- Métricas adicionales:
  - Matriz de confusión
  - Sensibilidad
  - Especificidad
  - Distribución de predicciones
### 5. Particularidades del Proceso
- Manejo robusto de valores faltantes
- Tratamiento especial para especies no vistas en entrenamiento
- Escalado de características basado en parámetros del conjunto de entrenamiento
