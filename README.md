
### gogplot - ggplot2 from python with pandas

I figure any self-respecting data person these days has their own attempt at making [ggplot2](http://ggplot2.org/) available from Python, especially with [pandas](http://pandas.pydata.org/) integration. So I just had to start my own...

In all seriousness though, ggplot2 is an absolutely wonderful implementation of the [Grammar of Graphics](http://www.amazon.com/The-Grammar-Graphics-Statistics-Computing/dp/0387245448) and is an indispensible tool for data analysis. Similarly pandas too is a brilliant toolset for working with data in Python. And it actually is a real problem that Python does not have a proper ggplot2-like package.

Various attempts at making such a package are under way and they are all commendable - and also maybe a bit more serious than this one. But anyways, I decided that I would try to make ggplot2 available to me when I am working with pandas in Python and I have tried here to do it in the absolute simplest way I could think of. And yes the name `gogplot` is terribly ugly, but so is the implementation :)

### Dependencies

For this to work you will need both Python with pandas and R with ggplot2 installed.
