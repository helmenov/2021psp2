#!/bin/bash

export CISCO_SPLIT_INC = 1
export CISCO_SPLIT_INC_0_ADDR = 133.45.0.0
export CISCO_SPLIT_INC_0_MASK = 255.255.0.0
export CISCO_SPLIT_INC_0_MASK_LEN = 16
export VPNC_SCRIPT_DIR=/usr/share/vpnc-scripts

exec $VPNC_SCRIPT_DIR/vpnc-script


