# Dataloop Applications?

Dataloop Applications are extensions (or add-ons) which can work under the main platform of the Dataloop ecosystem (Dataloop
OS). They receive access to the predefined panels and can utilise Dataloop's Python SDK and Components to create useful features for
the end-user. By learning how to work with applications in Dataloop, users can work more productively and efficiently, by incorporating their custom functionality
with the underlying platform.

## Start an App!
The best way to get started using Apps is to visit out [GitHub Apps Space](https://github.com/dataloop-ai-apps) and see real and working examples.

But if you want to start from scratch, there are a few steps you need to perform:
1. Firstly, you needd to install the [Dataloop Python SDK](https://developers.dataloop.ai/onboarding/01_python_sdk_installation/).
2. Create a directory where you want to initialize the Project in your terminal.
3. In the terminal, type:
```shell
dlp app init
```
4. Follow the installation steps and question - if you leave them empty they will take default values.

The App Package should now ready to start the development!


## Apps

The Applications are installed into the platform (to a Project or entire Organization).  In case you don't know where the Applications are, they are located in the Dashboard in the Dataloop WebUI, as seen in the image below.

![image](https://user-images.githubusercontent.com/58508793/232037983-a66da511-b9e9-4a3e-8b96-ea9b15a72433.png)

From the App Store, search application (by name, categories, etc.) and just click install. All the Application's components should be available to use after installation. You can change any settings or configuration (e.g. machine type, autoscaling) in the app settings.

## DPK - Dataloop Package

The Dataloop Package is a zipped file containing the entire Application's code. It holds all the required components of the Application, the panels it is serving, the Services it uses, and the source code of the Application.

### Panels and Toolbars

A Panel represents the what the user is going to see. The Panel can be deployed into any available slot in the main platform, for example:

1. Item Viewer - overrides the Item viewer content with a custom-made layout to view an Item from the Task browser or
   the Dataset browser.
2. Floating Window - creates a new window on top of the platform, which can be dragged and resized, and shows the Panel.
3. Data Browser - change the browsing view of Items in a Dataset
4. Item Side Panel - Add a new side panel to the Annotation and Info panels in the Item viewer.

A Toolbar is not *served*, it's a Panel that can be rendered into the platform slots, for example:

1. Buttons in the item studio, data browser, task menu, etc.
2. Configuration panels
3. Project widgets

## Modules and Functions

Python functions and modules can be used in the Application, and they are defined in the "modules" directory. For more information about our python modules [check out the Pacakge documentation](https://dataloop.ai/docs/faas-package).

### Services

Services are the carriers of the Application Panels and backend. A service is responsible for running a panel and managing its lifecycle.
The `dl.Service` entity represents the Service, for more information about services, please read the [Service Documentation](https://dataloop.ai/docs/faas-service).

### All the Others

You can also use any other Dataloop entity (Models, Tasks, etc.) in the Applications. Simply define it in the manifest, and it will be created on installation.

### Application Manifest - `dataloop.json`

The json that describes the Application is saved at the root of the Application directory, and is named `dataloop.json`. Is contains all the definitions of the Application's components.

### Store

The Application Store serves as a central repository for saving and publishing some custom Applications, varying from a Metadata viewer Application through audio recording on the website to a completely new UI for the Item viewer.

### Typical Workflow

The typical Workflow for an Application is the following:

1. Create an Application (the FE and BE).
2. Initialize the Application using the command line or Python SDK.
3. Test your Application locally, with the debugging tool in the platform.
4. Tweak in the process the `dataloop.json` file to accommodate your needs.
5. Build your Application and move the files into the appropriate panel directory (the Application's entry point is the `index.html` file).
6. Add the directory to the path of the generated js/CSS files.
7. Deploy your Application. (You might need to change the env using `dl.setenv()` for Dataloop developers)
8. Test a sample script (run it in the root folder of your Application).


If you want to change the Application configuration to build in the right directory (instead of the default ‘/dist’) do the following:

- For Vue - change `vue.config.js` outputDir property to the directory of the panel.
- For React - and `.env` file to the root folder of your Project, and add `BUILD_PATH='PATH_TO_PANEL'`.
- ForAngular - open the `angular.json` file and change `projects.<APP_NAME>.architect.build.options.outputPath` to the path of
the Panel.




