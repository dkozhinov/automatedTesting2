from selenium import webdriver


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    print("Before scenario ", scenario, "\n")


def after_scenario(context, scenario):
    print("scenario status" + scenario.status)
    context.browser.quit()
    print("After scenario ", scenario, "\n")


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_all(context):
    context.config.setup_logging()
