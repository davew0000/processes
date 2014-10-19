# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'first'
        db.create_table(u'stuff_first', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('var_one', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('var_two', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'stuff', ['first'])

        # Adding model 'second'
        db.create_table(u'stuff_second', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('new_var_one', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('new_var_two', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'stuff', ['second'])

        # Adding model 'Order'
        db.create_table(u'stuff_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_raised', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 19, 0, 0))),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('received', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'stuff', ['Order'])


    def backwards(self, orm):
        # Deleting model 'first'
        db.delete_table(u'stuff_first')

        # Deleting model 'second'
        db.delete_table(u'stuff_second')

        # Deleting model 'Order'
        db.delete_table(u'stuff_order')


    models = {
        u'stuff.first': {
            'Meta': {'object_name': 'first'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'var_one': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'var_two': ('django.db.models.fields.IntegerField', [], {})
        },
        u'stuff.order': {
            'Meta': {'object_name': 'Order'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_raised': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 19, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'received': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'stuff.second': {
            'Meta': {'object_name': 'second'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_var_one': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'new_var_two': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['stuff']