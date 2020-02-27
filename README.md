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

## Documentation

[Official Streamlit Documentation](https://docs.streamlit.io)

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

### Add text and data

#### Titles
```python
st.title("Here's my app.")
```

#### Write a data frame

```python
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

```

#### And also latex 

```python
st.latex(
    r'''
    \Pr(A|B)=\frac{\Pr(B|A)\Pr(A)}{\Pr(B|A)\Pr(A)+\Pr(B|\neg A)\Pr(\neg A)}
    '''
)
```

### Draw charts and maps

```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
```

### Maps
```python
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
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

## Interactive widgets

### Checkboxes

```python
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
```

### Selectbox

```python
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
```

### Sidebars

```python
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option
```
