
Feature: Gettop Cart Functionality

Background: Common step
  Given User open gettop homepage

  Scenario: Clicking on Cart icon
    When User clicks cart icon
    Then Empty Cart page opens


  Scenario: Hovering over empty cart icon
    When User hovers over empty cart icon
    Then 'No products in the cart.' message is shown

  Scenario:Verify price in the top Nav menu
    When Hover on MAC option in the top nav menu
    And Clicks on MacBook Air
    And Click ADD TO CART button
    Then Verify price is correct

    Scenario: Verify amount of items in top nav menu
      When Hover on MAC option in the top nav menu
      And Clicks on MacBook Air
      And Click ADD TO CART button
      Then Verify items amount is correct

    Scenario: verify correct products and subtotal shown
      When Hover on MAC option in the top nav menu
      And Clicks on MacBook Air
      And Click ADD TO CART button
      And User clicks cart icon
      Then verify correct products and subtotal shown


    Scenario: verify user can click on "View Cart" and is taken to cart page
      When Hover on MAC option in the top nav menu
      And Clicks on MacBook Air
      And Click ADD TO CART button
      And User hovers over cart icon
      And click "View Cart"
      Then verify user can click on "View Cart" and is taken to cart page

    Scenario: verify user can click on "Checkout" and is taken to checkout page
      When Hover on MAC option in the top nav menu
      And Clicks on MacBook Air
      And Click ADD TO CART button
      And User hovers over cart icon
      And click "Checkout"
      Then verify user can click on "Checkout" and is taken to checkout page


    Scenario: verify user can remove a product
      When Hover on MAC option in the top nav menu
      And Clicks on MacBook Air
      And Click ADD TO CART button
      And User hovers over cart icon
      And click "x" button
      And User hovers over cart icon
      Then verify user can remove a product
