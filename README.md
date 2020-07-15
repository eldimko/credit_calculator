# Credit Calculator
Entry level python assignment from JetBrains Academy. My execution of the stages can be found in this repository under the respective project files.
## About

Finance is an important part of the life of any people. Sometimes you think about getting additional income and want to open a deposit account. And sometimes you need additional money right now and want to take a credit or mortgage. Anyway, you may want to calculate different financial indicators to make a decision. Let’s make such an instrument that can help us.

## Learning Objectives

You’ll learn how to use mathematics and Python in everyday tasks, use third-party modules and libraries. Also, you’ll learn more about different financial instruments. Finally, you will make your own credit calculator!

# Objectives per stage:


## Stage 1: 
**Create a simple program which will print messages about some credit.**

Let's start by imitating this behavior. There are some prepared variables in source code that are ready for use: these are text messages that our credit calculator could output. At this stage, all you need to do is output them in the right order.


## Stage 2: 
**Communicate with the user to get necessary values, do simple mathematical operations and output the result.**

Prompt a user to enter their credit principal and choose one of the two parameters, i.e. the count of periods or the monthly payment.
To perform further calculations, you'll also have to ask for the lacking value.
Finally, inform the user of your results.


## Stage 3: 
**Calculate real credit parameters by using the mathematical capabilities of Python.**

At this stage, you should add new behavior to the calculator:

First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the count of periods, monthly payment and credit principal.
Then you need to ask them to input the remaining values.
Finally, compute and output the value that they wanted.



## Stage 4:
**Make the credit calculator be able to work with different types of payment and to work with command-line arguments.**
At this stage, it is required to implement these features:

1. the calculation of differentiated payment. To do this, the user may run the program specifying interest, count of periods and credit principal.


2. a capacity to calculate the same values as in the previous stage for annuity payment (principal, count of periods and value of the payment). A user specifies all known parameters with command-line arguments, while a single parameter will be unknown. This is the value the user wants to calculate.

3. handling of invalid parameters. It's a good idea to show an error message Incorrect parameters in case of invalid parameters (they are discussed in detail below).

The final version of your program is supposed to work from the command line and parse the following parameters:
`--type`, `--payment`, `--principal`, `--periods`, `--interest`

# References

JetBrains Academy: https://hyperskill.org/

Credit Calculator project page: https://hyperskill.org/projects/90?track=2
