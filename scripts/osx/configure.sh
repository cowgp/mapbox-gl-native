#!/usr/bin/env bash

BOOST_VERSION=1.59.0
BOOST_LIBPROGRAM_OPTIONS_VERSION=1.59.0
LIBCURL_VERSION=system
GLFW_VERSION=3.1.2
LIBPNG_VERSION=1.6.18
JPEG_VERSION=v9a
SQLITE_VERSION=3.9.1
LIBUV_VERSION=1.7.5
ZLIB_VERSION=system
NUNICODE_VERSION=1.6
LIBZIP_VERSION=1.0.1
VARIANT_VERSION=1.0
GTEST_VERSION=1.7.0
EARCUT_VERSION=0.10.3

function print_qt_flags {
    mason install qt system
    CONFIG+="    'qt_cflags%': $(quote_flags $(mason cflags qt system "QtCore QtGui QtOpenGL QtNetwork QtSql")),"$LN
    CONFIG+="    'qt_ldflags%': $(quote_flags $(mason ldflags qt system "QtCore QtGui QtOpenGL QtNetwork QtSql")),"$LN

    QT_VERSION_MAJOR=$(qmake -query QT_VERSION | cut -d. -f1)
    if [ ${QT_VERSION_MAJOR} -gt 4 ] ; then
        CONFIG+="    'qt_moc%': '$(pkg-config Qt${QT_VERSION_MAJOR}Core --variable=host_bins)/moc',"$LN
    else
        CONFIG+="    'qt_moc%': '$(pkg-config QtCore --variable=moc_location)',"$LN
    fi
}
