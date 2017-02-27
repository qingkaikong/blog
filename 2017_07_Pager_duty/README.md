As a graduate student at [Berkeley Seismological Lab](http://seismo.berkeley.edu/), doing pager duty is one of the things that accompany with you through your PhD study. Why called pager duty? You carry a pager with you and waiting for it to beep 24 hours for a week (The duty is rotating every semester). Whenever it beeps, you need sit in front of a computer, and working out the mechanism of the earthquake. This is a pager looks like:

![jpg](https://raw.githubusercontent.com/qingkaikong/blog/master/2017_07_Pager_duty/figures/pager.jpg)

Some of the young people may even don't know what is a paper, yes, we are still using it. It is amazing that there are still companies doing business with it. It has some advantages over the smartphone: the battery can last for months, it works at some places where no cell signal available, it is cool that we can show off to friends :-) etc. Overall, it does the job nicely. Like I mentioned, whenever this thing beeps, I need to work on the earthquake it reports in the next half hour to one hour, even in the middle of the night. Luckly, during my PhD life, I only got about 3 or 4 times that I need to do this 2 or 3 am in the morning. 

Ok, now you must curious what we will do after the pager beeps. Well, when it beeps, it means there is an earthquake larger than M3.5 in Northern California just now. Based on the waveforms recorded at seismic stations, a computer algorithm will generate a [Moment Tensor Solution](https://en.wikipedia.org/wiki/Focal_mechanism), which is a mathematical representation of the movement on a fault during an earthquake. This solution can tell us (mostly seismologists) how the fault actually moves. For the students' role, we need login a system, review the result and do a better version of Moment Tensor Solutions. Once the result is reviewed or a better version is made, we will publish it to USGS. It will on the USGS website as the following figure

[![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2017_07_Pager_duty/figures/solution_website_USGS.png)](http://earthquake.usgs.gov/earthquakes/eventpage/nc72113080#moment-tensor)

If you play around a little bit on the USGS website, and you can find more details about the solution the student did, here's an example I did in 2013:

[![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2017_07_Pager_duty/figures/solution_page.png)](http://www.ncedc.org/mt/nc72113080_MT.html)

Don't worry if you can not understand what is showing here, it is designed for seismologists. And if you really wants to know how it works, you can read this famous [A student's guide to and review of moment tensors](ftp://ftp.geo.uib.no/pub/LarsOttemoller/1989_srl_jost_herrmann_mt.pdf). You can also check out the following video to get an idea of focal mechanism, which is a very close concept. You will understand how to read a beach ball. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/MomVOkyDdLo" frameborder="0" allowfullscreen></iframe>

I think it is really cool that we students can contribute to the USGS earthquake website and leave our names there forever (I assume USGS earthquake page will last forever, as long as we still have earthquakes). 

Anyway, the pager duty is part of our graduate students' life, and I believe that we will miss the feeling of doing duty in the middle of night after we graduate. 

### Fun facts
1. The pager will beep two times a day for testing purposes, noon and 3:30 pm. That's usually the time when we show off to friends or get curious looking on other people's faces. 
2. During one duty (7 days), students will experience 0 or 1 earthquake most of the time. Some lucky ones will have earthquake swarm during their duty :-)
3. The average time to finish one earthquake is about 1 hour. 
4. We swtich duty on Wednesday.  

I downloaded the earthquake larger than M3.5 in Northern California (latitude 36 to 42, longitude -125 to -117, this is just a rough region) from 2011 to 2017, and made some quick figures to show some interesting facts. 

#### When the earthquakes happen?
![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2017_07_Pager_duty/figures/distribution_of_eq.png)

It seems we have more earthquakes around the end of 2014. 

#### Which hour during the day the earthquakes happen?
![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2017_07_Pager_duty/figures/hist_day_hour.png)

We see cleary two peaks around 12 am, how many of us remember the earthquakes wakes up in this time period, hands up! I at least have two cases in my memory. Also, earthquakes don't like noon, since everyone is at lunch :-)

#### Which weekday the earthquakes happen?

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2017_07_Pager_duty/figures/hist_weekday.png) 

Of course, Saturday pops up ..., you guys can not go hikings on Sa:-) It is actually interesting

#### Number of earthquakes each week?

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2017_07_Pager_duty/figures/weekly_eqs.png)

This figure shows the number of earthquakes in each week (Wedesday to next Wedsday), I am wondering who is the lucky one that have 15 earthquakes during the duty :-) Definitely not me.

#### How many earthquakes we usually do during duty?
![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2017_07_Pager_duty/figures/weekly_hist.png)

This histogram shows us most students did 1 or no earthquakes during the duty week (the top two bars show). The following table is a quick statistic summary of the earthquake counts. The mean is 1.24 earthquakes per duty, and 50 percentile is 1 earthquake, and 2 earthquakes for 75 percentile. For today, I already did two earthquakes (lucky day), maybe I will do more earthquakes this duty and fall on the tails of the histogram. 

|   |   |
|:-:|:-:|
| count |  313 | 
| mean |  1.23 | 
|  std |  1.90 | 
|  50% |  1 | 
|  75% |  2 | 
|  max |  15 | 
  
##Why do we have an alarm response team? Why do we have to get up in the middle of the night to look at earthquakes?
 
This is copied from [our Lab website](http://seismo.berkeley.edu/)! 

As a seismological observatory, the Berkeley Seismological Laboratory has been involved in "earthquake information" for over a century. Part of our mission is to monitor earthquake activity and to provide "timely and accurate" information to state and federal agencies, to the media, and to the public.

Our primary responsibilty is for local earthquakes. This has led to the development of the REDI project and the joint notification system with the USGS Menlo Park. Since much of this processing is automated, the Alarm Response workload has been significantly lightened. However, it is extremely important that the UCB alarm response people carefully review - and update, if necesssary - information for larger events. This reviewing process must be done in collaboration with the USGS person on duty.

We also have a responsibility to respond to regional and teleseismic events. In this situation, our duties are to provide supporting information for the "authoritative" agency - for example, Caltech, the University of Washington, or NEIC. In general, we do not formally release our locations and magnitudes to the press if we have a solution from the authoritative group.

## Conclusion

This blog is written because this maybe my last duty since I will graduate soon and will be off duty. I even feel a little sad, the pager duty experience is somewhat fun while frustration, and already been part of my life. I hope future students will enjoy the experience, and when I talk with them in the future, raise so much memories from me. 

