Report Table of Contents (ToC) – Odoo 18
Author: Abdulla Basil

Version: 18.0.1.0.0

License: AGPL-3

✨ Overview
This module empowers Odoo users to generate professional, automated Table of Contents (ToC) for any QWeb PDF report. It is the perfect solution for long business documents like product catalogs, technical manuals, or lengthy project quotations where navigation is key.

Unlike static reports, this module dynamically scans your generated PDF for specific headings and maps them to the correct page numbers automatically.

🎯 Features
📜 Automated ToC Generation: Dynamically creates a Table of Contents based on text markers within your PDF.

📍 Flexible Insertion: Choose exactly which page the ToC should appear on.

🔢 Smart Re-pagination: Automatically recalculates and replaces footer page numbers (e.g., "Page 1 of 10") to account for the added ToC pages.

🎨 Odoo 18 Styled: The ToC template is designed to match the modern Odoo 18 professional report layout.

⚙️ Configurable per Report: Enable or disable ToC for specific reports without affecting the rest of the system.

🛠️ Custom Footers: Define specific footer content (disclaimers/addresses) directly from the ToC configuration.

🚀 How It Works
Define Markers: Specify the "Search Text" (e.g., "Terms & Conditions") that the module should look for.

Scan & Map: The module renders the report, scans for those text markers using PyMuPDF, and records their page numbers.

Inject & Merge: It generates the ToC page with the correct page links and merges it back into your document at your desired insertion point.

Finalize: It cleans up the footers across the entire document to ensure page numbering remains perfectly sequential.

🛠 Installation & Requirements
Dependencies: This module requires the PyMuPDF (fitz) Python library.

Command: pip install pymupdf

Compatibility: Optimized for Odoo 18.0 (Community & Enterprise).

📂 Module Structure
Models: Configuration for ToC rules and line items.

Reports: Custom QWeb template for the ToC page.

Actions: Inherited report rendering logic for seamless integration.