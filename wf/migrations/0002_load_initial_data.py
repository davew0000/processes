# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        from django.core.management import call_command
        call_command("loaddata", "initial_workflow.json")
        
    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'wf.node': {
            'Meta': {'object_name': 'Node'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wf.Task']"}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wf.Workflow']"})
        },
        u'wf.process': {
            'Meta': {'object_name': 'Process'},
            'current_node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wf.Node']", 'null': 'True', 'blank': 'True'}),
            'date_initiated': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_set': ('django.db.models.fields.TextField', [], {})
        },
        u'wf.task': {
            'Meta': {'object_name': 'Task'},
            'function_ref': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'wf.transition': {
            'Meta': {'object_name': 'Transition'},
            'from_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from'", 'to': u"orm['wf.Node']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to'", 'to': u"orm['wf.Node']"})
        },
        u'wf.workflow': {
            'Meta': {'object_name': 'Workflow'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['wf']
    symmetrical = True
