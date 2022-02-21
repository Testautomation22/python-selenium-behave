
Feature:Testing Product pages functionality

Background: Common step
  Given Launch Gettop app

  Scenario: User can open and close Quick View by clicking on closing X
    When Hover on product
    And Click "QUICK VIEW"
    And "QUICK VIEW" opens
    Then Click X to close

 Scenario: User can click Quick View and add product to cart
   When Hover on product
   And Click "QUICK VIEW"
   And "QUICK VIEW" opens
   Then Add product to cart

 Scenario: User can click through multiple product pages by clicking 1, 2 for page number
   Then Click 1, 2

 Scenario: User can click through multiple product pages by clicking > and <
   Then Click > and <

