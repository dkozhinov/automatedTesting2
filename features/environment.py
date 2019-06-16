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
    print("After scenario ", scenario, "\n")
    print("scenario status" + context.scenario.steps[0].name)
    context.browser.quit()


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_all(context):
    context.config.setup_logging()
