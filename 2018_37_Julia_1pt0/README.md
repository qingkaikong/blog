
I think this week, the biggest news for me, maybe is [Julia 1.0 released](https://julialang.org/blog/2018/08/one-point-zero). It is a great language that I was thinking to learn for a long time (I just played it briefly before), therefore, I think I could use this 1.0 release as an excuse to learn it. 

Julia is a great language that has a goal to put the best features from different languages into one:

Using the reasons from [Wy we created Julia](https://julialang.org/blog/2012/02/why-we-created-julia):


> We want a language that’s open source, with a liberal license. We want the speed of C with the dynamism of Ruby. We want a language that’s homoiconic, with true macros like Lisp, but with obvious, familiar mathematical notation like Matlab. We want something as usable for general programming as Python, as easy for statistics as R, as natural for string processing as Perl, as powerful for linear algebra as Matlab, as good at gluing programs together as the shell. Something that is dirt simple to learn, yet keeps the most serious hackers happy. We want it interactive and we want it compiled.

See the key names of the languages: C, Ruby, Lisp, Matlab, Python, R, Perl, Shell, isn't really cool to learn this Julia! I will! 

### Setup the environment

Let's see how could we setup the environment using Jupyter notebook + julia (I really like to work in Jupyter notebook, therefore, this is my first step to set it up). I assume you already had Jupyter notebook. 

1. Download Julia from - [Download Julia](https://julialang.org/downloads/)
2. Add Julia into your .bashrc file - export PATH="/Applications/Julia-1.0.app/Contents/Resources/julia/bin:$PATH"
3. In the terminal, open Julia
4. In Julia, install IJulia:
    ![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_37_Julia_1pt0/figures/figure_0.png)
5. Open Jupter notebook, and select kernel: Julia 1.0.0 (note that, I had some old kernels when I played before)
    ![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_37_Julia_1pt0/figures/figure_1.png)
6. Let's run the famous 'Hello World!'


```julia
println("Hello World!")
```

    Hello World!

