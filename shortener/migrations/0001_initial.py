# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Url'
        db.create_table('shortener_url', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('expanded', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('shortened', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('shortener', ['Url'])


    def backwards(self, orm):
        # Deleting model 'Url'
        db.delete_table('shortener_url')


    models = {
        'shortener.url': {
            'Meta': {'object_name': 'Url'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expanded': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shortened': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['shortener']