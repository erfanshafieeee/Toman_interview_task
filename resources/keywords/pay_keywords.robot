*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Digikala Login Page
    Open Browser    https://www.digikala.com/users/login/    Chrome
    Maximize Browser Window
    Wait Until Page Contains Element    css:input[name="username"]    timeout=10s




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


Open sample product page
    [Arguments]    ${product_id}
    Go To    https://www.digikala.com/product/${product_id}

*** Keywords ***
Add Product To Cart
    Click Button   xpath=//button[@data-cro-id='pdp-add-to-cart']

Open Cart
    Go To    https://www.digikala.com/checkout/cart/

Continue shopping
    Click Element    xpath=//a[@data-cro-id='cart-continue-shopping']

Select Shipping Deliver Today
    Execute JavaScript    document.querySelector('[data-cro-id="shipping-deliver_today"]').click()

Ordering Continue
    Click Button   xpath=//button[@data-cro-id='shipping-continue']
          

Close Browser
    Close All Browsers
