#!/usr/bin/env python
# coding: utf-8

# ![HPC Masthead](https://kyrill.ias.sdsmt.edu/wjc/eduresources/AES_519_Masthead.png)
# # Comparing Future Climate Scenarios (Python Edition)
# 
# ## License
# 
# <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://wjcapehart.github.io/Capehart_Research_Page/Python/Welchs_t_Test_Python_Function_Capehart.html">Welchs_t_Test(): A basic Welch's t-Test Utility Function including textual and graphical output</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://wjcapehart.github.io/Capehart_Research_Page/">William J Capehart</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
# 

# 
# 
# ## Libraries
# 
# Let's start with our analog for R to do this task.
# 
# * [numpy](https://numpy.org/doc/stable/reference/generated/numpy.nansum.html): The Go-To Python Library for Arrays and Basic Math Operation
# * [scipy](https://docs.scipy.org/doc/scipy/index.html): An open-source software for mathematics, science, and engineering
# * [matplotlib](https://matplotlib.org/): The standard library for basic plotting in Python
# * [seaborn](https://seaborn.pydata.org/index.html): An extention for Matplotlib that leverages Pandas (but you can use it with other datamodels).
# 

# ---
# ## Welch's t-Test Function Declaration

# In[1]:


#########################################
#
# Welch's t-Test Text and Graphics Function
#

