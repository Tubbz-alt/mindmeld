#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dialogue
----------------------------------

Tests for app_manager module.

These tests apply only when async/await are supported.
"""
import pytest


@pytest.mark.asyncio
async def test_parse(async_kwik_e_mart_app):
    response = await async_kwik_e_mart_app.app_manager.parse('hello')

    fields = {'domain', 'intent', 'entities', 'params', 'request', 'dialogue_state',
              'directives', 'history'}
    for field in fields:
        assert field in response
