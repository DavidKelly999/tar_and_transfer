## Quickstart
 Install requirements: `pip install -r requirements.txt`
 
 Modify flow/flow-inputs.yaml to add your funcx endpoint, collections, and file paths 
 
 Run flow:
 `globus-automate flow run 50100f51-866b-48fb-8f93-28dd19078132 --flow-input flow/flow-input.yaml --label "Tar"`

## How to modify tar function

 1. Modify the tar function located at funcx/tar.py
 2. Use local_runner.py and remote_runner.py to test your changes
 3. Register the tar function with funcx by running register_function.py
 4. Change funcx_function value in flow/flow-inputs.yaml

## How to modify flow
The flow/ directory contains the automate flow definition, inputs, and input schema. To deploy a new flow:

`globus-automate flow deploy --title "Tar and transfer" --definition flow/definition.yaml --input-schema flow/input-schema.yaml --flow-starter all_authenticated_users --flow-viewer public`
