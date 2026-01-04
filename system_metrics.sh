#!/bin/bash
LOG="/var/log/system_metrics.log"
echo "===== $(date) =====" >> $LOG
echo "--- Disk Usage ---" >> $LOG
df -h >> $LOG
echo "--- Memory Usage ---" >> $LOG
free -h >> $LOG
echo "--- Top CPU-Consuming Processes ---" >> $LOG
ps -eo pid,cmd,%cpu,%mem --sort=-%cpu | head -10 >> $LOG
echo "" >> $LOG
