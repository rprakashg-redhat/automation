# setup_local
This ansible role automates installing and configuring your local environment with all the necessary tools

## Pre-requisites

### Variables

| Variable Name | Purpose |
| ------------- | ------- |
| installPackageManager | For MacOS Home brew will be installed. Set this to False if you have already installed package manager for your target platform. Default is True |
| installOpenshiftTools | Install Openshift tools, set this to false to skip installation. Default is True |
| binDir | Bin directory where downloaded binaries will be placed. Default is /usr/local/bin |
| mirrorUrl | Default https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest |