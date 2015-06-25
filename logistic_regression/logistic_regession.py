import numpy as np
import statsmodels.api as sm

from clean_data import clean_loan_data


df = clean_loan_data()
df['IR_TF'] = df['Interest.Rate'] < 12.0
df['intercept'] = 1.0

ind_vars = ['intercept', 'FICO.Score', 'Amount.Requested']

logit = sm.Logit(df['IR_TF'], df[ind_vars])
result = logit.fit()
coeff = result.params


def logistic_function(feature_vector, coef):
    xb = np.dot(feature_vector, coef)
    return 1.0/(1.0 + np.exp(-xb))

# Can we obtain a 10000 dollar loan with score of 720?
print 'p=', logistic_function([1.0, 720, 10000], coeff)
print 'p is > .7, so yes'
