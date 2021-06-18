# Copyright 2020 Akretion <raphael.reverdy@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade

column_renames = {
    "account_move_line": [("fsm_order_id", None)],
}


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
        env.cr, """
        ALTER TABLE account_move_line
        ADD COLUMN fsm_order_id integer""",
    )
    openupgrade.logged_query(
        env.cr,
        """
        UPDATE account_move_line aml
        SET fsm_order_id = ail.fsm_order_id
        FROM account_invoice_line ail
        WHERE ail.id = aml.old_invoice_line_id""",
    )
    openupgrade.rename_columns(env.cr, column_renames)
