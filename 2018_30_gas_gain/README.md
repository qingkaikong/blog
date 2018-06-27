
We know objects are expanding when the temperature goes up. Therefore, I always think that I should fill in my gasoline in my car in the early morning, so that I could have more gasoline when I spend the same money. But how much really we could gain if the temperature changes fill in gasoline at 60&deg;F instead of 80&deg;F (this is actually the changes of temperature at Berkeley during morning and noon). To calculate the change of the gasoline, we need to use the physics that we learned in high school, the basic equation is the following one, that relate the volume change of an object to the temperature change. 

$\Delta$V = $\beta\times T \times \Delta$T

$\Delta$V is the change of the volume, and $\beta$ is the average coefficient of volume expansion, and the V is the initial volume of the object, and $\Delta$T is the change of the temperature. Therefore, all we need to do is to find the [coefficient of volume expansion](http://www.kshitij-iitjee.com/Thermal-expansion/), and it is $9.6\times 10^{-4}/C$&deg;, that is $5.33\times 10^{-4}/F$&deg;. Now, let's assume that we fill in 10-gallon gasoline in the morning at 60&deg;F and how much it will be at noon (80&deg;F)


```python
delta_v = 5.33e-4 * 10 * 20
print('We gain %.2f gallon gasoline, \nif we fill in the morning instead of noon.'%delta_v)
```

    We gain 0.11 gallon gasoline, 
    if we fill in the morning instead of noon.


Well, it is 0.11-gallon difference if we fill in 10-gallon gasoline in the morning (that is, we will have 10.11-gallon at noon when temperature increases to 80&deg;F). Let's calculate how much we potentially can save if we drive our car for certain distances.  

Let's say your car's average MPG is 30, for 150,000 miles, we need 150,000 / 30 = 5000 gallon gasoline. The difference of gasoline will be $5000 / 10 \times0.11 = 55$ gallon. 
