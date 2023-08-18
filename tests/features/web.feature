Feature: Login and add items to cart on SauceDemo


  Scenario Outline: Login with credential
    Given User is on the SauceDemo login page
    When I enter "<username>" in user field "<password>" in password field and click login
    And User adds an item to the cart
    Then The item is added to the cart successfully
    Examples:
    | username | password     |
    | standard_user    | secret_sauce     |
