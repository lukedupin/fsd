# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table('website_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=10)),
            ('lng', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=10)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('website', ['Location'])

        # Adding model 'Tracker'
        db.create_table('website_tracker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Location'])),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('website', ['Tracker'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table('website_location')

        # Deleting model 'Tracker'
        db.delete_table('website_tracker')


    models = {
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