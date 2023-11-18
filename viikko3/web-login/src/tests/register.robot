*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    RSet Username  kalle
    RSet Password  kalle123
    RSubmit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    RSet Username  ka
    RSet Password  kalle123
    RSubmit Credentials
    Register Should Fail With Message  Invalid username or password

Register With Valid Username And Invalid Password
    # salasana ei sisällä halutunlaisia merkkejä
    RSet Username  kalle
    RSet Password  kalle
    RSubmit Credentials
    Register Should Fail With Message  Invalid username or password

Register With Nonmatching Password And Password Confirmation
    RSet Username  kalle
    RSet Password  kalle456
    RSubmit Credentials
    Register Should Fail With Message  Password does not match



Login With Nonexistent Username
    Create User  Nonexistent  kalle123
    Go To Register Page
    Register Page Should Be Open

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Login After Successful Registration
    RSet Username  kalle
    RSet Password  kalle456
    RSet Passwordc  kalle456
    RSubmit Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle456
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    RSet Username  kalle
    RSet Password  kalle123
    RSet Passwordc  kalle456
    RSubmit Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Register Should Succeed
    Register Page Should Be Open
    
Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

RSubmit Credentials
    Click Button  Register


RSet Username
    [Arguments]  ${username}
    Input Text  username  ${username}

RSet Password
    [Arguments]  ${password}
    Input Password  password  ${password}

RSet Passwordc
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
