
P45
Act without doing, work without effort. Think of the small as large and the few as many. Confront the difficult while it is still easy; accomplish the great task by a series of small acts. The Master never reaches for the great; thus achieves greatness. (ch. 63)

为无为，事无事，味无味。
大小多少，报怨以德。
图难于其易，为大于其细。
天下难事，必作于易；天下大事，必作于细。

IPython project began in 2001 as Fernando Perez's side project to make a better interactive Python interpreter.

While it does not provide any computational or data analytical tools by itself, IPython is designed from the ground
up to maximize your productivity in both interactive computing and software development.

It encourages an execute-explore workflow instead of the typical edit-compile-run workflow.

**Learning**

As with any keyboard-driven console-like env, developing muscle-memory for the common commands is part of the 
learning curve.

**Basics**

In [7]: from numpy.random import randn
In [8]: data = {i : randn() for i in range(7)}
In [9]: data
Out[9]: 
{0: -1.764851973005172,
 1: 0.3456085497539203,
 2: -0.07122651793900005,
 3: -1.7820285799128224,
 4: -1.522797097479855,
 5: 0.038755935366163285,
 6: 0.3251686627198628}
 
**Tab Completion**

One of the major improvements over the standard Python shell is tab completion.

- vars
- functions
- members (including private ones)
- file paths (could be combined with the %run command)

**Introspection**

- var? (obj intro)
- func?? (source code)
- np.*load*?

**%run**

- %run some_script.py
- %run -i some_script.py (including defined vars outside the file)

- <Ctrl-C> to stop

**%paste**

- %paste
- %cpaste

**Magic Commands**

A magic command is any command prefixed by the percent symbol %.

- %timeit np.dot(a, a)
- %reset
- %quickref
- %hist
- %who, %whos, %who_ls

**Qt-based Rich GUI Console**

ipython qtconsole --pylab=incline

-- matplotlib

ipython --pylab

**Input/Output vars**

- -(in) -- (out)
- _i27/_27

%logstart
%logstop

**OS**

!cmd
output = !cmd args
%alias alias_name cmd
%bookmark
%cd dir
%pwd
%pushd dir
%popd
%dirs
%dhist
%env

ex: !python
ip_info = !ifconfig en0 | grep "inet "

foo = 'log*'
!ls $foo

%bookmark gh /Users/andersc/github/
cd gh

list: %bookmark -l

**IPython HTML Notebook**

...

**Tips for productive coding**

- dreload: reloading modules
- keep relevant objects and data alive
- flat is better than nested
- overcome a fear of longer files

**Advanced Features**

- making your own classes IPython-friendly (__repr__)
- profiles and config sys




