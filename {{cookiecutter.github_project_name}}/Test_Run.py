
# coding: utf-8

# In[1]:

import numpy as np
import {{ cookiecutter.python_package_name }} as xt

from IPython.display import display


# ### Function example1

# In[25]:

print(xt.example1.__doc__)


# In[6]:

a = np.arange(15).reshape(3, 5) + 5
b = xt.example1(a)
display(a)
display(b)


# ### Function example2

# In[26]:

print(xt.example2.__doc__)


# In[7]:

a = np.arange(15).reshape(3, 5)
b = xt.example2(a)
display(a)
display(b)


# ### Function readme_example1

# In[27]:

print(xt.readme_example1.__doc__)


# In[31]:

PI = np.pi
a = np.linspace(0, PI, 100)
b = xt.readme_example1(a)
display(a)
display(np.sin(a).sum())
display(b)


# ### Function vectorize_example1

# In[28]:

print(xt.vectorize_example1.__doc__)


# In[37]:

PI = np.pi
a = np.linspace(0, PI, 10)
b = np.linspace(0, 2*PI, 10)
c = xt.vectorize_example1(a, b)
d = np.sin(a)+np.cos(b)
display(a)
display(b)
display(c)
display(np.isclose(c, d))

