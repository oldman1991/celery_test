#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/1/5
# coding=utf-8
import os

LOG_DIR = '/data/log/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'profile': {
            'format': '%(asctime)s %(message)s'
        },
        'consumer': {
            'format': '%(asctime)s %(levelname)s Process ID:%(process)d %(module)s.%(funcName)s Line:%(lineno)d %(message)s'
        },
        'raw': {
            'format': '%(message)s'
        },
    },

    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'default.log'),
            'formatter': 'verbose',
        },
        'info_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'info.log'),
            'formatter': 'verbose',
        },
        'error_handler': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'verbose',
        },
        'profile_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'profile.log'),
            'formatter': 'profile',
        },

        'exception_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'exception.log'),
            'formatter': 'verbose',
        },
        'alidayu_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'alidayu.log'),
            'formatter': 'profile',
        },
        'tracer_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'tracer.log'),
            'formatter': 'raw',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['default'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['error_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'info_logger': {
            'handlers': ['info_handler', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'error_logger': {
            'handlers': ['error_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'profile_logger': {
            'handlers': ['profile_handler'],
            'level': 'INFO',
            'propagate': False,
        },

        'exception_logger': {
            'handlers': ['exception_handler'],
            'level': 'ERROR',
            'propagate': False,
        },

        'alidayu_logger': {
            'handlers': ['alidayu_handler'],
            'level': 'INFO',
            'propagate': False,
        },

        'gm_tracer.subscribe': {
            'handlers': ['tracer_handler'],
            'propagate': False,
            'level': 'INFO'
        },

    }
}

