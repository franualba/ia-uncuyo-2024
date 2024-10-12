#### 1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a fexible statistical learning method to be better or worse than an infexible method. Justify your answer.

Flexible methods are most valuable when there's a clear signal (like non-linear relationships) and enough data to reliably estimate complex patterns. They tend to perform worse when dealing with limited data, too many predictors, or high noise, as these conditions make overfitting more likely.

a) When n is extremely large and p is small: WORSE. 
	A flexible method would generally perform worse here. With a large sample size and few predictors, we have a very stable learning environment where we can reliably estimate relationships. An inflexible method would be less likely to overfit and would capitalize on the abundant data to estimate a simpler model with high precision. The high n provides enough data to get accurate estimates of even simple relationships.

b) When p is extremely large and n is small: WORSE. 
	A flexible method would perform worse in this case. With many predictors and few observations, we're at high risk of overfitting. A flexible method would try to capture complex patterns in what is likely mostly noise, given the limited data. An inflexible method with strong regularization would help prevent overfitting in this "large p, small n" scenario.

c) When the relationship is highly non-linear: BETTER.
	A flexible method would perform better here. Inflexible methods (like linear regression) would fail to capture the true non-linear relationships in the data. Flexible methods can adapt to and model complex non-linear patterns. This is exactly the type of scenario where we want the additional flexibility to model curved relationships.

d) When error variance is extremely high: WORSE.
	A flexible method would perform worse with high error variance. When there's a lot of noise in the data, flexible methods tend to overfit by trying to model the noise rather than the true underlying relationship. An inflexible method would be more resistant to fitting to noise and would focus on capturing the main trends in the data.

#### 2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

