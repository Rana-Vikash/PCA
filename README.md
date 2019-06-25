# PCA

OUTPUT :- 

Line 13 :
Index(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], dtype='object')

Line 18 :
Open         float64
High         float64
Low          float64
Close        float64
Adj Close    float64
Volume       float64
dtype: object

Line 21 : 
Open         0
High         0
Low          0
Close        0
Adj Close    0
Volume       0
dtype: int64

Line 44 : 
array([8.83367459e-01, 1.16134354e-01, 2.84419537e-04, 1.71619035e-04, 4.21479554e-05])

Principal component analysis, or PCA, is a statistical technique to convert high dimensional data to low dimensional data by selecting the most important features that capture maximum information about the dataset. The features are selected on the basis of variance that they cause in the output. The feature that causes highest variance is the first principal component. The feature that is responsible for second highest variance is considered the second principal component, and so on. It is important to mention that principal components do not have any correlation with each other.