def Welchs_t_Test(x1 =        None,
                  x2 =        None,
                test = "two-sided",
       variable_name =          "",
             x1_name =        "x₁",
             x2_name =        "x₂",
               alpha =        0.05):
    """
    Applies a Welch's t-Test to two samples with tablular and graphical output

    Author: WJ Capehart, South Dakota Mines.

    Licensing: Creative Commons BY-NC-SA version 4.0
       (https://creativecommons.org/licenses/by-nc-sa/4.0/)

    Citation: 

    "Welchs_t_Test(): A basic Welch's t-Test Utility Function 
        including textual and graphical output" by William J Capehart 
        is licensed under Creative Commons Attribution-NonCommercial-
        ShareAlike 4.0 


    Args:
        x1 (array): Experimental Sample
        x2 (array): Control Sample
        test (string): t-test: ["two-sided","greater","less"]
        variable_name (string): User Text Name for Variable
        x1_name (string): Experimental Sample Name
        x2_name (string): Control Sample Name
        alpha (float): Experimental Sample

    Returns:
        t_stat (float): Calculated t-statistic 
        p (float): p-value
        df (int): degrees of freedom
        Verdict (string): Hypothesis Result
    """



    #
    # Libraries
    #

    import numpy             as np
    import matplotlib.pyplot as plt
    import seaborn           as sns    
    import scipy.stats       as stats



    #
    # Test Language for Output
    #

    if (test == "greater"):
        Ho_sym, Ha_sym = ["≤", ">"]
        x1_fill        = "magenta"
        x2_fill        = "cyan"
        x1_line        = "darkred"
        x2_line        = "darkblue"
        t_color        = "blue"
    elif (test == "less"):
        Ho_sym, Ha_sym = ["≥", "<"]   
        x1_fill        = "cyan"
        x2_fill        = "magenta"
        x1_line        = "darkblue"
        x2_line        = "darkred"
        t_color        = "blue"
    else:
        Ho_sym, Ha_sym = ["=", "≠"] 
        x1_fill        = "cyan"
        x2_fill        = "grey"
        x1_line        = "darkblue"
        x2_line        = "black"
        t_color        = "green"

    Ho_Text = x1_name + " " + Ho_sym + " " + x2_name
    Ha_Text = x1_name + " " + Ha_sym + " " + x2_name

    #
    # Run T-Test
    #

    t_test_out = \
         stats.ttest_ind(a           =    x1,
                         b           =    x2,
                         alternative =  test,
                         equal_var   = False)
    #
    # Output from T-Test
    #

    t_stat   = t_test_out.statistic
    p        = t_test_out.pvalue
    df       = t_test_out.df

    P_t_stat = stats.t.cdf(x  = t_stat,
                           df =     df)

    #
    # Get Crit T-Thresholds, and calculated p vals s (<, >, two-tail)
    #

    if (test == "greater"):
        t_threshold = stats.t.ppf(q  =   1 - alpha,
                                  df =          df)
        p_calc      = 1-P_t_stat
        alpha_tail  = "{:02}".format(1-alpha)
    elif (test == "less"):
        t_threshold = stats.t.ppf(q  =       alpha,
                                  df =          df)  
        p_calc      = P_t_stat
        alpha_tail  = "{:02}".format(1-alpha)
    else:
        t_threshold = stats.t.ppf(q  = 1 - alpha/2,
                                  df =          df) 
        p_calc      = 2*(1-P_t_stat)
        alpha_high  = "{:03}".format(1-alpha/2)
        alpha_low   = "{:03}".format(alpha/2)

    #
    # Verdict of t-Test given alpha
    #

    if (p > alpha):
        Verdict = "Ho cannot be rejected; " + Ho_Text
    else:
        Verdict = "Ho is rejected; " + Ha_Text


    #
    # Welch's T Test Report
    #

    print("")
    print("╔═══════════════════════════════════════════════════")
    print("║╭──────────────────────────────────────────────")
    print("║│  Welch's t-Test Report (ɑ="+str(alpha)+")")
    if (variable_name != ""):
        print("║│ Variable :", variable_name )
    print("║│       Ho :", Ho_Text)
    print("║│       Ha :", Ha_Text)
    print("║│        t :", t_stat)
    if (test != "two-sided"):
        print("║│   t₍₁₋ₐ₎ :", t_threshold)
    else:
        print("║│  t₍₁₋½ₐ₎ :", t_threshold)
    print("║│        p :", p,p_calc )
    print("║│   Result :", Verdict  ) 
    print("║╰──────────────────────────────────────────────")

    #
    # Calucate p(t) for Graphics
    #

    p_t_stat = stats.t.pdf(x  = t_stat,
                           df =     df)


    #
    # X-Axis for T-Values for Plots
    #

    t_plotedge  = stats.t.ppf(q  = 0.99999,
                              df =      df)

    t_plotedge_max = np.max([t_plotedge,
                                 t_stat])

    t_plotedge_min = np.min([-t_plotedge,
                                  t_stat])

    t_axis_plot_range = np.linspace(start =  t_plotedge_min,
                                     stop =  t_plotedge_max,
                                     num  =            1000)

    #
    # Plot T-Curve
    #

    sns.set_theme(style = "ticks", 
          rc    = {"axes.spines.right":False, 
                     "axes.spines.top":False})

    fig, [ax1, ax2] = plt.subplots(nrows = 1,
                                   ncols = 2,
                                   figsize = [8,3])

    if (variable_name != ""):
        fig.suptitle("Welch's t-Test : "+ variable_name,fontsize="small")
    else:
        fig.suptitle("Welch's t-Test",fontsize="small")


    #
    # Plot x1 and x2
    #

    sns.kdeplot(x1, 
                color       = x1_fill, 
                ax          =     ax1,
                fill        =    True,
                alpha       =  0.3333,
                common_norm =   False)
    sns.kdeplot(x2, 
                color       = x2_fill, 
                ax          =     ax1,
                fill        =    True,
                alpha       =  0.3333,
                common_norm =   False)
    ax1.legend([x1_name,x2_name],
                framealpha = 0,      # makes legend transparent
                fontsize = "xx-small") 
    sns.kdeplot(x1, 
                color       = x1_line, 
                ax          =     ax1,
                fill        =   False,
                common_norm =   False)   
    sns.kdeplot(x2, 
                color       = x2_line, 
                ax          =     ax1,
                fill        =   False,
                common_norm =   False)
    ax1.set_xlabel(variable_name, fontsize="x-small")
    ax2.set_ylabel(r"$p(x)$", fontsize="x-small")
    ax1.set_title("Probability Distributions", fontsize="x-small")   

    #
    # Plot t-Distribution
    #

    if (p > alpha):
        ax2.set_title(r"$H_0$: " + Ho_Text, fontsize="x-small")
    else:
        ax2.set_title(r"$H_a$: " + Ha_Text, fontsize="x-small")


    ax2.plot(t_axis_plot_range, 
             stats.t.pdf(x  = t_axis_plot_range,
                         df = df), 
             color = "grey",
             label = r"$p(t)$")

    if (test == "greater"):
        t_axis_greater = np.linspace(start = t_plotedge_min,
                                      stop =    t_threshold,
                                       num =           1000)
        ax2.fill_between(t_axis_greater, 
                         stats.t.pdf(x  = t_axis_greater,
                                     df = df), 
                         color = t_color,
                         alpha = 0.33333,
                         label = r"$P(t)$ = "+alpha_tail)

    elif (test == "less"):
        t_axis_less = np.linspace(start =    t_threshold,
                                   stop = t_plotedge_max,
                                    num =           1000)
        ax2.fill_between(t_axis_less, 
                         stats.t.pdf(x  = t_axis_less,
                                     df = df), 
                         alpha = 0.33333,
                         color = t_color,
                         label = r"1-$P(t)$ = "+alpha_tail)

    else:
        t_axis_2tail = np.linspace(start = -t_threshold,
                                    stop =  t_threshold,
                                     num =         1000)
        ax2.fill_between(t_axis_2tail, 
                         stats.t.pdf(x  = t_axis_2tail,
                                     df = df), 
                         alpha = 0.33333,
                         color = t_color,
                         label = alpha_low+" > P(t) > "+alpha_high)

    ax2.plot([t_stat,   t_stat],
             [    -1, p_t_stat],
             marker    = "o",
             color     = "red",
             label     = r"Welch's $t$ value",
             linestyle = "dotted")

    ax2.legend(framealpha = 0,      # makes legend transparent
                 fontsize = "xx-small") 

    ax2.set_ylim(bottom = 0)
    ax2.set_xlabel(r"$t$",    fontsize="x-small")
    ax2.set_ylabel(r"$p(t)$", fontsize="x-small")


    ax1.tick_params(labelsize = "x-small")
    ax2.tick_params(labelsize = "x-small")


    plt.tight_layout
    plt.show()

    print("╚═══════════════════════════════════════════════════")
    print("")

    return {"t": t_stat,
            "p": p,
           "df": df,
       "Result": Verdict}
