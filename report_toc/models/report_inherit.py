import tempfile
import fitz
import os
from html import unescape

from odoo import models, api

class ReportActions(models.AbstractModel):
    _inherit = 'ir.actions.report'

    @api.model
    def _render_qweb_pdf(self, report_ref, res_ids, data=None, **kwargs):
        report = self._get_report(report_ref)

        # Render MAIN report ONCE
        main_pdf_bytes, content_type = super()._render_qweb_pdf(
            report_ref, res_ids, data=data, **kwargs
        )

        # Save to temp file for analysis
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            f.write(main_pdf_bytes)
            main_pdf_path = f.name

        doc = fitz.open(main_pdf_path)

        toc_page_map = {}
        toc_records = self.env['report.toc'].search([
            ('main_report_id', '=', report.id),
            ('active', '=', True),
        ], limit=1)

        if toc_records:
            for line in toc_records.toc_line_ids:
                search_text = unescape(line.search_heading).upper().strip()
                print('searchtest',search_text)
                for i, page in enumerate(doc, start=1):
                    page_text = page.get_text().upper()
                    if search_text in page_text:
                        toc_page_map[line.id] = i
                        break

        doc.close()
        os.unlink(main_pdf_path)
        print('page_found',toc_page_map)

        if not toc_records:
            return main_pdf_bytes, content_type

        # Prepare data for TOC report
        toc_data = dict(data or {})
        toc_data.update({
            'toc_page_map': toc_page_map,
            'toc_id': toc_records.id,
        })

        # Render TOC PDF
        toc_report = toc_records.toc_report_id
        toc_pdf_bytes, _ = toc_report._render_qweb_pdf(
            toc_report.report_name,
            [toc_records.id],
            data=toc_data
        )

        # Merge PDFs
        final_doc = fitz.open(stream=main_pdf_bytes, filetype="pdf")
        toc_doc = fitz.open(stream=toc_pdf_bytes, filetype="pdf")

        insert_page = max(0, toc_records.insert_page - 1)

        final_doc.insert_pdf(toc_doc, start_at=insert_page)

        output = final_doc.tobytes()

        final_doc.close()
        toc_doc.close()

        return output, content_type
