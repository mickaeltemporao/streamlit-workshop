# Streamlit Workshop 

### What 
- Quickly build interactive web application 
- Without dev knowledge but of course helps to have some...

### 3 Principles
- Embrace Python scripting
- Weave in interaction
- Deploy instantly

## System requirements

Requires Python, 3+ and poetry ...

## Installation

```shell
mkdir streamlit-workshop
cd streamlit-workshop
poetry init
poetry add pandas, streamlit
poetry shell
```

## Example

### Hello World

Building web apps in streamlit is real^100y easy.

```python
import streamlit as st

st.write('Hello folks!')
```

then simply run

```shell
streamlit run app.py
```

This `st.write` is the swiss-army knife of Streamlit commands. 
It does different things depending on what you throw at it.

### Latex

```python
st.latex(
    '''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    '''
)
```


## Streamlit Magic

Magic commands are a feature in Streamlit. 
They allow you to quickly write markdown and data to your app. 

Here’s an example:

```python
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df  # <-- Draw the dataframe

x = 10
'x', x  # <-- Draw the string 'x' and then the value of x
```

