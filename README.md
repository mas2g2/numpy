07/27/2018
Email: mileshshah@gmail.com

This application runs basic statistical analysis on either one or two sets of numbers
specified by the user

The statistical analyses include:
- mean
- median
- mode
- standard deviation
- variance
- linear regression

To run statistical analysis on one array execute the following command:

"python bsf.py # # # ..." (Each pound sign represents a number that the user will add to an array)
(The user can add as many numbers as he/she wants to add)

To run a statistical analysis that includes linear regression the user will need to add to sets 
of numbers, for this the user will run the following command:

"python bsf.py # # # ... / # # # ..." (The forward slash sign will indicate the begining of a new
list. Both lists must contain the same amount of numbers for linear regression)

To run this program the user must install the following:

- Python2.7
- NumPy
In this program wee also include a node.js file that can extract the statistical analysis data from the 
python file am can save it in a string variable tht can be stored as a JSON object^
To run the node.js file the user will run command:
"node get-bsf-data.js # # # ..." or "node get-bsf-data.js # # # ... / # # # ..."


