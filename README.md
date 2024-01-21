# CodeYourPath project

Here will be all the documentation.

## Installing libraries
To install libraries run
```shell
pip install -r <path_to_requirements.txt_file> 
```

## Notebooks
To run notebooks using command line **(Terminal)** use this command:
```shell
jupyter notebook <path_to_notebook>
```
`<path_to_notebook>` is replaced your path, be it windows path
or linux.


## `Quadratic.py`
Calculates x values for specified quadratic 
equation coefficients - `ax^2 + bx + c = 0`. 
### Usage
To execute the script and calculate roots of quadratic
equation, run the following command in your terminal:
```bash
python Quadratic.py --a <a_coef> --b <b_a_coef> --c <c_coef> 
```
#### Command Line Options
- `a_coef` - `a` coefficient of quadratic equation (`ax^2`)
- `b_coef` - `b` coefficient of quadratic equation (`bx`)
- `c_coef` - `c` coefficient of quadratic equation (`c`)

### Example
We want to solve equation `x^2 - 6x + 2 = 0`. To solve it
using our program we pass the variables in such way:
```bash
python Quadratic.py --a 1 --b -6 --c 2
```
The output of such program looks like 
```bash
Result = [5.645751311064591, 0.3542486889354093]
```

---