from odoo import models, fields

class ReportTOC(models.Model):
    _name = 'report.toc'
    _description = 'Report Table of Contents'
    _order = 'name'

    name = fields.Char(
        string='TOC Name',
        required=True
    )

    insert_page = fields.Integer(
        string='Insert Page',
        default=1
    )

    main_report_id = fields.Many2one(
        'ir.actions.report',
        string='Main Report',
        required=True,
        domain="[('report_type', '=', 'qweb-pdf')]"
    )

    toc_report_id = fields.Many2one(
        'ir.actions.report',
        string='TOC Report Template',
        required=True,
        domain="[('report_type', '=', 'qweb-pdf')]",
        default=lambda self: self.env.ref(
            'report_toc.action_report_toc_report',
            raise_if_not_found=False
        )
    )

    toc_line_ids = fields.One2many(
        'report.toc.line',
        'toc_id',
        string='TOC Lines'
    )

    active = fields.Boolean(default=True)



class ReportTOCLine(models.Model):
    _name = 'report.toc.line'
    _description = 'Report TOC Line'
    _order = 'sequence, id'

    toc_id = fields.Many2one(
        'report.toc',
        ondelete='cascade',
        required=True
    )

    sequence = fields.Integer(default=10)

    toc_heading = fields.Char(
        string='TOC Heading',
        required=True,
        help='Heading displayed in the TOC page'
    )

    search_heading = fields.Char(
        string='Search Text in PDF',
        required=True,
        help='Text searched inside the main PDF'
    )
