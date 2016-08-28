I recently saw the [20 Questions to Detect Fake Data Scientists](http://www.kdnuggets.com/2016/01/20-questions-to-detect-fake-data-scientists.html) on KDnuggests. Too bad, after I took go through the question lists, I found a lot of them I don't know how to answer, or only can answer partially. Results: I am a fake data scientists !!! :-). Anyway, to pretend I am a less fake one, I decided to prepare all the answers for these questions. Here are my answers, and if you use them to test me again, you will treat me as a genuine data scientists. I put these answers here more like a references/summary for me, if you spot any mistakes, please let me know to make me a better data scientists.     

1. **Explain what regularization is and why it is useful.**  
	A lot of the machine learning problems can be generalized into minimize a loss function to reduce the difference the model output and the true results. My understanding of the regularization is to add more constrains to the loss function to make sure that the parameters of the model can not change freely. This is in a sense reduce the flexible of the model, which means we will increase bias, but reduce variance in the error (to understand the bias and variance trade-off, check out this great blog [here](http://scott.fortmann-roe.com/docs/BiasVariance.html)). If we choose a reasonable regularization, we will get a nice trade-off between the bias and variance, and reduce the overfitting of the unwanted signal (noise) in the data. 
	
	Let's use [Lasso (L1 norm)](https://en.wikipedia.org/wiki/Lasso_(statistics)) or [Ridge (L2 norm)](https://en.wikipedia.org/wiki/Tikhonov_regularization) regression as an example. As we know, Lasso works by setting some of the parameters to very small number, or even zero, which means it is doing an internal feature selection to give you a subset of the features to work with. This small set of features makes your model less flexible, but less sensitive to the changes of the data (reduce the variance). Ridge regression is similar, but different in that it can not set the parameters to zero (it can set the parameters really small though). This is means it gives less weight on some of the parameters, in other words, treat them as nothing. It achieves the same goal of making the model less flexible to reduce the overfitting.  

2. **Which data scientists do you admire most? which startups?**  
	The following is a short list of my hero in this field (no purticular order, I just randomly think who I will add here), it may different from yours, or even missing some big figures. But remember, this is my list!  
	[**Geoff Hinton**](http://www.cs.toronto.edu/~hinton/), from University of Toronto, who is one of the main force to push neural network, and deep learning forward. I especially love this [video - The Deep Learning Saga](https://www.youtube.com/watch?v=mlXzufEk-2E)  
	[**Michael Jordan**](https://people.eecs.berkeley.edu/~jordan/) from UC Berkely. Just look at the list of his past students and postdocs, you will realize how many great experts he taught before! I took his class before, but at that moment, I can not understand all!  
	[**Trevor Hastie**](https://en.wikipedia.org/wiki/Trevor_Hastie) and [**Robert Tibshirani**](https://en.wikipedia.org/wiki/Robert_Tibshirani) I learned most of my machine learning knowledge from their books - [An introduction to Statistical Learning](https://www.amazon.com/Introduction-Statistical-Learning-Applications-Statistics/dp/1461471370/ref=sr_1_4?ie=UTF8&qid=1472255536&sr=8-4&keywords=Robert+Tibshirani) and [The Elements of Statistical Learning](https://www.amazon.com/Elements-Statistical-Learning-Prediction-Statistics/dp/0387848576/ref=sr_1_1?ie=UTF8&qid=1472255536&sr=8-1&keywords=Robert+Tibshirani). If you don't know who invented Lasso method we just talked above, google it!  
	[**Andrew Ng**](http://www.andrewng.org/), from Stanford. Most people knows Andrew probabaly from the coursera machine learning course. Recently, he is very active in machine learning field.   
	[**Tom M. Mitchell**](http://www.cs.cmu.edu/~tom/), from Carnegie Mellon University. I first know him is from his book [machine learning](https://www.amazon.com/Machine-Learning-Tom-M-Mitchell/dp/0070428077/ref=sr_1_12?ie=UTF8&qid=1472394494&sr=8-12&keywords=machine+learning), a very readable introduction.     
	[**Yann LeCun**](https://en.wikipedia.org/wiki/Yann_LeCun), another driving force in deep learning. He is best known for his contribution in the convulutional neural networks.   
	[**Christopher Bishop**](https://www.microsoft.com/en-us/research/people/cmbishop/), from University of Edinburdh. He was trained as a physists, but then later became an expert in machine learning. His book [Pattern Recognition and Machine Learning](https://www.amazon.com/Pattern-Recognition-Learning-Information-Statistics/dp/0387310738/ref=sr_1_2?ie=UTF8&s=books&qid=1263391804&sr=8-2#reader_0387310738) is another must have if you want to learn machine learning.   
3. **How would you validate a model you created to generate a predictive model of a quantitative outcome variable using multiple regression.**   
	I usually use [cross-validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics)) or [bootstrap](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)) to make sure my multiple regression works well. For determine how many predictors I need, I use [adjusted R^2](https://en.wikipedia.org/wiki/Coefficient_of_determination#Adjusted_R2) as a metrics, and do a feature selection using some of the methods described [here](https://en.wikipedia.org/wiki/Feature_selection). 

4. **Explain what precision and recall are. How do they relate to the ROC curve?**   
	

5. **How can you prove that one improvement you've brought to an algorithm is really an improvement over not doing anything?**   


6. **What is root cause analysis?**   


7. **Are you familiar with pricing optimization, price elasticity, inventory management, competitive intelligence? Give examples.**   


8. **What is statistical power?**   


9. **Explain what resampling methods are and why they are useful. Also explain their limitations.**   


10. **Is it better to have too many false positives, or too many false negatives? Explain.**    

   
11. **What is selection bias, why is it important and how can you avoid it?**     


12. **Give an example of how you would use experimental design to answer a question about user behavior.**   


13. **What is the difference between "long" and "wide" format data?**  


14. **What method do you use to determine whether the statistics published in an article (e.g. newspaper) are either wrong or presented to support the author's point of view, rather than correct, comprehensive factual information on a specific subject?**  


15. **Explain Edward Tufte's concept of "chart junk."**  


16. **How would you screen for outliers and what should you do if you find one?**  


17. **How would you use either the extreme value theory, Monte Carlo simulations or mathematical statistics (or anything else) to correctly estimate the chance of a very rare event?**  


18. **What is a recommendation engine? How does it work?**  


19. **Explain what a false positive and a false negative are. Why is it important to differentiate these from each other?**  


20. **Which tools do you use for visualization? What do you think of Tableau? R? SAS? (for graphs). How to efficiently represent 5 dimension in a chart (or in a video)?**