#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import javabridge

PATH = os.path.abspath(os.path.dirname(__file__))

THOUGTHLAND_JAR = os.path.join(
    PATH, "jars", "thoughtland-0.0.1-SNAPSHOT-jar-with-dependencies.jar"
)


class Thoughland(object):

    def __init__(self, thoughtland_jar=None, *args, **kwargs):

        kwargs.setdefault("class_path", []).append(
            thoughtland_jar or THOUGTHLAND_JAR
        )
        kwargs.setdefault("run_headless", True)
        import ipdb; ipdb.set_trace()
        javabridge.start_vm(*args, **kwargs)




