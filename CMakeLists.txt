# Copyright © 2016-2022. Savenkov Igor
# SPDX-License-Identifier: GPL-3.0-or-later

cmake_minimum_required (VERSION 3.22.0)

project (conan_test)

find_package (fmt REQUIRED)
find_package (Qt6 COMPONENTS Core REQUIRED)

add_executable (conan_test src/main.cpp)
target_link_libraries (conan_test PUBLIC fmt::fmt)
target_link_libraries (conan_test PUBLIC Qt6::Core)
