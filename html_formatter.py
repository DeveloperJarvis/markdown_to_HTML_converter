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
# HTML FORMATTER MODULE
# --------------------------------------------------
"""
Docstring for HTML formatter
Responsibility:
Ensures that the final HTML output is properly structured, formatted
and wrapped.
Components:
N/A
Key Functions:
1. add_doctype(): Adds the <!DOCTYPE html> declaration at the start
of the HTML document
2. add_html_structure(): Wraps the HTML content in <html>, <head>,
and <body> tags.
3. add_meta_tags(): Adds meta information such as character encoding,
viewport settings, etc.
Data Structures:
N/A
Outputs:
A complete HTML document string with the required structure.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------

# add_doctype(): Adds the <!DOCTYPE html> declaration at the start
# of the HTML document
def add_doctype():
    return "<!DOCTYPE html>"

# add_html_structure(): Wraps the HTML content in <html>, <head>,
# and <body> tags.
def start_head_structure():
    return "<html>\n<head>\n<title>Markdown to HTML</title>\n"

def end_head_structure():
    return "</head>\n"

# add_meta_tags(): Adds meta information such as character encoding,
# viewport settings, etc.
def add_meta_tags():
    return '<meta charset="UTF-8">\n<meta name="veiwport" content="width=device-width, initial-scale=1.0">'

def start_body_structure():
    return "<body>"

def end_body_structure():
    return "</body>\n</html>"