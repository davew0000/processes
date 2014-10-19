# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Workflow'
        db.create_table(u'wf_workflow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'wf', ['Workflow'])

        # Adding model 'Task'
        db.create_table(u'wf_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('module', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'wf', ['Task'])

        # Adding model 'Node'
        db.create_table(u'wf_node', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workflow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wf.Workflow'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wf.Task'])),
            ('start_node', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('terminal_node', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'wf', ['Node'])

        # Adding model 'Transition'
        db.create_table(u'wf_transition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from', to=orm['wf.Node'])),
            ('to_node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to', to=orm['wf.Node'])),
            ('index', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'wf', ['Transition'])

        # Adding model 'Process'
        db.create_table(u'wf_process', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model_set', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('current_node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wf.Node'], null=True, blank=True)),
            ('date_initiated', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 19, 0, 0))),
            ('transition_ready', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'wf', ['Process'])


    def backwards(self, orm):
        # Deleting model 'Workflow'
        db.delete_table(u'wf_workflow')

        # Deleting model 'Task'
        db.delete_table(u'wf_task')

        # Deleting model 'Node'
        db.delete_table(u'wf_node')

        # Deleting model 'Transition'
        db.delete_table(u'wf_transition')

        # Deleting model 'Process'
        db.delete_table(u'wf_process')


    models = {
        u'wf.node': {
            'Meta': {'object_name': 'Node'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_node': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wf.Task']"}),
            'terminal_node': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wf.Workflow']"})
        },
        u'wf.process': {
            'Meta': {'object_name': 'Process'},
            'current_node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wf.Node']", 'null': 'True', 'blank': 'True'}),
            'date_initiated': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 19, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_set': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'transition_ready': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'wf.task': {
            'Meta': {'object_name': 'Task'},
            'function': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'wf.transition': {
            'Meta': {'object_name': 'Transition'},
            'from_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from'", 'to': u"orm['wf.Node']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'to_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to'", 'to': u"orm['wf.Node']"})
        },
        u'wf.workflow': {
            'Meta': {'object_name': 'Workflow'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['wf']