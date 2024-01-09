#!/bin/bash

# 1. Retrieve author information from Git history:
git log --format='%aN <%aE>' | sort -u > AUTHORS