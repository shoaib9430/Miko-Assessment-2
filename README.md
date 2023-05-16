# Miko-Assessment-2

# Junior Developer Assignment (R1):
Create a simple assembly Language which will have 3 operations,
Get a constant into a register of the form
MV REG1,#2000
MV REG2,#4000
Add two registers together. Save results in the first register
ADD REG1, REG2
Add register and constant together. Save results in the first register.
ADD REG1,600
Show the results of a register
SHOW REG
The simple java or python program should be able to accept a program containing one or more
MV statements and an ADD statement and print the results of a SHOW REG at the end.
Write java/python code which will parse the SQL statements and either create files or insert into
files.

# Here's an example assembly language program that meets the requirements:
MV REG1, #2000   ; load 2000 into register 1
MV REG2, #4000   ; load 4000 into register 2
ADD REG1, REG2   ; add register 2 to register 1 and store result in register 1
ADD REG1, 600    ; add 600 to register 1 and store result in register 1
SHOW REG1        ; print the value of register 1
