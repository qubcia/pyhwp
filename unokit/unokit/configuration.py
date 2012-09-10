# -*- coding: utf-8 -*-
#
#                   GNU AFFERO GENERAL PUBLIC LICENSE
#                      Version 3, 19 November 2007
#
#   pyhwp : hwp file format parser in python
#   Copyright (C) 2010 mete0r@sarangbang.or.kr
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

def open_config(nodepath):
    from unokit.services import css
    from unokit.util import dict_to_propseq
    provider = css.configuration.ConfigurationProvider()
    param = dict_to_propseq(dict(nodepath=nodepath))
    configaccess = 'com.sun.star.configuration.ConfigurationAccess'
    return provider.createInstanceWithArguments(configaccess, param)


def get_soffice_product_info():
    config = open_config('/org.openoffice.Setup')

    # see schema in libreoffice/officecfg/registry/schema/org/office/Setup.xcs

    version = tuple(int(x) for x in config.Product.ooSetupVersionAboutBox.split('.'))
    version += (config.Product.ooSetupVersionAboutBoxSuffix,)
    return dict(vendor=config.Product.ooVendor,
                name=config.Product.ooName,
                version=version,
                locale=config.L10N.ooLocale)