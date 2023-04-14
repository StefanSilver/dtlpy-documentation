# Dataloop JSON Examples

This section provides you various examples for a `dataloop.json` file for developing stages ([Debug Applications](./index.md)).

## Floating Window

The code below defines a component called "reference-viewer" in JSON format. The component has a supported slot of "floatingWindow" type and a configuration object with properties for width, height, resizeable, and background color. There are no specific resource requirements or dependencies specified in the component's conditions object. 

```json
{
  "components": {
    "panels": [
      {
        "name": "reference-viewer",
        "supportedSlots": [
          {
            "type": "floatingWindow",
            "configuration": {
              "layout": {
                "width": 455,
                "height": 340,
                "resizeable": true,
                "backgroundColor": "dl-color-studio-panel"
              }
            }
          }
        ],
        "conditions": {
          "resources": []
        }
      }
    ]
  }
}
```

### Item Viewer
This is a JSON code block that defines a component called "item-viewer". It specifies that the component supports a single slot of type "itemViewer" with a specific configuration for layout. It also sets conditions for when this component can be used, specifically when the resources being viewed are items with a mimetype of "image/*".
```json

{
  "components": {
    "panels": [
      {
        "name": "item-viewer",
        "supportedSlots": [
          {
            "type": "itemViewer",
            "configuration": {
              "layout": {
                "leftBar": false,
                "rightBar": false,
                "bottomBar": false
              }
            }
          }
        ],
        "conditions": {
          "resources": [
            {
              "entityType": "item",
              "filter": {
                "metadata.system.mimetype": "image/*"
              }
            }
          ]
        }
      }
    ]
  }
}
```

### Pipeline Node
This is a JSON code block that defines a pipeline system with custom nodes. It includes a pipeline node panel with a single pipeline node config slot, a custom pipeline node called `data_split` that belongs to the "data" category, and a `custom_nodes` module with two functions: `data_split` and `test`.
```json
{
  "components": {
    "panels": [
      {
        "name": "pipelineNodePanel",
        "supportedSlots": [
          {
            "type": "pipelineNodeConfig",
            "configuration": {}
          }
        ],
        "conditions": {
          "resources": []
        }
      }
    ],
    "pipelineNodes": [
      {
        "invoke": {
          "type": "function",
          "namespace": "custom_nodes.data_split"
        },
        "categories": [
          "data"
        ]
      }
    ],
    "modules": [
      {
        "name": "custom_nodes",
        "entryPoint": "modules/main.py",
        "className": "Runner",
        "initInputs": [],
        "functions": [
          {
            "name": "data_split",
            "description": "Data splitting custom node",
            "input": [
              {
                "type": "Item",
                "name": "item"
              }
            ],
            "output": [
              {
                "type": "Item",
                "name": "item"
              }
            ],
            "displayIcon": "qa-sampling",
            "displayName": "Data Split"
          },
          {
            "name": "test",
            "description": "Testing the waters",
            "input": [],
            "output": [],
            "displayIcon": "node-train",
            "displayName": "Test"
          }
        ]
      }
    ]
  }
}
```

### Toolbars

This is a JSON code block that defines a dialog panel component with a single dialog slot that has a specific layout configuration. It also defines two toolbars, one to invoke the dialog panel and the other to invoke a custom function called `my_function` belonging to the `my_module` module. The `my_function` takes an Item as input and als outputs an Item. You can use this code to Invoke a panel or a function in an Application.


```json
{
  "components": {
    "panels": [
      {
        "name": "dialogPanel",
        "supportedSlots": [
          {
            "type": "dialog",
            "configuration": {
              "layout": {
                "position": "center",
                "width": 455,
                "height": 340
              }
            }
          }
        ],
        "conditions": {
          "resources": []
        }
      }
    ],
    "toolbars": [
      {
        "displayName": "Run Dialog",
        "invoke": {
          "type": "panel",
          "namespace": "dialogPanel"
        },
        "icon": "icon-dl-add",
        "location": "datasetsDashboard",
        "conditions": {
          "resources": []
        }
      },
      {
        "displayName": "Run function",
        "invoke": {
          "type": "function",
          "namespace": "my_module.my_function"
        },
        "icon": "icon-dl-edit",
        "location": "itemMenu",
        "conditions": {
          "resources": []
        }
      }
    ],
    "modules": [
      {
        "name": "my_module",
        "entryPoint": "modules/main.py",
        "className": "Runner",
        "initInputs": [],
        "functions": [
          {
            "name": "my_function",
            "input": [
              {
                "type": "Item",
                "name": "item"
              }
            ],
            "output": [
              {
                "type": "Item",
                "name": "item"
              }
            ]
          }
        ]
      }
    ]
  }
}
```
