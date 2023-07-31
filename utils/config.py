import configparser



def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    return config


def save_config(config):
    with open('config.ini', 'w', encoding='utf-8') as file:
        config.write(file)


def get_user():
    return {
        "username": get_config().get('user', 'username'),
        "password": get_config().get('user', 'password'),
    }


def get_settings_config():
    """
    获取配置文件'settings'部分的所有配置
    :return: list
    """
    return get_config().items('settings')


def is_save_cookies():
    return get_config().get('settings', 'save_cookies')


def get_error_retry():
    return int(get_config().get('settings', 'error_retry'))


def enable_log():
    return get_config().get('settings', 'enable_log') == "true"


def enable_log_level():
    return get_config().get('settings', 'enable_log_level').split(",")


def print_info_level():
    return get_config().get('settings', 'print_info_level') == "true"


def get_data_config():
    """
    获取配置文件'data'部分的所有配置
    :return: list
    """
    return get_config().items('data')


def get_log_folder():
    return get_config().get('data', 'log_folder')


def get_cookies_path():
    return get_config().get('data', 'cookies_path')


def get_description_path():
    return get_config().get('data', 'description_path')


def get_tasks_path():
    return get_config().get('data', 'tasks_path')
