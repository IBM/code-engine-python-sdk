#!/bin/bash
##################################################
# Licensed Materials - Property of IBM
# IBM Cloud Code Engine, 5900-AB0
# © Copyright IBM Corp. 2020, 2023
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.
##################################################

set -e

function get_repo {
    if [ ! -d "$apiDirectory" ]; then
        printf "Cloning github.ibm.com/coligo/api...\n"
        git clone https://github.ibm.com/coligo/api.git "$apiDirectory"
    else
        printf "github.ibm.com/coligo/api already cloned, getting latest...\n"
        cd "$apiDirectory"
        if [[ $(git status --porcelain) ]]; then
            printf "Local working tree contains changes... stashing them\n"
            git stash
        fi
        git checkout main
        git pull
        cd "$rootDirectory"
    fi
}

echo ""
echo "----------------------------------"
echo "Getting test dependencies ..."
echo "----------------------------------"
rootDirectory=$(pwd)
apiDirectory=$rootDirectory/api
get_repo