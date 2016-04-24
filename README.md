# Forecasting Passenger Traffic Using Support Vector Regression with an RBF Kernel

Given an airport's total monthly passenger counts for a period of N months, forecast its passenger count for the next 12 months. 

Input Format

The first line contains an integer, N, denoting the number of months of passenger data. The NN subsequent lines each contain the monthly passenger counts in the form of 22 tab-separated values:

    The first value is <img src="http://www.sciweavers.org/tex2img.php?eq=MonthNum%5C_X&bc=White&fc=Black&im=jpg&fs=12&ff=mathdesign&edit=0" align="center" border="0" alt="MonthNum\_X" width="121" height="18" />, where X is an an integer denoting the month number.
    The second value is an integer denoting the number of passengers for that month.

Constraints

<img src="http://www.sciweavers.org/tex2img.php?eq=N%20%3C%20150&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="N < 150" width="71" height="15" />

Output Format

For each line i (where <img src="http://www.sciweavers.org/tex2img.php?eq=1%20%5Cle%20i%20%5Cle%2012&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="1 \le i \le 12" width="83" height="17" />), print the forecasted passenger count for month number N+i on a new line.

