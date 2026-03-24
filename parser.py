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
# PARSER MODULE
# --------------------------------------------------
"""
Docstring for parser
Responsibility:
Parses the Markdown input string, identifies various Markdown
components and structures the data in an intermediary format
that is easier to convert into HTML
Components:
1. Tokenizer - Identifies and breaks down different Markdown
token like headings, lists, paragraphs, etc.
2. Pattern Matching: Uses regular expressions or other matching
techniques to detect patterns (e.g. '## Header', '* List', etc.)
3. Syntax Handling: Handles various Markdown features (headers, 
lists, code blocks, inline code, links, etc.)
Key Functions:
1. parse_headers(markdown_text): Detects header syntax (# or ##)
and structures it.
2. parse_lists(markdown_text): Detects list syntax (ordered and
unordered lists) and structures it.
3. parse_inline_syntax(markdown_text): Identifies inline elements
like bold, italics, links, images, etc.
4. parse_code_blocks(markdown_text): Identifies code blocks and
inline code.
Data Structures:
Intermediate structured format (like a dictionary or list)
containing:
    - "type" of element (header, list, paragraph, code, etc.)
    - "content" (text, URL, image, etc.)
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import re

# MARKDOWN HEADER
'''
#       Heading level 1     <h1>Heading level 1</h1>	
##      Heading level 2	    <h2>Heading level 2</h2>	
###     Heading level 3	    <h3>Heading level 3</h3>	
####    Heading level 4	    <h4>Heading level 4</h4>	
#####   Heading level 5	    <h5>Heading level 5</h5>	
######  Heading level 6	    <h6>Heading level 6</h6>

OR

Heading level 1     <h1>Heading level 1</h1>
===============	
Heading level 2     <h2>Heading level 2</h2>
---------------
'''
# parse_headers(markdown_text): Detects header syntax (# or ##)
# and structures it.
def parse_headers(markdown_text):
    # Match headers with 1 to 6 # symbols
    header_pattern = r'^(#{1,6})\s*(.*)$'
    headers = []
    for line in markdown_text.splitlines():
        match = re.match(header_pattern, line)
        if match:
            # Header level corresponds to the number of '#' symbols
            level = len(match.group(1))
            content = match.group(2)
            headers.append(
                # f"<h{level}>{content}</h{level}>"
                {
                    "level": level,
                    "content": content
                }
            )
    return headers

# MARKDOWN LISTS
## MARKDOWN ORDERED LIST
'''
Markdown                 HTML
                        <ol>
1. First item               <li>First item</li>
2. Second item              <li>Second item</li>
3. Third item               <li>Third item</li>
4. Fourth item	            <li>Fourth item</li>
                        </ol>
                        <ol>
1. First item               <li>First item</li>
2. Second item              <li>Second item</li>
3. Third item               <li>Third item</li>
    1. Indented item        <ol>
    2. Indented item            <li>Indented item</li>
4. Fourth item                  <li>Indented item</li>
                            </ol>
                            <li>Fourth item</li>
                        </ol>
'''
## MARKDOWN UNORDERED LIST
'''
Markdown                 HTML
                        <ul>
- First item               <li>First item</li>
- Second item              <li>Second item</li>
- Third item               <li>Third item</li>
- Fourth item	            <li>Fourth item</li>
                        </ul>
                        <ul>
- First item               <li>First item</li>
- Second item              <li>Second item</li>
- Third item               <li>Third item</li>
    - Indented item        <ul>
    - Indented item            <li>Indented item</li>
- Fourth item                  <li>Indented item</li>
                            </ul>
                            <li>Fourth item</li>
                        </ul>
-, *, + can be used interchangebly for unordered lists.
'''
# parse_lists(markdown_text): Detects list syntax (ordered and
# unordered lists) and structures it.
def parse_lists(markdown_text):
    # Match list with numbers
    ordered_list_pattern = r'^\d+\.\s+(.*)$'
    # Match list with '*', '-', '+'
    # unordered_list_pattern = r'^\[\*\-\+]\s+(.*)$'
    unordered_list_pattern = r'^[-*+]\s+(.*)$'
    ordered_list = []
    unordered_list = []
    in_ordered_list = False
    in_unordered_list = False
    for line in markdown_text.splitlines():
        match_ordered = re.match(ordered_list_pattern, line)
        match_unordered = re.match(unordered_list_pattern, line)

        if match_ordered:
            if not in_ordered_list:
                ordered_list.append("<ol>")
                in_ordered_list = True
            ordered_list.append(f"<li>{match_ordered.group(1)}</li>")
        elif match_unordered:
            if not in_unordered_list:
                unordered_list.append("<ul>")
                in_unordered_list = True
            unordered_list.append(f"<li>{match_unordered.group(1)}</li>")
        else:
            if in_ordered_list:
                ordered_list.append("</ol>")
                in_ordered_list = False
            if in_unordered_list:
                unordered_list.append("</ul>")
                in_unordered_list = False
    # Join the lists and return
    if in_ordered_list:
        ordered_list.append("</ol>")
    if in_unordered_list:
        unordered_list.append("</ul>")
    result = "\n".join(filter(None, [
        "\n".join(ordered_list),
        "\n".join(unordered_list)
    ]))

    return result if result.strip() else ""

# MARKDOWN LINEBREAKS
'''
Markdown	                    HTML	
This is the first line.         <p>This is the first line.<br>
And this is the second line.	And this is the second line.</p>
'''
#MARKDOWN BOLD
'''
Markdown                    HTML
I just love **bold text**.	I just love <strong>bold text</strong>.	
I just love __bold text__.	I just love <strong>bold text</strong>.	
Love**is**bold	            Love<strong>is</strong>bold
'''
# MARKDOWN ITALIC
'''
Markdown                                HTML
Italicized text is the *cat's meow*.	Italicized text is the <em>cat's meow</em>.	
Italicized text is the _cat's meow_.	Italicized text is the <em>cat's meow</em>.	
A*cat*meow	                            A<em>cat</em>meow
'''
# MARKDOWN LINKS
'''
Markdown
[link](https://www.example.com/my%20great%20page)
HTML
<a href="https://www.example.com/my great page">link</a>
'''
# MARKDOWN IMAGES
'''
Markdown
![alt text](https://picsum.photos/200/300)
HTML
<img src="https://picsum.photos/200/300" alt="alt text">
'''
# parse_inline_syntax(markdown_text): Identifies inline elements
# like bold, italics, links, images, etc.
def parse_inline_syntax(markdown_text):
    # Bold (either **bold** or __bold__)
    markdown_text = re.sub(r'(\*\*(.*?)\*\*)',r'<strong>\2</strong>',markdown_text)
    markdown_text = re.sub(r'(__(.*?)__)',r'<strong>\2</strong>',markdown_text)

    # Italics (either *italic* or _italic_)
    markdown_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>',markdown_text)
    markdown_text = re.sub(r'_(.*?)_', r'<em>\1</em>',markdown_text)
    
    # Links
    markdown_text = re.sub(r'(\[([^\]]+)\])\(([^)]+)\)', r'<a href="\3">\2</a>', markdown_text)
    
    # Images
    markdown_text = re.sub(r'!(\[([^\]]+)\])\(([^)]+)\)', r'<img src="\3" alt="\2">', markdown_text)
    
    return markdown_text

# Markdown Code
'''
Markdown
`code1`
```
code2
cont
```
HTML
<code>code1</code>
<pre><code>
code2
cont
</code></pre>
'''
# parse_code_blocks(markdown_text): Identifies code blocks and
# inline code.
def parse_code_blocks(markdown_text):
    # triple backticks first
    # Fenced code blocks (```)
    markdown_text = re.sub(
        r'```(.*?)```',
        r'<pre><code>\1</code></pre>',
        markdown_text,
        flags=re.DOTALL
    )

    # then inline
    # Inline code (matches text surrounded by backticks)
    markdown_text = re.sub(
        r'`(.*?)`',
        r'<code>\1</code>',
        markdown_text
    )

    return markdown_text

# MARKDOWN PARAGRAPH
'''
Markdown
I really like using Markdown.
HTML
<p>I really like using Markdown.</p>
Markdown
I think I'll use it to format all of my documents from now on.
HTML
<p>I think I'll use it to format all of my documents from now on.</p>
'''
def parse_paragraphs(markdown_text):
    # Split by double newlines for paragraphs
    # paragraphs = markdown_text.split('\n\n')
    parsed_paragraphs = []
    in_ordered_list = False
    in_unordered_list = False
    for p in markdown_text.splitlines():
        # print("Debug: "+ f"<p>{parse_inline_syntax(p)}</p>")
        # parsed_paragraphs.append(f"<p>{parse_inline_syntax(p)}</p>")
        # Skip headings
        if re.match(r'^(#{1,6})\s*(.*)$', p): 
            continue
        # skip inline code
        # elif re.match(r'`(.*?)`', p):
        #     continue
        # # skip code blocks (triple backticks)
        # elif re.match(r'```(.*?)```', p):
        #     continue
        # skip unordered lists
        elif re.match(r'^[-*+]\s+(.*)$', p.strip()):
            continue
        # skip ordered lists
        elif re.match(r"^\d+\.\s+", p.strip()):
            continue
        else:
            # Only wrap paragraphs tjat are not part of lists or code blocks
            if p.strip():
                # if "<code>" in p or "<pre>" in p:
                if p.strip().startswith("<"):
                    parsed_paragraphs.append(p)
                else:
                    parsed_paragraphs.append(f"<p>{parse_inline_syntax(p.strip())}</p>")
    return "\n".join(parsed_paragraphs)
