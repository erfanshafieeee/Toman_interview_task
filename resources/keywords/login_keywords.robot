*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Digikala Login Page
    Open Browser    https://www.digikala.com/users/login/    Chrome
    Maximize Browser Window
    Wait Until Page Contains Element    css:input[name="username"]    timeout=10s

Verify Successful Login
    ${current_url}=    Get Location
    Should Be Equal    ${current_url}    https://www.digikala.com/

Verify Unsuccessful Login
    ${current_url}=    Get Location
    Should Not Be Equal    ${current_url}    https://www.digikala.com/



Login With Mobile And Password
    [Arguments]    ${mobile}    ${password}
    Input Text    css:input[name="username"]    ${mobile}
    Click Element    xpath=/html/body/div/main/div[2]/div[2]/form/button
    Wait Until Page Contains Element  xpath=/html/body/div/main/div[2]/div[2]/button[1]
    Click Element    xpath=/html/body/div/main/div[2]/div[2]/button[1]
    Wait Until Page Contains Element    css:input[name="password"]    timeout=10s
    Input Text    css:input[name="password"]    ${password}
    Click Button    css:button[type="submit"]
    Sleep    5


Login With Email And Password
    [Arguments]    ${mobile}    ${password}
    Input Text    css:input[name="username"]    ${mobile}
    Click Element    xpath=/html/body/div/main/div[2]/div[2]/form/button
    Wait Until Page Contains Element    css:input[name="password"]    timeout=10s
    Input Text    css:input[name="password"]    ${password}
    Click Button  xpath=/html/body/div/main/div[2]/div[2]/button[2]
    Sleep    5

Close Browser
    Close All Browsers
