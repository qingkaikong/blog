Continue from [previous blog](http://qingkaikong.blogspot.com/2016/10/machine-learning-1-what-is-machine.html), we will talk about types of Machine Learning (ML) this week. 

# Three types of common ML
![Figure 0](https://www.safaribooksonline.com/library/view/python-machine-learning/9781783555130/graphics/3547_01_01.jpg "machine learning")

## 1. Supervised Learning
![Figure 1](https://media.licdn.com/mpr/mpr/shrinknp_800_800/AAEAAQAAAAAAAAQJAAAAJDJlZmMwOTZiLTNlNDgtNDI0ZC04NzY5LWVkNDI2ZTk1ZmFlYw.jpg "machine learning")  

**Example**: I try to teach a small baby to recognize apple from orange. I will first give it an orange, and tell it this is an orange. Then the baby will remember the features of this orange, i.e. shape, yellowish color, smell, texture, and so on. 

Next, I give the baby an apple, and tell it, this is an apple. Again, it remembers the features of the apple (red color, texture is smoother than the orange, a different smell). 

Finally, I give the baby another object, but not telling what this object is. The baby will compare the features of this object with that it memorized for the apple and orange, and see which one matches. 

**More Explain**:  
For this example, the apple and orange recognition, is a classic classification problem. It has two classes: apple and orange. Features are the usually the most important part of the model building process. Note that, we give the baby an apple and orange, and tell it what the object is. This is the training data for building the model in the baby's mind. The fact we give it the true class of the object (apple or orange) is the label of the training data, this is also why it is called supervised learning. It is more like, I am a teacher, and gives the baby the true answer for it to learn. See more on [WiKi](https://en.wikipedia.org/wiki/Supervised_learning). 


## 2. Unsupervised Learning  
![Figure 2](http://blogs.ubalt.edu/academicinnovation/wp-content/uploads/sites/38/2015/05/ApplesOranges.jpg "unsupervised learning")       

**Example**: Let's just give the baby many apples and oranges without telling it what the objects are. Then the baby just learn by itself, and put all the oranges into one box, and all the apples to another box, based on color, texture, and maybe smell. 

**More Explain**: In this example, we can see the difference from the previous example - there are no labels associated with the training data (the baby doesn't know which is apple, and which is orange). But it can learn by itself and find some interesting difference between the two, and put them into groups. Due to we don't teach the baby with the labels, this approach is called unsupervised learning. See more on [WiKi](https://en.wikipedia.org/wiki/Unsupervised_learning). 
 
## 3. Reinforcement Learning
![Figure 3](http://images.rcp.realclearpolitics.com/253490_5_.png "reinforcement learning")  

![Figure 4](http://espanol.babycenter.com/blog/wp-content/gallery/las-madres-y-las-manchas/captura-de-pantalla-2013-04-10-a-las-00-39-02.png "reinforcement learning") 


**Example**: The first time when a baby tries lemon, it is a memorable time. This is also an experience that the baby actively learning the world. It will understand that lemon tastes not good after a few tries. In contrasts, chocolate is different experience. After the baby tastes it, it will remember and ask for more soon. 

This is actually reinforcement learning. The baby learns from award (chocolate) or punishment (lemon) experience. 

**More Explain**: Reinforcement learning allows machines and software agents to automatically determine the ideal behavior within a specific context, in order to maximize its performance due to award or punishment. See more on [WiKi](https://en.wikipedia.org/wiki/Reinforcement_learning). 

## 4 Others  
There are also other types, as [semi-supervised learning](https://en.wikipedia.org/wiki/Semi-supervised_learning) or [transduction](https://en.wikipedia.org/wiki/Transduction_(machine_learning)), which is kind of hybrid from supervised and unsupervised learning. I will not provide examples here. 

# Another way to divide ML types

## 1 Classification
You can see the example for the supervised learning above.  

## 2 Regression  
![Figure 4](http://digital.library.lse.ac.uk/objects/lse:hub777nep/view "regression")  

**Example**: If I ask you what is the height of a X month baby (from birth to two years old), how can you answer that? We can ask babies in different ages, and record their heights, and then whenever you ask me, for example, what is the height of a 18-month baby, we can plug in the 18 month, and find the corresponding height. This is a basic regression analysis. 

**More Explain**: Regression is a process for estimating the relationships among different variables (for the example here, the variables are age and height). See more on [WiKi](https://en.wikipedia.org/wiki/Regression_analysis). 


## 3 Clustering
You can see the example for the unsupervised learning above.   

## 4 Dimensionality reduction

![Figure 5](http://static.fjcdn.com/pictures/World_b627d6_1081870.jpg "dimensionality reduction") 

**Example**: We live in a 3 dimensional world, but when we plot on maps, it is much easier to plot them as a 2 dimension map instead of 3. 

**More Explain**: Dimensionality reduction is the process of reducing the number of random variables under consideration. See more on [WiKi](https://en.wikipedia.org/wiki/Dimensionality_reduction). 

## Density Estimation  
![Figure 6](http://www.publicdomainpictures.net/pictures/30000/velka/koi-fishes.jpg "density estimation")
**Example**: When you go fishing, there are two equal size lakes A and B. At lake A, you can easily have 10 fishes in one hour. But at lake B, you only get one fish in the same amount of time. Well, we can say that the density of the fish in lake A is probably higher than that of lake B. 

**More Explain**: Density estimation is the construction of an estimate, based on observed data, of an unobservable underlying probability density function. See more on [WiKi](https://en.wikipedia.org/wiki/Density_estimation). 

All the figures are from internet, I thank the authors for the figures! 