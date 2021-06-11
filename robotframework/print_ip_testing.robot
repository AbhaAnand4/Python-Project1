*** Settings ***
Documentation     PrintIP test cases using the keyword-driven testing approach.
...
...               All tests contain a workflow constructed from keywords in
...               ``IpPrintLibrary.py``.
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Library           IpPrintLibrary.py

*** Test Cases ***
To print ip address of input1.json
    Print ip    ../examples/input1.json
    Result should be    0

To print ip address of input2.json
    Print ip    ../examples/input2.json
    Result should be    0

To print ip address if empty.json file is passed
    Print ip    ../examples/empty.json
    Result should be    1

To print ip address if invalid_json.json file is passed
    Print ip    ../examples/invalid_json.json
    Result should be    1

To print ip address if input.txt file is passed
    Print ip    ../examples/input.txt
    Result should be    1

To print ip address if filename not passed
    Print ip    fdfdf
    Result should be    1