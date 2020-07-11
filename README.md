# Credit Calculator
Entry level python assignment from JetBrains Academy. My execution of the stages can be found in this repository under the respective project files.

# Objectives per stage:


## Stage 1: 
**Create a simple program which will print messages about some credit.**

Let's start by imitating this behavior. There are some prepared variables in source code that are ready for use: these are text messages that our credit calculator could output. At this stage, all you need to do is output them in the right order.

### Output:


#### Example 1

```
Credit principal: 1000
Month 1: paid out 250
Month 2: paid out 250
Month 3: paid out 500
The credit has been repaid!
```

## Stage 2: 
**Communicate with the user to get necessary values, do simple mathematical operations and output the result.**

Prompt a user to enter their credit principal and choose one of the two parameters, i.e. the count of periods or the monthly payment.
To perform further calculations, you'll also have to ask for the lacking value.
Finally, inform the user of your results.

### Output:

#### Example 1
```
Enter the credit principal:
> 1000
What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment:
> m
Enter monthly payment:
> 150

It takes 7 months to repay the credit
```
#### Example 2
```
Enter the credit principal:
> 1000
What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment:
> m
Enter monthly payment:
> 1000

It takes 1 month to repay the credit
```
#### Example 3
```
Enter the credit principal:
> 1000
What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment:
> p
Enter count of months:
> 10
 
Your monthly payment = 100
```
#### Example 4
```
Enter the credit principal:
> 1000
What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment
> p
Enter count of months:
> 9
 
Your monthly payment = 112 with last month payment = 104.
```
## Stage 3: 
Let's compute all the parameters of the credit. There are at least two kinds of credit: those with annuity payment and with differentiated payment. At this stage, you're going to calculate only the annuity payment which is fixed during the whole credit term.

You are interested in four values: the count of periods to repay the credit, monthly payment, credit principal and credit interest. Each of these values can be calculated if others are known:

At this stage, you should add new behavior to the calculator:

First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the count of periods, monthly payment and credit principal.
Then you need to ask them to input the remaining values.
Finally, compute and output the value that they wanted.

## Stage 3:
**Calculate real credit parameters by using the mathematical capabilities of Python.**




## Stage 3:
**Make the credit calculator be able to work with different types of payment and to work with command-line arguments.**
