import os
import sys
import site
import gettext
import logging

########################################################################################################################
#                                                    Some helpers                                                      #
########################################################################################################################


def set_config(config_name):
    """

    Config parse

    :param config_name: config file name
    :type config_name: str
    :return: parsed config
    :rtype: dict

    """
    import json
    try:
        return json.load(open(config_name, 'r'))
    except FileNotFoundError:
        print('%s %s' % (config_name, 'not found'))
        exit(1)
    except json.JSONDecodeError as error:
        print('%s %s: %s' % (config_name, 'format error', str(error)))
        exit(1)

# ----------------------------------------------------------------------------------------------------------------------


def activate_virtual_environment(**kwargs):
    """

    Activate virtual environment

    :param kwargs: key parameters

    Allowed following parameters:

    - environment (virtual environment directory, default: 'venv')
    - packages (path to packages in environment, default: 'lib/python3.5/site-packages')

    """
    env = kwargs.get('environment', 'venv')
    env_path = env if env[0:1] == "/" else os.getcwd() + "/" + env
    env_activation = env_path + '/' + 'bin/activate_this.py'
    site.addsitedir(env_path + '/' + kwargs.get('packages', 'lib/python3.5/site-packages'))
    sys.path.append('/'.join(env_path.split('/')[:-1]))
    try:
        exec(open(env_activation).read())
    except Exception as e:
        print('%s: (%s)' % ('virtual environment activation error', str(e)))
        exit(1)

# ----------------------------------------------------------------------------------------------------------------------


def set_localization(**kwargs):
    """

    Install localization

    :param kwargs: key parameters

    Allowed following parameters:

    - locale_domain (default: sys.argv[0])
    - locale path (default: '/usr/share/locale')
    - language (default: 'en')
    - quiet (default: False)

    """
    locale_domain = kwargs.get('locale_domain', sys.argv[0])
    locale_dir = kwargs.get('locale_dir', '/usr/share/locale')
    language = kwargs.get('language', 'en')
    gettext.install(locale_domain, locale_dir)
    try:
        gettext.translation(locale_domain, localedir=locale_dir, languages=[language]).install()
    except FileNotFoundError:
        if not kwargs.get('quiet', False):
            print('%s %s \'%s\' %s, %s' % ('translation', 'for', language, 'not found', 'use default'))

# ----------------------------------------------------------------------------------------------------------------------


def get_logger(logger_name, logging_format, file_name):
    """

    Get logger with path 'file name'. If permission error, create log in /tmp

    :param logger_name: logger name
    :type logger_name: str
    :param logging_format: log format
    :type logging_format: str
    :param file_name: log file name
    :type file_name: str
    :return: logger
    :rtype: logging.Logger

    """
    path, prepared = '', True
    for cat in file_name.split('/')[1:-1]:
        path += '/%s' % cat
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except PermissionError:
                prepared = False
                break
    if not prepared:
        file_name = '/tmp/%s' % file_name.split('/')[-1]
    logging.basicConfig(level=logging.INFO, format=logging_format)
    log = logging.getLogger(logger_name)
    handler = logging.FileHandler(file_name, encoding='utf8')
    handler.setFormatter(logging.Formatter(logging_format))
    log.addHandler(handler)
    log.setLevel(level=logging.INFO)
    return log