(a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors afect CEO salary. 

> This is a regression problem, and we're more interested in inference.

(b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables. 

> This is a classification problem, and we're more interested in prediction.

(c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.

> This is a regression problem, and we're more interested in prediction.

#### 3. We now revisit the bias-variance decomposition. 

Regarding the bias-variance decomposition:

(a) Provide a sketch of typical (squared) bias, variance, training error, test error, and Bayes (or irreducible) error curves, on a single plot, as we go from less fexible statistical learning methods towards more fexible approaches. The x-axis should represent the amount of fexibility in the method, and the y-axis should represent the values for each curve. There should be five curves. Make sure to label each one. 

![[sketch.png]]

(b) Explain why each of the five curves has the shape displayed in part (a)

- Bias (squared) - Blue curve, decreasing: As model flexibility increases, bias decreases. Less flexible models make stronger assumptions about the underlying structure of the data, which can lead to higher bias if these assumptions are incorrect. More flexible models can adapt better to the true underlying relationship, reducing bias.
- Variance - Red curve, increasing: Variance increases with model flexibility. More flexible models are more sensitive to the specific data points in the training set, leading to higher variance. They can change dramatically with small changes in the training data.
- Training Error - Green curve, monotonically decreasing: As model flexibility increases, training error consistently decreases. More flexible models can adapt more closely to the training data, potentially even fitting noise, which results in lower training error.
- Test Error - Purple curve, U-shaped: Test error is the sum of bias, variance, and irreducible error. It typically follows a U-shape. Initially, as flexibility increases, bias decreases rapidly while variance increases slowly, causing test error to decrease. At some point, the increase in variance outpaces the decrease in bias, causing test error to rise again for very flexible models.
- Bayes (Irreducible) Error - Black horizontal line: This represents the lowest possible error rate for any model due to inherent noise in the problem. It's constant regardless of model flexibility because it's a property of the data, not the model.

#### 5.  What are the advantages and disadvantages of a very fexible (versus a less fexible) approach for regression or classifcation? Under what circumstances might a more fexible approach be preferred to a less fexible approach? When might a less fexible approach be preferred?

**Advantages** of a very flexible approach:

1. Can capture complex, non-linear relationships in the data
2. Potentially lower bias, especially when the true underlying relationship is complex
3. Can adapt to a wide variety of data patterns
4. Often performs well when there's a large amount of training data

**Disadvantages** of a very flexible approach:

1. Higher risk of overfitting, especially with limited data
2. Increased variance - more sensitive to the specific training data used
3. Less interpretable - often act as "black boxes"
4. May require more computational resources
5. Can perform poorly on new, unseen data if overfitted

**Advantages** of a less flexible approach:

1. More interpretable - easier to understand and explain the model's decisions
2. Lower variance - more stable predictions across different training sets
3. Less prone to overfitting, especially with limited data
4. Often computationally simpler and faster
5. Can perform well when the true relationship is relatively simple

**Disadvantages** of a less flexible approach:

1. Higher bias, especially when the true relationship is complex
2. May underfit if the model is too simplistic for the data
3. Limited ability to capture non-linear relationships

When a **more flexible** approach might be **preferred**:

1. Large dataset: With more data, flexible models can better learn complex patterns without overfitting.
2. Complex relationships: When the underlying relationship between features and the target is known or suspected to be highly non-linear or complex.
3. Prediction is more important than interpretation: When the primary goal is predictive accuracy rather than understanding the model's decision-making process.
4. Sufficient computational resources: When you have the computing power to handle more complex models.
5. In domains where capturing subtle patterns can be crucial, like image recognition or natural language processing.

When a **less flexible** approach might be **preferred**:

1. Small dataset: With limited data, simpler models are less likely to overfit.
2. Need for interpretability: In fields like healthcare or finance where understanding the model's decision process is crucial.
3. Simple underlying relationship: When the relationship between features and the target is known or suspected to be relatively straightforward.
4. Limited computational resources: When simpler, faster models are necessary due to constraints.
5. High-stakes decisions: In situations where model reliability and consistency are paramount, and where complex models might introduce unpredictable behavior.
6. Regulatory requirements: Some industries have regulations that favor simpler, more interpretable models.
7. When the signal-to-noise ratio in the data is low: Simpler models can be more robust to noise.

#### 6. Describe the diferences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classifcation (as opposed to a non-parametric approach)? What are its disadvantages?

**PARAMETRIC APPROACH:**

- Assumes a specific functional form for the relationship between predictors and the response.
- Involves estimating a fixed number of parameters, regardless of the amount of training data.
- Examples include linear regression, logistic regression, and linear discriminant analysis.

**NON-PARAMETRIC APPROACH:**

- Does not assume a specific functional form for the relationship.
- The number of parameters can grow with the amount of training data.
- Examples include k-nearest neighbors, decision trees, and kernel methods.

**Advantages** of a Parametric Approach:

1. **Simplicity and Interpretability**: Parametric models often have a clear, interpretable structure. For instance, in linear regression, coefficients directly represent the effect of each predictor.
2. **Efficiency with Limited Data**: With fewer parameters to estimate, parametric models can perform well even with smaller datasets.
3. **Lower Risk of Overfitting**: The fixed structure of parametric models inherently limits their complexity, reducing the risk of overfitting.
4. **Computational Efficiency**: Generally faster to train and make predictions, especially with large datasets.
5. **Ease of Inference**: Statistical inference (e.g., hypothesis testing, confidence intervals) is often more straightforward with parametric models.
6. **Extrapolation**: Parametric models can more confidently make predictions outside the range of observed data.
7. They provide a simple summary of the relationship between predictors and response.

**Disadvantages** of a Parametric Approach:

1. **Potential for High Bias**: If the assumed functional form is incorrect, the model may systematically misrepresent the true relationship, leading to high bias.
2. **Limited Flexibility**: Parametric models may struggle to capture complex, non-linear relationships in the data.
3. **Model Misspecification**: Incorrect assumptions about the underlying data distribution can lead to poor performance.
4. **Difficulty with High-Dimensional Data**: Many parametric models struggle when the number of predictors is large relative to the number of observations.
5. **Assumption Violations**: Parametric models often rely on specific assumptions (e.g., normality, variance homogeneity) that may not hold in real-world data.
6. **Risk of Underfitting**: If the model is too simple for the underlying relationship, it may underfit the data, missing important patterns.

In practice, the choice between parametric and non-parametric approaches boils down to factors like:

- **Data size**: Parametric models may be preferred for smaller datasets.
- **Domain knowledge**: If there's strong prior knowledge about the relationship's form, a parametric model might be more appropriate.
- **Interpretability requirements**: If understanding the model's decision-making process is crucial, parametric models often have an advantage.
- **Complexity of the underlying relationship**: For highly complex, unknown relationships, non-parametric models might be more suitable.
- **Computational resources**: Parametric models are often computationally more efficient.

#### 7.  
![[7_sentences.png]]

(a) To compute the Euclidean distance between each observation and the test point (0,0,0), we use the formula: d = sqrt((X1-0)^2 + (X2-0)^2 + (X3-0)^2)

Obs. 1: sqrt(0^2 + 3^2 + 0^2) = 3 
Obs. 2: sqrt(2^2 + 0^2 + 0^2) = 2 
Obs. 3: sqrt(0^2 + 1^2 + 3^2) = sqrt(10) ≈ 3.16 
Obs. 4: sqrt(0^2 + 1^2 + 2^2) = sqrt(5) ≈ 2.24 
Obs. 5: sqrt((-1)^2 + 0^2 + 1^2) = sqrt(2) ≈ 1.41 
Obs. 6: sqrt(1^2 + 1^2 + 1^2) = sqrt(3) ≈ 1.73

(b) With K = 1, we look at the single nearest neighbor. The smallest distance is 1.41 (Obs. 5), which corresponds to Y = Green. 
Prediction: Green 
Why? Because the closest point to our test point is green.

(c) With K = 3, we look at the three nearest neighbors. The three smallest distances are: 1.41 (Obs. 5, Green), 1.73 (Obs. 6, Red), 2 (Obs. 2, Red) 
Prediction: Red 
Why? Because among the 3 nearest neighbors, we have 2 Red and 1 Green, and the majority wins.

(d) If the Bayes decision boundary is highly non-linear, we would expect the **best value** for K to be **small**.

Why? A smaller K allows the model to capture more complex, non-linear decision boundaries. With a small K, the model can adapt to local patterns in the data, which is necessary for capturing a highly non-linear boundary.

As K increases, the decision boundary becomes smoother and less complex. With a large K, the model averages over more data points, which tends to smooth out the decision boundary, making it less capable of capturing highly non-linear patterns.

Therefore, to capture a highly non-linear Bayes decision boundary, a smaller K would be preferred as it allows for more flexibility in the decision boundary shape.