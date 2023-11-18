*** Settings ***
Resource  resource.robot
#Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input New Command
    Input Credentials  kalle  kalle1234
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be longer than 3 letters

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  kalle!  kalle123
    Output Should Contain  Username must contain only letters between a to z

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  kalle  kalle
    Output Should Contain  Password must be longer than 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password cannot consist only of letters