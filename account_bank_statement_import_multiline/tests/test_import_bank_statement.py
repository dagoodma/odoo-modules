from openerp.tests.common import TransactionCase
from openerp.modules.module import get_module_resource

class TestMultilineFile(TransactionCase):
    """Tests for import bank statement ofx file format (account.bank.statement.import)
    """

    def setUp(self):
        super(TestMultilineFile, self).setUp()
        self.statement_import_model = self.registry('account.bank.statement.import')
        self.bank_statement_model = self.registry('account.bank.statement')

    def test_multiline_file_import(self):
        cr, uid = self.cr, self.uid
        creation_wiz_obj = self.registry('account.bank.statement.import.journal.creation')
        """ofx_file_path = get_module_resource('account_bank_statement_import_ofx', 'test_ofx_file', 'test_ofx.ofx')
        ofx_file = open(ofx_file_path, 'rb').read().encode('base64')
        bank_statement_id = self.statement_import_model.create(cr, uid, dict(
            data_file=ofx_file,
        ))
        res = self.statement_import_model.import_file(cr, uid, [bank_statement_id])
        self.assertEquals(res['res_model'], 'account.bank.statement.import.journal.creation', 'boom')
        ctx = res.get('context', {}).copy()
        wiz_id = creation_wiz_obj.create(cr, uid, {}, context=ctx)
        wiz = creation_wiz_obj.browse(cr, uid, [wiz_id], context=ctx)
        wiz.create_journal()

        statement_id = self.bank_statement_model.search(cr, uid, [('name', '=', '000000123')])
        bank_st_record = self.bank_statement_model.browse(cr, uid, statement_id)
        self.assertEquals(bank_st_record.balance_start, 2516.56)
        self.assertEquals(bank_st_record.balance_end_real, 2156.56)"""
