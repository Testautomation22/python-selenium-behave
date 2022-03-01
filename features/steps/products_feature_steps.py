from behave import given, then, when
import time


@given(u'Launch Gettop app')
def step_impl(context):
    context.app.home.open()
    time.sleep(4)


@when(u'Hover on product')
def step_impl(context):
    context.app.hover_iphone.hover_iphone_se()
    time.sleep(4)


@when(u'Click "QUICK VIEW"')
def step_impl(context):
    context.app.quick_view.click_quick_view()


@when(u'"QUICK VIEW" opens')
def step_impl(context):
    time.sleep(4)
    context.app.verify_prod.verify_prod_results('iPhone SE')


@then(u'Click X to close')
def step_impl(context):
    context.app.click_close.close_quick_view()


@then(u'Add product to cart')
def step_impl(context):
    context.app.top_nav.add_to_cart()


@then(u'Click 1, 2')
def step_impl(context):
    context.app.dots.click_page_dots()


@then(u'Click > and <')
def step_impl(context):
    context.app.arrows.click_arrows()


