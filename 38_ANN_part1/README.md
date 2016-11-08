From this week, I will try to cover the basics of [Artificial Neural Network](https://en.wikipedia.org/wiki/Artificial_neural_network) in a simple and intuitive way. Let's start with a brief history of the artificial neural network. 

## Brief history of neural network  
Since there are many good introductions already online, I will just list the following important periods, you can check out this nice blog for more - ['A Concise History of Neural Networks'](https://medium.com/@Jaconda/a-concise-history-of-neural-networks-2070655d3fec#.ekc89166m). The important period for neural networks are:   

**1940s** - The beginning of Neural Networks (Electronic Brain)   
**1950s and 1960s** - The first golden age of Neural Networks (Perceptron)   
**1970s** - The winter of Neural Networks (XOR problem)  
**1980s** - Renewed enthusiasm (Multilayered Perceptron, backpropagation)  
**1990s** - Subfield of Radial Basis Function Networks was developed  
**2000s** - The power of Neural Networks Ensembles & Support Vector Machines is apparent  
**2006** - Hinton presents the Deep Belief Network (DBN)  
**2009** - Deep Recurrent Neural Network  
**2010** - Convolutional Deep Belief Network (CDBN)  
**2011** - Max-Pooling CDBN

I also found this [cool figure](http://www.slideshare.net/deview/251-implementing-deep-learning-using-cu-dnn/4) online, which shows clearly the progress of neural network:  

![Figure 1](https://raw.githubusercontent.com/qingkaikong/blog/master/38_ANN_part1/figures/figure1_ANN_history.jpg "Brief history of neural network") 

## What is neural network and how it works  
First, how our brain works to recognize things? Too bad, no one knows the exact answer. Many researchers worked actively on this and try to find the truth. The past research already gave us much knowledge of how the brain works. In a much simplified version: in our brain, we have billions of neurons that do the computation to make the brain function correctly, like recognize apple or orange from some images, memorize certain things, making decisions, etc. These neurons are the basic element in the brain to process information. They connected to each other, and based on different stimulate from outside world, they can fire a signal to certain other neurons. The fired neurons will form different patterns to respond different situation, and this makes our brain can do a lot of amazing things. See the fired neurons in the following figure:   

![Figure 2](https://raw.githubusercontent.com/qingkaikong/blog/master/38_ANN_part1/figures/figure2_how_brain_works.jpg "Neurons in the brain")   

The Artificial neural network (ANN) is a mathematical tool to modeling the above brain process to certain degree (the truth is, we can only model the very basic things, and many more complicated processes that we even don't understand). It has the basic component of how the brain works: the neurons, the firing capability, the learning capability and so on. On a very high level, ANN can be simplified to the following model:  

![Figure 3](https://raw.githubusercontent.com/qingkaikong/blog/master/38_ANN_part1/figures/figure3_Input_output_system.png "Input and Output system")  

This simplified ANN model will have 4 parts: the input layer, the process layer, and the output layer plus a feedback process. Information first comes and enters into the system via the input layer. The ANN will process the input information and generate an output at the output layer which can be evaluated and give feedback to the input layer to adjust how the information enters into the system. Note that, this feedback and adjust the input is essentially the learning part of the ANN model, since doing this many times will adjust the model to fit the data well, a process we can think as learning from the data. For the ANN model, since we usually only see the input and output layer, and the process layer is kind of like a black-box to us, we usually call it, the hidden layer.      

More formally, what you will usually see when study ANN is the following figure:  

<img src="https://raw.githubusercontent.com/qingkaikong/blog/master/38_ANN_part1/figures/figure4_Artificial_neural_network.jpg" width="600"/> 

Likely, you already see the connection with the figure we just talked about. The input layer, hidden layer (process), output layer. Each of the input node (circle) will take one input and push it to the ANN model via the links (shown as the black arrows, they represent how strong the signals are from the input layer to each of the neurons) to the hidden nodes (we can also call it neurons in the hidden layer). The neurons in the hidden layer will process this information, and pass it to the output layer, again via the links. What's missing on this figure is the feedback process, which means we evaluate the output with the true results, and go back to adjust the strength of the links both in the input layer and output layer, to enhance some good data or to reduce some bad ones. Usually, we do this backward from the output layer to the input layer, this is also the reason it is called backpropagation.   

Let's talk a little more about the information flow and the role of the links. The information enters into the ANN model from the input layer, and we can see each of the input nodes is actually connected with all the neurons in the hidden layer. Like we said before, the links represent the strength, we call them weights. We can think them as pipes connected input nodes and neurons. They will control how much information will pass through. The larger the weights (larger size of the pipe), the more information will pass from certain input node, vice versa. The same thing for the hidden layer to the output layer as well. These weights/links can control how important/much of certain information pass across the network. We can initialize the ANN model with small random weights (both postive and negative values), and after we evaluate the output results from the ANN model and the true results, we will find some input information is more important than others to get the results correct, while others will make things worse. Now for the information make the results correct, we can either not change the weights or change very little, but for the ones making things wrong, we will change the weights towards they contribute to the correct contribution. This is the role of the links or weights.  

![Figure 5](https://raw.githubusercontent.com/qingkaikong/blog/master/38_ANN_part1/figures/figure5_weights.jpeg "weights")  

## Simple Example 
If you still confused with the above explanation, let's see a simple example to gain more sense how ANN works (This is not an accurate example to show how an ANN works, but it shows the most important part of the algorithm).   

Let's say we have many pictures of [president Obama](https://en.wikipedia.org/wiki/Barack_Obama) and [Dr. Sheldon Cooper](https://en.wikipedia.org/wiki/Sheldon_Cooper). We want the ANN algorithm to recognize which picture is President Obama and which one is Dr. Sheldon Cooper.   

<img src="https://raw.githubusercontent.com/qingkaikong/blog/master/38_ANN_part1/figures/figure6_sheldon_and_obama.jpg" width="600"/> 

### Step 1 Information pass through network 
The first step is to pass the information through the network, and we can see we have many pictures of president Obama to pass in the network. In order to recognize the picture, we need to find some clear characteristic features to make the classification. We can choose eye, nose, mouth, skin color, hair style, head shape, teeth, and so on as different features. In the hidden layer, we have n neurons, and you can see there are n links/weights connect these features to the neurons. Each of the features we select will have n links to all the neurons, and the neurons work like a big function that aggregate the information (this is shown as the function in the picture, F(eye\*w1 + nose\*w2 + ... + mouth\*wn)). The generated output from the neurons in this case is Dr. Sheldon cooper. We can see the information from the input layer propagate through the whole network to the output layer.  

<img src="https://raw.githubusercontent.com/qingkaikong/blog/master/38_ANN_part1/figures/figure7_ANN_example_1.jpg" width="600"/> 

### Step 2 Information feedback 
Now, we need to evaluate the results from the ANN. We can see the correct answer is president Obama. Clearly, the ANN algorithm made a mistake, and by comparing with the correct answer, we can get an error, which we will use as the basis to update the weights to reflect the fact that it made a mistake. This is the feedback process. 

<img src="https://raw.githubusercontent.com/qingkaikong/blog/master/38_ANN_part1/figures/figure8_ANN_example_2.jpg" width="600"/> 

### Step 3 Update weights   
The errors from previous steps may be contributed by some features, for example, the shape of the head, or the hair style all confused the ANN to make the wrong decision. What we need to do is to update the weights associated with them so that to reduce the error. If the features can capture the difference, say, the skin color, then we may just update very small number to the weight associated with it, or even not update it. The blue color weights which reflect the facts that we updated them. With many data feeding into the network (training data) and updating the weights many times, the ANN will learn how to make the correct decision. Of course, the update is based on some rules we will talk in the next few weeks.      

<img src="https://raw.githubusercontent.com/qingkaikong/blog/master/38_ANN_part1/figures/figure9_ANN_example_3.jpg" width="600"/> 

### Step 4 Recognize correctly  
After training the ANN with many data, the weights have already been updated to capture the difference from the images of this two persons. Therefore, when we pass through the images of president Obama, and we can get the correct answer out!   

<img src="https://raw.githubusercontent.com/qingkaikong/blog/master/38_ANN_part1/figures/figure10_ANN_example_4.jpg" width="600"/> 

The example we show here just gives you a sense of how ANN works, and for more details, we will talk in the future posts.  


## Acknowledgements
All the figures are from the internet, I thank the authors for the figures!  

## More reading  
[A Concise History of Neural Networks](https://medium.com/@Jaconda/a-concise-history-of-neural-networks-2070655d3fec#.shsa54ev6)  
[Neural networks](https://cs.stanford.edu/people/eroberts/courses/soco/projects/neural-networks/index.html)   
[What is a simple explanation of how artificial neural networks work](https://www.quora.com/What-is-a-simple-explanation-of-how-artificial-neural-networks-work-1)  

