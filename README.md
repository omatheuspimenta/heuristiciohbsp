# heuristiciohbsp
Heuristic Methods for Minimizing Cut Bars and Using Leftovers from the One-dimensional Cutting Process - IOH-BSP Heuristic.

## Getting Started
#### Dependencies
You need Python 3.8 or later to use **heuristiciohbsp**. You can find it at [python.org](https://www.python.org/).

#### Installation
Clone this repo to your local machine using:
```
git clone https://github.com/omatheuspimenta/heuristiciohbsp.git
```
or
```p
pip install heuristiciohbsp
```

## Features
In this heuristic, the losses of the cutting process are concentrated on the smallest number of bars possible, using a greedy structure, in order to become losses (unusable) into leftovers (usable). 

## Example
```python
from heuristiciohbsp import bsp

n = 7
L = 30
l = [7, 9, 11, 14, 19, 21, 26]
d = [2, 3, 2, 2, 2, 1, 1]

left = loss = bar = 0
x = []

left,loss,bar,x = bsp.ioh(L=L, n=n, l=l, d=d)
```
## Input and Parameters
* **L:** Size of bar to be cutting. _(int)_
* **n:** Number of Items to be cutting. _(int)_
* **l:** Lenght of items to be cutting. _(list)_
* **d:** Demand of items to be cutting. _(list)_
* **smallitem:** Size of small item. Default is the smallest item to be cutting. _(int)_

## Output 
* **left:** Leftover from the cutting process. _(int)_
* **loss:** Loss from the cutting process. _(int)_
* **bar:** Bar number used in the cutting process. _(int)_
* **x:** Cutting pattern. _(list)_

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Citation
If you use this software in your work, please cite our paper. (soon)

## License
[MIT](https://choosealicense.com/licenses/mit/)
