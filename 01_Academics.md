# Markdown Tricks

Markdown here works mostly like traditional Markdown in [Jupyter Markdown](https://jupyternotebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html) or [RStudio Markdown](https://rmarkdown.rstudio.com/index.html)

This presumes that the user understands how to use topic headers, include images, links, and can __bold__, _italicize_, ___etc___ for text.  If not there are examples of these features in the raw markdown on this and other pages in larger template package.

## Markdown Headers to Make a Table of Contents

Markdown pages will be "titled" on the sidebar with a single "#" header and do not have the share the same name as the Markdown ".md" file.  Higher-level headers (##, ###, etc) will be then listed in dropdowns on the sidebar menu.

## Equations

Equations follow the LaTeX Markdown format.

As with Jupyter and RStudio, you can use a pair of $'s to wrap your equations.

$$\pi=\int_0^1{ \frac{4}{1+x^2}}dx$$

The [Codecogs's LaTeX Equation Editor](https://latex.codecogs.com/eqneditor/editor.php) is a useful tool to graphically construct the markdown code for most equations, as well as learn the basics of LaTeX equations so you can encopde simple equations on your own.

## "Admonitions" & "Toasts"

Not the same as code blocks, these four types of blocks highlight pointers and alarms of various degrees of importance.  

```tip
Protip: There are no wrong answers, just really bad right ones.
```

```note
Just saying: Markdown in Github could benefit from a spell checker.
```

```warning
This is not guidance: Pennies are not fuses on a budget
```

```danger
Kids Dom't try this at home: Try it at your *friends* house!
```



