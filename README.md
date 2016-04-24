# Forecasting Passenger Traffic Using Support Vector Regression with an RBF Kernel

Given an airport's total monthly passenger counts for a period of N months, forecast its passenger count for the next 12 months. 

Input Format

The first line contains an integer, N, denoting the number of months of passenger data. The N subsequent lines each contain the monthly passenger counts in the form of 2 tab-separated values:

    The first value is MonthNum_X, where X is an an integer denoting the month number.
    The second value is an integer denoting the number of passengers for that month.

Constraints

<img src="http://www.sciweavers.org/tex2img.php?eq=N%20%3C%20150&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="N < 150" width="71" height="15" />

Output Format

For each line i (where  1≤i≤12), print the forecasted passenger count for month number N+i on a new line.

