# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AndroidBugs'
        db.delete_table('website_androidbugs')

        # Adding model 'AndroidBug'
        db.create_table('website_androidbug', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('package_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('package_version', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('stacktrace', self.gf('django.db.models.fields.TextField')(max_length=32768)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('website', ['AndroidBug'])


    def backwards(self, orm):
        # Adding model 'AndroidBugs'
        db.create_table('website_androidbugs', (
            ('stacktrace', self.gf('django.db.models.fields.TextField')(max_length=4096)),
            ('package_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('package_version', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('website', ['AndroidBugs'])

        # Deleting model 'AndroidBug'
        db.delete_table('website_androidbug')


    models = {
        'website.androidbug': {
            'Meta': {'object_name': 'AndroidBug'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'package_version': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'stacktrace': ('django.db.models.fields.TextField', [], {'max_length': '32768'})
        },
        'website.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '10'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '10'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'website.tracker': {
            'Meta': {'object_name': 'Tracker'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Location']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['website']