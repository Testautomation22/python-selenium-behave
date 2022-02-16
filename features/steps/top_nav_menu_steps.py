from behave import given, when, then


@given(u'User open gettop homepage')
def step_impl(context):
    context.app.home.open()


@when(u'User clicks cart icon')
def step_impl(context):
    context.app.top_nav.click_cart_icon()


@when(u'User hovers over empty cart icon')
def step_impl(context):
    context.app.top_nav.hover_cart_icon()


@when(u'Hover on MAC option in the top nav menu')
def step_impl(context):
    context.app.top_nav.hover_category()


@when(u'Clicks on MacBook Air')
def step_impl(context):
    context.app.top_nav.click_product()


@when(u'Click ADD TO CART button')
def step_impl(context):
    context.app.top_nav.add_to_cart()


@when(u'User hovers over cart icon')
def step_impl(context):
    context.app.top_nav.hover_cart_icon()


@when(u'click "View Cart"')
def step_impl(context):
    context.app.click_view.click_view_cart_button()


@when(u'click "Checkout"')
def step_impl(context):
    context.app.checkout_button.click_checkout_button()


@when(u'click "x" button')
def step_impl(context):
    context.app.remove.click_remove_button()


@then(u'Verify price is correct')
def step_impl(context):
    context.app.subtotal.verify_subtotal('$999.00')


@then(u'Verify items amount is correct')
def step_impl(context):
    context.app.items_amount.verify_items_amount('1')


@then(u'verify correct products and subtotal shown')
def step_impl(context):
    context.app.products.verify_product('Subtotal $999.00')


@then(u'verify user can click on "View Cart" and is taken to cart page')
def step_impl(context):
    context.app.verify_shopping_cart.verify_shopping_cart_page('SHOPPING CART')


@then(u'verify user can click on "Checkout" and is taken to checkout page')
def step_impl(context):
    context.app.verify_checkout.verify_checkout_page('CHECKOUT DETAILS')


@then(u'verify user can remove a product')
def step_impl(context):
    context.app.empty_cart_results.verify_cart_empty('No products in the cart.')


@then(u'Empty Cart page {opens}')
def step_impl(context, opens):
    context.app.empty_cart_results.verify_results('Your cart is currently empty.')


@then(u"'No products in the cart.' {message} is shown")
def step_impl(context, message):
    context.app.empty_cart_results.verify_hover_results('No products in the cart.')