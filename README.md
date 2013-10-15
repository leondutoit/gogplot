
### gogplot - ggplot2 from python with pandas

I figure any self-respecting data person these days has their own attempt at making [ggplot2](http://ggplot2.org/) available from Python, especially with [pandas](http://pandas.pydata.org/) integration. So I just had to start my own...

In all seriousness though, ggplot2 is an absolutely wonderful implementation of the [Grammar of Graphics](http://www.amazon.com/The-Grammar-Graphics-Statistics-Computing/dp/0387245448) and is an indispensible tool for data analysis. Similarly pandas too is a brilliant toolset for working with data in Python. And it actually is a real problem that Python does not have a proper ggplot2-like package.

Various attempts at making such a package are under way. It is great that such projects are underway, but none of them are complete or stable enough yet. So I decided to make the simplest implementation I could think of for my own usage. It might even be more feature complete than the alternatives? I guess I'll find out soon enough :)

### Dependencies

For this to work you will need both Python with pandas and R with ggplot2 installed. How to do this has been documented in many other places.

### Quick start

```python
import pandas as pd
from gogplot import gogplot

# a simple scatterplot
df = pd.DataFrame({'x': [1,2,3,4,5], 'y': [33,7,60,5,43]})
gogplot(df, 'ggplot(df, aes(x, y)) + geom_point()')

```
