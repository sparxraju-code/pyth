#!/bin/bash

DATE=$(date +%F)
BACKUP_FILE="/backups/apache_backup_$DATE.tar.gz"
LOG_FILE="/backups/apache_backup_verification.log"

APACHE_CONF="/etc/apache2"
APACHE_DOCROOT="/var/www/html"

tar -czf "$BACKUP_FILE" "$APACHE_CONF" "$APACHE_DOCROOT"

echo "Backup created on $(date)" >> $LOG_FILE
tar -tzf $BACKUP_FILE >> $LOG_FILE
echo "-----------------------------------" >> $LOG_FILE
