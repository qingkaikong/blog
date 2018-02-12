Recently, our new paper '[Structural Health Monitoring of Buildings Using Smartphone Sensors]((https://pubs.geoscienceworld.org/ssa/srl/article/525824/structural-health-monitoring-of-buildings-using) )' is out, which is part of our exploration of what MyShake data could be used. 

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_04_SHM_smartphone/figures/figure_0.png)

Think about this: most of the smartphones will be used inside a building, for example, at night, your phone is in your building, and during the day, it is likely to be in your office building. If we could utilize the phones in the building to record the movement of the building during the earthquake, could we monitor the health state of the buildings? This is what we want to show in the paper by doing a shaker test, which you can find the description from my [previous blog](http://qingkaikong.blogspot.com/2016/10/how-to-shake-9-story-building-on.html). 

In the paper, we propose to use the smartphones to potentially extract the fundamental frequency of the building before and after the earthquake as a way to monitor the health state of the building. Why the fundamental frequency change can work as an indicator of the health state of the building? Let's have a look below. 

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_04_SHM_smartphone/figures/figure_1.png)

If we think we use a tractor pull the house with a rope, and what will happen if we cut the rope suddenly?

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_04_SHM_smartphone/figures/figure_2.png)

The building will start to move back and forth for a while as shown in the above picture. It is basically can be seen as an inverted pendulum that could oscillate at a certain frequency (or period if you are more familiar with this, the period is just 1/frequency). The building will move back and forth at certain period T, but with a decaying amplitude of the shaking. 

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_04_SHM_smartphone/figures/figure_3.png)

Bud different buildings have different characters in terms of oscillation, some oscillate with high frequency (fast) and some oscillate with low frequency (slow) as shown in the above figure. A rule of thumb is the taller the buildings are, the lower frequency they are. The fundamental frequency reflects the nature of the building, with softer building have lower frequency. 

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_04_SHM_smartphone/figures/figure_4.png)

Different earthquakes may cause various damages to the same building, with larger earthquakes causing more damage. These damages to the building will cause the building become softer, thus change the fundamental frequency of the building decrease. 

Therefore, if we know the fundamental frequency of the building before an earthquake, and we could measure the fundamental frequency of the building during the earthquake, we may get a sense of how much the building damaged during the earthquake. This is our idea of using smartphone sensors to extract the fundamental frequency of the building during the earthquake, you could see the details in the paper. 

Of course, there are still a lot of things need to be done to prove it, for one example, how do we find out which floor the phones are. But we do think that the smartphones to monitor the buildings is promising. 

Acknowledgement:
The first figure I found online, but I couldn't remember from where, but I thank the authors for making this image. For the rest of the images, it is all from [NICEE - Earthquake Tips](https://www.nicee.org/EQTips.php), which is a very nice series about the basics of earthquake engineering. 