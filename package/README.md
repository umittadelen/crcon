# crcon

crcon console is a python package that uses chromaconsole to change text color of cmd

* if ***requests*** is installed this package updates automaticaly
* some terminals still don't support *ANSI escape*

<br>

## Installation

```cmd
pip install crcon
```

<br>

## Functions
```cmd
crcon text <hex code>
#text color

crcon bg <hex code>
#text background color

crcon text reset
#reset text color

crcon bg reset
#reset bg color

crcon style <style>
#change text styling (italic, bold, doubleunderlined, faint, hidden, normalintensity, overlined, propspacing, reverse, strikethrough, underline)
```
<br>