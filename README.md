## Exercise 1

Write a program using python3 called ip_print to print out IP addresses.
The program takes a single command line argument, FILENAME which is the name of
the file containing some JSON data that contains the IP addresses.

Your program must print out the IP addresses, which are the values of
all of the keys inside the "value" object one per line. If the file also contains
a "network" object, then you should also print out a second IP address on the same line
that corresponds to the same "name".

Two example files are given called input1.json and input2.json.
The expected outputs are:

> \$ ip_print input1.json
> 192.168.101.101
> 192.168.101.70
> 192.168.101.153

> \$ ip_print input2.json
> 192.168.102.33 10.0.0.87
> 192.168.103.74 10.0.0.77
> 192.168.102.155 10.0.0.99

## Solution: How to printip program:

virtualenv venv
. venv/bin/activate
pip install -e .

> Then run:
> ip_print examples/input1.json
> ip_print examples/input2.json

## Exercise 2:

Write tests using Robot framework to test ip_print. It should test running it against input1.json, input2.json as well as error cases.

## Solution: How to test printip program using robot framework
Prerequisite: Install robotframework

> cd robotframework
> source ./robottest.sh

> > Notes: Test result would be generated in TestResult folder

## Exercise 3:

Write a Jenkins declarative pipeline that contains two stages called input1 and input2.
Each stage should run ip_print with the example file corresponding to the stages' name.

The pipeline should check out the program and the input files out of a git repository.
You do not need to provide access to a real git repository.

## Solution: J
Added Jenkins declarative pipeline file named "Jenkinsfile"
