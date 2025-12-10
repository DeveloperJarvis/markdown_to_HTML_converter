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
# FILE I/O MODULE
# --------------------------------------------------
"""
Docstring for file I/O
Responsibility:
Handles input and output files (reading the Markdown file and 
writing the HTML file).
Components:
N/A
Key Functions:
1. read_markdown_file(file_path): Reads the input Markdown file.
2. write_html_file(output_path, html_content): Writes the HTML
output to a file.
3. convert_markdown_to_html(input_file, output_file): Orchestrates
the entire conversion process from reading the Markdown file to
writing the HTML file.
Data Structures:
N/A
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from parser import (parse_paragraphs, parse_code_blocks,
                    parse_headers, parse_inline_syntax,
                    parse_lists)
from converter import (convert_code, convert_headers,
                       convert_inline_elements, convert_lists,
                       convert_paragraphs)
from html_formatter import (add_doctype,add_meta_tags, 
                            start_head_structure,
                            end_head_structure,
                            start_body_structure,
                            end_body_structure)

'''
The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
 
 ``x''  Create - will create a file, returns an error if the file exists
'''

# read_markdown_file(file_path): Reads the input Markdown file.
def read_markdown_file(file_path):
    try:
        with open(file=file_path, mode="r") as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return f"Error: The file {file_path} is not found"
    except Exception as e:
        return f"Error: An exception occurred: {e}"


# write_html_file(output_path, html_content): Writes the HTML
# output to a file.
def write_html_file(output_path, html_content):
    try:
        with open(file=output_path, mode="a") as f:
            f.write(html_content)
        return f"Content successfully appended to {output_path}"
    except FileNotFoundError:
        return f"Error: The file {output_path} is not found"
    except Exception as e:
        return f"Error: An exception occurred: {e}"


# --------------------------------------------------
# DATA FLOW AND INTERACTION
# --------------------------------------------------
"""
1. Input: The user provides a Markdown file or string.
2. Parsing: The Parser Module processes the input and breaks it
down into structured components.
- The tokenizer identifies Markdown elements such as headers, lists,
    code, etc.
- The regular expression patterns match specific syntax for inline
    elements like bold, italics and links.
3. Conversion: The parsed data is passed to the Converter Module,
which converts each element into its corresponding HTML tag.
4. Formatting: The HTML Formatter Module ensures the HTML document
is well-structured by adding a doctype, HTML tags and other
necessary elements.
5. Output: The final HTML document is written to a specified output
file via the File I/O Module.
"""

# convert_markdown_to_html(input_file, output_file): Orchestrates
# the entire conversion process from reading the Markdown file to
# writing the HTML file.
def convert_markdown_to_html(input_file, output_file):

    '''1. Input: The user provides a Markdown file or string.'''
    input_markdown_content = read_markdown_file(input_file)
    
    # print("DEBUG: len:", len(input_markdown_content))
    # Empty file handling
    if input_markdown_content == None:
        output_html_response = write_html_file(
        output_path=output_file,
        html_content=None
        )
        return 0    
    '''2. Parsing: The Parser Module processes the input and breaks it
            down into structured components.'''
    headers = parse_headers(input_markdown_content)
    lists = parse_lists(input_markdown_content)
    # paragraphs = parse_paragraphs(input_markdown_content)
    inline_syntax = parse_inline_syntax(input_markdown_content)
    code_blocks = parse_code_blocks(input_markdown_content)

    # Combine parsed components (headers, lists, paragraphs, etc.)
    # This could be a list or dictionary of components for latter use
    parsed_data = {
        'headers': headers,
        'lists': lists,
        # 'paragraphs': paragraphs,
        'inline_syntax': inline_syntax,
        'code_blocks': code_blocks
    }
    # print("DEBUG: parsed_data['paragraphs']:\n", parsed_data['paragraphs'])

    '''3. Conversion: The parsed data is passed to the Converter Module,
            which converts each element into its corresponding HTML tag.'''
    html_content = ""

    '''4. Formatting: The HTML Formatter Module ensures the HTML document
            is well-structured by adding a doctype, HTML tags and other
            necessary elements.'''
    html_content = add_doctype() + "\n"
    html_content += start_head_structure() + "\n"
    html_content += add_meta_tags() + "\n"
    html_content += end_head_structure() + "\n"

    html_content += start_body_structure() + "\n"
    # print("Debug: \n\n", html_content)
    '''3. Continued: Conversion of parsed data to HTML tags'''
    html_content += convert_headers(parsed_data['headers'])
    # print("Debug: \n\n", html_content)
    html_content += convert_lists(parsed_data['lists'])
    # print("Debug: \n\n", html_content)
    # html_content += convert_paragraphs(parsed_data['paragraphs'])
    # print("Debug: \n\n", html_content)
    html_content += convert_inline_elements(parsed_data['inline_syntax'])
    # print("Debug: \n\n", html_content)
    html_content += convert_code(parsed_data['code_blocks'])
    # print("Debug: \n\n", html_content)
    html_content += end_body_structure() + "\n"
    # print("Debug: \n\n", html_content)

    '''5. Output: The final HTML document is written to a specified output
            file via the File I/O Module.'''
    output_html_response = write_html_file(
        output_path=output_file,
        html_content=html_content
        )
