
Numpy, short for Numerical Python, is the foundation on which nearly all of the higher-level tools are built. Below 
are some of the things it provides:

- ndarry, a fast and space-efficient md array
- standard math funcs
- tools for reading/writing array data to disk and working with memory-mapped files
- linear algebra
- tools for integrating code written in C/C++ or Fortran

For most data analysis apps, the main areas of functionality include:

- Fast vectorized array operations for data munging and cleaning, subsetting and filtering, transformation, and any 
other kind of computations
- Common array algorithms like sorting, unique and set ops
- Efficient descriptive stats and aggregating/summarizing data
- Data alignment and relational data manipulations
- Expressing conditional logic as array exps
- Group-wise data manipulations (aggregation, transformation, func app)

**dtype**

It's worth keeping in mind that floating point numbers, such as those in float64 and float32 arrays, are only capable
 of approximating fractional quantities.
 
**Operations between Arrays and Scalars**

Any arithmetic operations between equal-size arrays applies the operation element-wise.

**Indexing**

**Fancy Indexing**

A term adopted by Numpy to describe indexing using integer arrays.


**Universal Funcs**

ufunc is a function that performs elementwise operations on data in adarrays.

