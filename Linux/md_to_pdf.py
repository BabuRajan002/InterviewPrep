#!/usr/bin/env python3
"""
Convert Markdown to PDF with proper styling
"""
import markdown2
from weasyprint import HTML, CSS
import os

def markdown_to_pdf(md_file, pdf_file):
    """Convert markdown file to PDF with custom styling"""

    # Read markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML with extras
    html_content = markdown2.markdown(
        md_content,
        extras=[
            'fenced-code-blocks',
            'tables',
            'header-ids',
            'code-friendly',
            'break-on-newline'
        ]
    )

    # Create full HTML document with styling
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Linux Architecture Guide</title>
        <style>
            @page {{
                size: A4;
                margin: 2cm;
                @bottom-right {{
                    content: "Page " counter(page) " of " counter(pages);
                    font-size: 9pt;
                    color: #666;
                }}
            }}

            body {{
                font-family: 'Segoe UI', Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 100%;
            }}

            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                margin-top: 30px;
                page-break-before: always;
                font-size: 28pt;
            }}

            h1:first-of-type {{
                page-break-before: avoid;
                margin-top: 0;
            }}

            h2 {{
                color: #34495e;
                border-bottom: 2px solid #95a5a6;
                padding-bottom: 8px;
                margin-top: 25px;
                font-size: 20pt;
                page-break-after: avoid;
            }}

            h3 {{
                color: #2980b9;
                margin-top: 20px;
                font-size: 16pt;
                page-break-after: avoid;
            }}

            h4 {{
                color: #27ae60;
                margin-top: 15px;
                font-size: 14pt;
            }}

            code {{
                background-color: #f4f4f4;
                border: 1px solid #ddd;
                border-radius: 3px;
                padding: 2px 5px;
                font-family: 'Courier New', monospace;
                font-size: 9pt;
                color: #c7254e;
            }}

            pre {{
                background-color: #f8f8f8;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 15px;
                overflow-x: auto;
                page-break-inside: avoid;
                margin: 15px 0;
            }}

            pre code {{
                background-color: transparent;
                border: none;
                padding: 0;
                color: #333;
                font-size: 9pt;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 15px 0;
                page-break-inside: avoid;
                font-size: 10pt;
            }}

            th {{
                background-color: #3498db;
                color: white;
                padding: 12px;
                text-align: left;
                border: 1px solid #2980b9;
            }}

            td {{
                padding: 10px;
                border: 1px solid #ddd;
            }}

            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}

            ul, ol {{
                margin: 10px 0;
                padding-left: 30px;
            }}

            li {{
                margin: 5px 0;
            }}

            blockquote {{
                border-left: 4px solid #3498db;
                padding-left: 15px;
                margin: 15px 0;
                color: #555;
                font-style: italic;
            }}

            strong {{
                color: #2c3e50;
            }}

            em {{
                color: #555;
            }}

            hr {{
                border: none;
                border-top: 2px solid #ddd;
                margin: 30px 0;
            }}

            a {{
                color: #3498db;
                text-decoration: none;
            }}

            a:hover {{
                text-decoration: underline;
            }}

            .page-break {{
                page-break-before: always;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Convert HTML to PDF
    print(f"Converting {md_file} to PDF...")
    HTML(string=full_html).write_pdf(pdf_file)
    print(f"✓ PDF created successfully: {pdf_file}")

    # Get file size
    file_size = os.path.getsize(pdf_file)
    print(f"✓ File size: {file_size / 1024:.2f} KB")

if __name__ == "__main__":
    md_file = "01_Linux_Architecture_Enhanced.md"
    pdf_file = "01_Linux_Architecture_Enhanced.pdf"

    if not os.path.exists(md_file):
        print(f"Error: {md_file} not found!")
        exit(1)

    try:
        markdown_to_pdf(md_file, pdf_file)
    except Exception as e:
        print(f"Error converting to PDF: {e}")
        exit(1)
