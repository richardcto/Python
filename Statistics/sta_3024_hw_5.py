#%%
# Simple program to find a and b coefficient given data
import numpy

# x, y data values
# Change these arrays for each answer
x = [43, 21, 25, 42, 57, 59]
y = [99, 65, 79, 75, 87, 81]

# Function to find coefficient b, coefficient a
# and Coefficient of determinatoin R-squared
def polyfit(x, y, degree):
    
    results = {}

    coeffs = numpy.polyfit(x, y, degree)

     # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = numpy.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = numpy.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = numpy.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = numpy.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination R^2'] = ssreg / sstot
    
    return results

print('First value is coefficient b, second is coefficient a', polyfit(x, y, 1))

#Find Correlation Coefficient, r
correlation_coefficient = numpy.corrcoef(x, y)

# Print Correlation Coefficient r
print('Correlation Coefficient r: ', correlation_coefficient)

# %%
