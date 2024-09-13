#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun June 23 23:57:59 2024

@author: hetalprajapati
"""

import glassdoor_scraper as gs

results = gs.fetch_jobs('data analyst', 30, 'canada')
results
