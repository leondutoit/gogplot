
### gogplot - ggplot2 from python with pandas

I figure any self-respecting data person these days has their own attempt at making [ggplot2](http://ggplot2.org/) available from Python, especially with [pandas](http://pandas.pydata.org/) integration. So I just had to start my own...

In all seriousness though, ggplot2 is an absolutely wonderful implementation of the [Grammar of Graphics](http://www.amazon.com/The-Grammar-Graphics-Statistics-Computing/dp/0387245448) and is an indispensible tool for data analysis. Similarly pandas too is a brilliant toolset for working with data in Python. And it actually is a real problem that Python does not have a proper ggplot2-like package.

Various attempts at making such a package are under way. They are all commendable (and also maybe a bit more serious than this one). However, they are all incomplete. I decided to make the simplest implementation I could think of (maybe it is even more complete than some of the other attempts?).

### Dependencies

For this to work you will need both Python with pandas and R with ggplot2 installed.

### Quick start

```python
import pandas as pd
from gogplot import gogplot

# a simple scatterplot
df = pd.DataFrame({'x': [1,2,3,4,5], 'y': [33,7,60,5,43]})
gogplot(df, 'ggplot(data, aes(x, y)) + geom_point()')

```
