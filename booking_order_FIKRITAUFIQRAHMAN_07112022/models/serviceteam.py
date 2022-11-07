from odoo import api, fields, models

class serviceteam(models.Model):
    _name = "service.team"
    _description = 'new description'

    name = fields.Char(
        string='Team Name',
        required=True,
        readonly=False,
        default=False)

    team_leader_id = fields.Many2one(
        comodel_name='res.users',
        string='Team Leader',
        required=True,
        readonly=False,
        default=False)
    
    team_member_ids = fields.Many2many(
        comodel_name='res.users',
        string='Team Members',
        required=False,
        readonly=False,
        default=False)
    
    