#!/bin/sh

export CISCO_SPLIT_INC=1
export CISCO_SPLIT_INC_0_ADDR=133.45.0.0
export CISCO_SPLIT_INC_0_MASK=255.255.0.0
export CISCO_SPLIT_INC_0_MASK_LEN=16

## Where is VPN Client Script?
## if you use mac, comment off next line.
#export VPNC_SCRIPT_DIR=/usr/local/etc
## else if you use linux, comment off next line.
export VPNC_SCRIPT_DIR=/usr/share/vpnc-scripts # Linux

exec $VPNC_SCRIPT_DIR/vpnc-script
