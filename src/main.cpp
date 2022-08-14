// Copyright © 2016-2022. Savenkov Igor
// SPDX-License-Identifier: GPL-3.0-or-later

#include <iostream>

#include <QtCore/QString>

#include <fmt/core.h>

int main(int argc, char* argv[])
{
    auto qt_string = QString("Qt");
    fmt::print("Hello, {} world!\n", qt_string.toStdString());
    return 0;
}
