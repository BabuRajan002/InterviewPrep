#!/usr/bin/env python3
"""
Convert Markdown to styled HTML (which can be printed to PDF from browser)
"""
import markdown2
import os

def markdown_to_html(md_file, html_file):
    """Convert markdown file to styled HTML"""

    # Read markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML with extras
    html_body = markdown2.markdown(
        md_content,
        extras=[
            'fenced-code-blocks',
            'tables',
            'header-ids',
            'code-friendly',
            'break-on-newline',
            'toc'
        ]
    )

    # Create full HTML document with print-friendly styling
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Linux Architecture Guide</title>
        <style>
            @media print {{
                @page {{
                    size: A4;
                    margin: 2cm;
                }}

                h1, h2, h3, h4 {{
                    page-break-after: avoid;
                }}

                pre, table, blockquote {{
                    page-break-inside: avoid;
                }}

                h1 {{
                    page-break-before: always;
                }}

                h1:first-of-type {{
                    page-break-before: avoid;
                }}
            }}

            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 900px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
            }}

            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                margin-top: 40px;
                font-size: 2.2em;
            }}

            h1:first-of-type {{
                margin-top: 0;
            }}

            h2 {{
                color: #34495e;
                border-bottom: 2px solid #95a5a6;
                padding-bottom: 8px;
                margin-top: 30px;
                font-size: 1.8em;
            }}

            h3 {{
                color: #2980b9;
                margin-top: 25px;
                font-size: 1.4em;
            }}

            h4 {{
                color: #27ae60;
                margin-top: 20px;
                font-size: 1.2em;
            }}

            code {{
                background-color: #f4f4f4;
                border: 1px solid #ddd;
                border-radius: 3px;
                padding: 2px 6px;
                font-family: 'Monaco', 'Courier New', monospace;
                font-size: 0.9em;
                color: #c7254e;
            }}

            pre {{
                background-color: #f8f8f8;
                border: 1px solid #ddd;
                border-left: 4px solid #3498db;
                border-radius: 5px;
                padding: 15px;
                overflow-x: auto;
                margin: 15px 0;
            }}

            pre code {{
                background-color: transparent;
                border: none;
                padding: 0;
                color: #333;
                font-size: 0.85em;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}

            th {{
                background-color: #3498db;
                color: white;
                padding: 12px;
                text-align: left;
                border: 1px solid #2980b9;
                font-weight: 600;
            }}

            td {{
                padding: 10px 12px;
                border: 1px solid #ddd;
            }}

            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}

            tr:hover {{
                background-color: #f0f0f0;
            }}

            ul, ol {{
                margin: 15px 0;
                padding-left: 30px;
            }}

            li {{
                margin: 8px 0;
            }}

            blockquote {{
                border-left: 4px solid #3498db;
                padding-left: 15px;
                margin: 20px 0;
                color: #555;
                font-style: italic;
                background-color: #f9f9f9;
                padding: 10px 15px;
            }}

            strong {{
                color: #2c3e50;
                font-weight: 600;
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
                transition: color 0.2s;
            }}

            a:hover {{
                color: #2980b9;
                text-decoration: underline;
            }}

            /* Print button styles */
            .print-instructions {{
                background-color: #fffbcc;
                border: 2px solid #f0e68c;
                border-radius: 5px;
                padding: 15px;
                margin: 20px 0;
                text-align: center;
            }}

            .print-button {{
                background-color: #3498db;
                color: white;
                border: none;
                padding: 12px 24px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                margin: 10px;
                transition: background-color 0.3s;
            }}

            .print-button:hover {{
                background-color: #2980b9;
            }}

            @media print {{
                .print-instructions, .print-button {{
                    display: none;
                }}
            }}

            /* Syntax highlighting for bash commands */
            pre code {{
                display: block;
                white-space: pre;
            }}
        </style>
        <script>
            function printToPDF() {{
                window.print();
            }}
        </script>
    </head>
    <body>
        <div class="print-instructions">
            <h3 style="margin-top: 0; color: #d35400;">📄 Ready to Save as PDF</h3>
            <p>Click the button below or use <strong>Cmd+P</strong> (Mac) / <strong>Ctrl+P</strong> (Windows) to open print dialog</p>
            <p>Then select <strong>"Save as PDF"</strong> as the destination</p>
            <button class="print-button" onclick="printToPDF()">🖨️ Save as PDF</button>
        </div>

        {html_body}

        <hr>
        <footer style="text-align: center; color: #7f8c8d; margin-top: 40px; padding: 20px;">
            <p><em>Linux Architecture - Comprehensive Guide</em></p>
            <p>Document Version 2.0 | Last Updated: December 12, 2025</p>
        </footer>
    </body>
    </html>
    """

    # Write HTML file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"✓ HTML created successfully: {html_file}")
    print(f"✓ File size: {os.path.getsize(html_file) / 1024:.2f} KB")
    print(f"\n📖 Next steps:")
    print(f"   1. Open {html_file} in your browser")
    print(f"   2. Press Cmd+P (Mac) or Ctrl+P (Windows)")
    print(f"   3. Select 'Save as PDF' as destination")
    print(f"   4. Choose your preferred settings and save")
    print(f"\n   Or click the 'Save as PDF' button in the browser!")

if __name__ == "__main__":
    md_file = "01_Linux_Architecture_Enhanced.md"
    html_file = "01_Linux_Architecture_Enhanced.html"

    if not os.path.exists(md_file):
        print(f"Error: {md_file} not found!")
        exit(1)

    try:
        markdown_to_html(md_file, html_file)
    except Exception as e:
        print(f"Error converting to HTML: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
