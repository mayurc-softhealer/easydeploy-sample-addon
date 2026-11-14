from odoo.tests import TransactionCase


class TestNote(TransactionCase):
    def test_create(self):
        note = self.env["sample.note"].create({"name": "hello"})
        self.assertEqual(note.name, "hello")
