*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/keywords/pay_keywords.robot

*** Variables ***
${VALID_MOBILE}    09908917206
${VALID_Email}  erfanshafieeee@gmail.com
${CORRECT_PASSWORD}    Erf@n5183
${INCORRECT_PASSWORD}  Erfan123456
${PRODUCT_ID}   dkp-20261601/گوشی-موبایل-اپل-مدل-iphone-16-ch-دو-سیم-کارت-ظرفیت-128-گیگابایت-و-رم-8-گیگابایت-اکتیو/



*** Test Cases ***
Successful pay product
    [Tags]   Positive
    Open Digikala Login Page
    Login With Mobile And Password    ${VALID_MOBILE}    ${CORRECT_PASSWORD}
    Open sample product page    ${PRODUCT_ID}
    Sleep    10
    Add Product To Cart
    Sleep    5
    Open Cart
    Sleep    10
    Continue shopping
    Sleep    10
    Select Shipping Deliver Today
    Sleep    2
    Ordering Continue
    Close Browser



