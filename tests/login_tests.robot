*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/keywords/login_keywords.robot

*** Variables ***
${VALID_MOBILE}    09908917206
${VALID_Email}  erfanshafieeee@gmail.com
${CORRECT_PASSWORD}    Erf@n5183
${INCORRECT_PASSWORD}  Erfan123456



*** Test Cases ***
Successful Login With Mobile And Password
    [Tags]    Positive
    Open Digikala Login Page
    Login With Mobile And Password    ${VALID_MOBILE}    ${CORRECT_PASSWORD}
    Verify Successful Login
    Close Browser

Unsuccessful Login With Mobile And Password
    [Tags]    Negative
    Open Digikala Login Page
    Login With Mobile And Password    ${VALID_MOBILE}    ${INCORRECT_PASSWORD}
    Verify Unsuccessful Login
    Close Browser

Successful Login With Email And Password
    [Tags]    Positive
    Open Digikala Login Page
    Login With Mobile And Password    ${VALID_Email}    ${CORRECT_PASSWORD}
    Verify Successful Login
    Close Browser

Unsuccessful Login With Email And Password
    [Tags]    Negative
    Open Digikala Login Page
    Login With Mobile And Password    ${VALID_Email}    ${INCORRECT_PASSWORD}
    Verify Unsuccessful Login
    Close Browser

