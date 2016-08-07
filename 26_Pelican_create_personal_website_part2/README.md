This is the personal website generated by [Pelican](https://github.com/getpelican/pelican) based on [Qingkai's Tutorial part 2](http://qingkaikong.blogspot.com/2016/07/create-personal-website-with-pelican.html).

Let's continue to build a personal website from the [part 1 of the blog](http://qingkaikong.blogspot.com/2016/07/create-personal-website-with-pelican.html). This week, we will see how to change to a different theme, add images, videos, attach files, and publish the sites. 

## Change a theme  
You can change the theme of your website. You can either [create your own theme](http://docs.getpelican.com/en/3.6.3/themes.html), or there are already many existing themes that you can use, see these [nice themes](https://github.com/getpelican/pelican-themes). I won't bother to create my own theme, so I will use the existing ones. You can have a look of [different themes](http://www.pelicanthemes.com/). Now, let's start to change themes. All you need do is to download these themes, say I store it in my Download folder. If I want to use a theme, for example, 'subtle'. I can follow the steps: 
 
```bash
# this will install the theme
$ pelican-themes -i ~/Downloads/pelican-themes-master/subtle
# list all the themes on you machine
$ pelican-themes -l
# use the theme
$ pelican content -t subtle
# Now you should see the change of the theme on your website (reload if you didn't see it).
```

Note: If you want to change something on the theme, before you install it, go to the folder and change the html template or the css files. 

## Add an image or video
Adding an image or video is simple, just add the html code into the markdown file, then you will have them, all you need do is to adjust the alignment and position.   

Add an image

```html
<img align="left" src="./images/iron_man.jpg" alt="Drawing" style="width: 200px;"/>
```

Add a video: 
 
```html
<div style="margin: 0px auto; text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/WSYRkTTcEg0" frameborder="0" allowfullscreen></iframe></div>
```

## Attach file
This is how you attach a file:

```markdown
You can download iron man's image [here]({filename}../images/iron_man.jpg)
```

## Add Google Analytics
Add google analytics to track the visits of your site is quite simple in pelican, all you need do is to change the trackID field GOOGLE_ANALYTICS in the publishconf.py file. To get the track ID from google analytics, you can follow the steps [here](https://support.google.com/analytics/answer/1008080?hl=en)

## Publish your site  
There are many ways to [publish your site](http://docs.getpelican.com/en/3.6.3/publish.html). I am using [Fabric](http://www.fabfile.org/) to publish my site. Change the remote server configuration in the fabfile.py:

``` text
# Remote server configuration
# this is your remote server address and port
production = 'username@XXXX.XXX.berkeley.edu:22'
# this is the folder contains all your site content
dest_path = '/home/kongqk/public_html'
```

Ok, you almost done, after you modified your site, and you can publish it using:

```bash
$ fab build
$ fab publish
# then type your login information!
``` 