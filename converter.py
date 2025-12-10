# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the markdown_to_HTML_converter Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# markdown_to_HTML_converter - Write a small parser that converts basic Markdown syntax into HTML
#                               Skills: string parsing, file handling
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# CONVERTER MODULE
# --------------------------------------------------
"""
Docstring for converter
Responsibility:
Converts the parsed Markdown components into corresponding HTML
tags.
Components:
1. HTML Builder - A module responsible for converting parsed 
components into valid HTML tags.
Key Functions:
1. convert_headers(parsed_data): Convers parsed headers into <h1>,
<h2>, etc.
2. convert_lists(parsed_data): Converts parsed list data into <ul>
and <ol>, <li> tags.
3. convert_paragraphs(parsed_data): Converts plain text into <p>
tags.
4. convert_inline_elements(parsed_data): Converts bold (** or __),
italic (* or _), and other inline elements into corresponding HTML
tags like <strong>, <em>, etc.
5. convert_code(parsed_data): Converts inline code and code blocks
into <code> and <pre><code> blocks
Data Structures:
For each parsed element, HTML tags are mapped and inserted 
accordingly.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------

# convert_headers(parsed_data): Convers parsed headers into <h1>, <h2>, etc.
def convert_headers(parsed_data):
    return "".join(parsed_data)

# convert_lists(parsed_data): Converts parsed list data into <ul> and <ol>,
# <li> tags.
def convert_lists(parsed_data):
    # lists are already wrapped into <ol> and <ul>, <li> tags
    return parsed_data

# convert_paragraphs(parsed_data): Converts plain text into <p> tags.
def convert_paragraphs(parsed_data):
    return "".join(parsed_data)

# convert_inline_elements(parsed_data): Converts bold (** or __),
# italic (* or _), and other inline elements into corresponding HTML
# tags like <strong>, <em>, etc.
def convert_inline_elements(parsed_data):
    # Inline elements are already processed in the parser
    return parsed_data

# convert_code(parsed_data): Converts inline code and code blocks
# into <code> and <pre><code> blocks
def convert_code(parsed_data):
    # Code blocks are already processed in the parser
    return parsed_data
    