#
#########################################


# ---
# ## Testing Example
# 
# This test leverages a dataset compiled by
# 
# > De Vito, S., E. Massera, M. Piga, L. Martinotto, G. Di Francia, 2008: On  field calibration of an electronic nose for benzene estimation in an urban pollution monitoring scenario, *Sensors and Actuators B: Chemical*, **129** (2), 750-757, [doi: 10.1016/j.snb.2007.09.060](https://www.sciencedirect.com/science/article/abs/pii/S0925400507007691).
# 
# The dataset is maintained by the Univ of California at Irvine, Machine Learning Repository ([doi: 10.24432/C59K5F](https://doi.org/10.24432/C59K5F))
# 
# Here, the data is extracted for two Benzine samples (a training sample with 70 samples and a testing sample of 30 samples) at 0700 UTC between 2004-March-11 and 2005-April-04.
# 
# ### Support Libraries for Demonstration
# 
# * [numpy](https://numpy.org/doc/stable/reference/generated/numpy.nansum.html): The Go-To Python Library for Arrays and Basic Math Operation
# * [pandas](https://pandas.pydata.org/docs/): Our Go-To Library for Tabular Data.

# In[2]:


#########################################
#
# Demonstration Libraries
#

import pandas as pd

#
#########################################


# In[3]:


#########################################
#
# Demonstration Libraries
#

url_xlsx = "http://kyrill.ias.sdsmt.edu:8080/thredds/fileServer/CLASS_Examples/CEE_284_Area/Statistics/Air_Quality_Extraction_H0700.xlsx"

training = pd.read_excel(io         = url_xlsx,
                         sheet_name = "Training").  \
              set_index("Time")

testing  = pd.read_excel(io         = url_xlsx,
                         sheet_name = "Testing").  \
              set_index("Time")

display(training)
display(testing)
#
#########################################


# ## Executing the Function
# 
# Here we will demonstrate all three basic statistical tests, challenging the Testing sample against the Training sample.

# In[4]:


#########################################
#
# Demonstration of Function
#

#
# Two-Tail Function Output
#

T_test_Ha_Testing_ne_Training = \
    Welchs_t_Test(x1 =         testing["C6H6 (μg/m³)"],
                  x2 =        training["C6H6 (μg/m³)"],
                test =                     "two-sided",
       variable_name = "Benzine Concentration [μg/m³]",
             x1_name =                       "Testing",
             x2_name =                      "Training",
               alpha =                            0.05)

print("Two-Tail Function Output")
display(T_test_Ha_Testing_ne_Training)
print("")
print("")

#
# Right-Tail Function Output
#

T_test_Ha_Testing_gt_Training = \
    Welchs_t_Test(x1 =         testing["C6H6 (μg/m³)"],
                  x2 =        training["C6H6 (μg/m³)"],
                test =                       "greater",
       variable_name = "Benzine Concentration [μg/m³]",
             x1_name =                       "Testing",
             x2_name =                      "Training",
               alpha =                            0.05)

print("Right-Tail Function Output")
display(T_test_Ha_Testing_gt_Training)
print("")
print("")

#
# Left-Tail Function Output
#

T_test_Ha_Testing_lt_Training = \
    Welchs_t_Test(x1 =         testing["C6H6 (μg/m³)"],
                  x2 =        training["C6H6 (μg/m³)"],
                test =                          "less",
       variable_name = "Benzine Concentration [μg/m³]",
             x1_name =                       "Testing",
             x2_name =                      "Training",
               alpha =                            0.05)

print("Left-Tail Function Output")
display(T_test_Ha_Testing_lt_Training)
print("")
print("")

#
#########################################


# ---
# ## Version Information
# 
# * [version_information](https://github.com/jrjohansson/version_information): Robert Johansson's Version Information Utility
#   

# In[5]:


#########################################
#
# Version Information Utility
#

get_ipython().run_line_magic('load_ext', 'version_information')

get_ipython().run_line_magic('version_information', 'numpy, scipy, matplotlib, pandas, version_information')

#
#########################################

