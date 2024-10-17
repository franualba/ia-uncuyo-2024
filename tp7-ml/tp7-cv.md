```
create_folds <- function(df, num_folds) {
  # Obtener el número total de filas en el dataframe
  n <- nrow(df)
  
  # Crear un vector de índices aleatorios
  indices <- sample(1:n)
  
  # Calcular el tamaño aproximado de cada fold
  fold_size <- ceiling(n / num_folds)
  
  # Crear la lista de folds
  folds <- list()
  for (i in 1:num_folds) {
    start_index <- (i - 1) * fold_size + 1
    end_index <- min(i * fold_size, n)
    folds[[paste0("Fold", i)]] <- indices[start_index:end_index]
  }
  
  return(folds)
}
```

```
library(rpart)
library(caret)

cross_validation <- function(df, num_folds) {
  folds <- create_folds(df, num_folds)
  
  metrics <- data.frame(Accuracy=numeric(num_folds),
                        Precision=numeric(num_folds),
                        Sensitivity=numeric(num_folds),
                        Specificity=numeric(num_folds))
  
  for (i in 1:num_folds) {
    # Separar datos de entrenamiento y prueba
    test_indices <- folds[[i]]
    train_indices <- unlist(folds[-i])
    
    train_data <- df[train_indices, ]
    test_data <- df[test_indices, ]
    
    # Entrenar el modelo
    model <- rpart(inclinacion_peligrosa ~ diametro_tronco + altura, data=train_data, method="class")
    
    # Hacer predicciones
    predictions <- predict(model, test_data, type="class")
    
    # Calcular matriz de confusión
    conf_matrix <- table(test_data$inclinacion_peligrosa, predictions)
    
    # Calcular métricas
    metrics$Accuracy[i] <- calculate_accuracy(conf_matrix)
    metrics$Precision[i] <- calculate_precision(conf_matrix)
    metrics$Sensitivity[i] <- calculate_sensitivity(conf_matrix)
    metrics$Specificity[i] <- calculate_specificity(conf_matrix)
  }
  
  # Calcular media y desviación estándar
  results <- data.frame(
    Metric = c("Accuracy", "Precision", "Sensitivity", "Specificity"),
    Mean = colMeans(metrics),
    SD = apply(metrics, 2, sd)
  )
  
  return(results)
}
```

![[tabla_cv.png]]
