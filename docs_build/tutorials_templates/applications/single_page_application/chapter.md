# Create and test a Dataloop app locally.

## How to create and test Dataloop Applications?

### TL;DR
The simple and quick way you can do this is shown in the .gif file below. Follow the steps presented there and they will guide you through how to do it. If you want the long explanation, keep reading this section.
![Tutorial Image](https://github.com/dataloop-ai-apps/dtlpy-documentation/raw/tutorial-application/assets/apps/app_testing_tutorial.gif "Tutorial Image")

The exact steps are as follows:
1. Create a client-side Application using the framework of your choice. Use our [JS SDK](https://dtlpy-documentation.redoc.ly/resources/dtljs/) to work with Dataloop entities.
2. Serve `dataloop.json` and `app.json` files on the root of your Application.
3. Serve this Application on your local server on the `local.dataloop.ai` domain over HTTPS.
4. Open `console.dataloop.ai` and go to FaaS/Application Hub. Go to the `Developer` tab and click on `Add Function`.
5. Fill out the form and choose the type of your Panel (e.g. Item Viewer).
6. Go to the screen where your Panel is used and trigger your Panel to test the Application.
7. Use the Browser console and Network tab to debug the Application.


## Example

As a part of this tutorial, we will be creating and testing a react-based "Image Item Viewer" Application and serving it using an Apache server. Through this Application, you can view an image in a react Application. Although, Dataloop runs on Micro-frontend architecture so you can write your Application on any framework of your choice. For this tutorial, we will be writing a React-based Application.

### Prerequisites
To be able to follow this execrice, you need th have the following prerequisites installed:
- [Install Node.js](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04) for running the react based application.
- [install Apache server](https://ubuntu.com/tutorials/install-and-configure-apache#2-installing-apache) for serving your build on ports 80 and 443. You can use Nginx, Node.js, Python, etc based servers as well.

### Create a React Application:

1. Initiatialise a react-based Application.
    ```
    npx create-react-app image-viewer
    ```
2. Move to the react app folder.
    ```
    cd image-viewer
    ```
3. Change the `App.js` file to render anything you want in your react Application. If you just want to show an image in your React Application, do the following:



```
import './App.css';
import { useEffect, useState } from 'react';

function App() {
  const [ img, setImage ] = useState('');
  const [ width, setWidth ] = useState(0);
  const [ height, setHeight ] = useState(0);

  const handleFetch = async () => {
    const item = await window.dl.items.get()
    const stream = await window.dl.items.stream(item.stream)
    const width = item.metadata?.system.width
    const height = item.metadata?.system.height;
    setHeight(height)
    setWidth(width)
    setImage(stream)
  }

  useEffect(() => {
   const init = async function() {
    await window.dl.init()
    await window.dl.on('ready', async () => {
        console.log('ready')
        await handleFetch()
    })
  }
  init()
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>
          Hello World
        </h1>
        <div>
          <img alt="item" src={img} height={height} width={width}>
          </img>
        </div>
      </header>
    </div>
  );
}

export default App;
```



4. (Optional) If you want to use the [JD SDK](https://dtlpy-documentation.redoc.ly/resources/dtljs/) of Dataloop, you can include it as an external script in your main `index.html` file located in the public folder. Keep it in the HEAD of the HTML.

```
<script src="https://console.dataloop.ai/dlAppLib.js"></script>
```

The `dl` object should now be globally available through the window object, (i.e. `window.dl`). You can do a lot of stuff on all the Dataloop entities using `dl`. For using typescript please [see below](#typescript).

### Create a host
If you want to create a host, you nee to:
1. Open /etc/hosts folder:
    ```
    sudo vi /etc/hosts
    ```
2. Register the domain by adding the following lines:
    ```
    127.0.0.1 local.dataloop.ai
    ```


### Generate SSL certificate

We need to serve this Application on HTTPS, so use [OPENSSL](https://www.ibm.com/docs/en/api-connect/2018.x?topic=overview-generating-self-signed-certificate-using-openssl) to create an SSL certificate on your local machine.

    ```
    openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
    ```

Now, you can choose any option to serve your Application over HTTPS. We have mentioned two ways here. One is using `create-react-app` and other is to use Apache.


### CREATE-REACT-APP

There are various ways to enable HTTPS in the [create-react-app’s local build](https://create-react-app.dev/docs/using-https-in-development/#linux-macos-bash-1).

- Open `package.json`.
- Locale scripts section and start command there.
- Rewrite the start command, using:
```
“start”: “HTTPS=true SSL_CRT_FILE=cert.pem SSL_KEY_FILE=key.pem react-scripts start”
```
**Note:** Make sure the path of the file `cert.pem` and `key.pem` is correct.

Now, your application would be running on the default port 3000 on the following host:
```
https://local.dataloop.ai:3000
```

### APACHE SETUP
If you want to use Apache, you need to set it up first, as follows:

1. After creating your Application, you should create a React build and move it to the `/var/www/html/image-viewer` folder for the Apache server to access it.

2. Open the file file `000-default.conf` using:

```
sudo vi /etc/hosts/sites-available/000-default.conf
```

3. Make changes to the file:

```
DocumentRoot /var/www/html ====> DocumentRoot /var/www/html/image-viewer
```


4. Move the `cert.pem` and `key.pem` files to the respective folders `/etc/ssl/certs/` and `/etc/ssl/private/`.

```
mv cert.pem /etc/ssl/certs/cert.pem
mv key.pem /etc/ssl/private/key.pem
```

5. Go to the sites-available folder in the Application.
```
cd /etc/apache2/sites-available
```


6. Open the `default-ssl.conf` file and make the following changes:
    - To the filename of the SSL certificate and private key as follows:
        ```
            SSLCertificateFile /etc/ssl/certs/cert.pem
            SSLCertificateKeyFile /etc/ssl/private/key.pem
        ```

    - To the `DocumentRoot` folder:
        ```
        DocumentRoot /var/www/html ====> DocumentRoot /var/www/html/image-viewer
        ```

7. Enable this site:
```
sudo a2ensite default-ssl.conf
```

8. Enable SSL in apache:
```
sudo a2enmod ssl
```

9. Restart Apache:
```
sudo service apache2 restart
```

10. Open `https://local.dataloop.ai`.

Your react app should be running here.

### Test the Application locally

Before deploying your Application, you want to quickly test it. For that reason, we have the debug Application feature, which allows you to run your Application locally, test it on the platform, and see the changes immediately as they happen.

You will need two files: `dataloop.json` and `app.json`. These files define the meta configuration of your Application and let the Dataloop OS know what to expect from your Application.

The base route of your application should serve these files. For example if your base route is `local.dataloop.ai` then the dataloop.json file should be available at GET `https://local.dataloop.ai/dataloop.json` location.

**Note**: Currently, there is no validation of the JSON file, it doesn’t affect the operation of the Application.

**Note:** Update the above line when the validation is done.

Below you can see some examples of basic `app.json` and `dataloop.json` (click them to expand):

<details>
    <summary>app.json</summary>

```
{

  "components": {

    "panels": [

      {

        "name": "preview-modality",

        "minRole": "annotator",

        "supportedSlots": [

          {

            "type": "itemSidePanel",

            "configuration": {

              "route": []

            }

          }

        ],

        "conditions": {

          "resources": []

        },

        "icon": "icon-dl-sdk-documentation",

        "metadata": {},

        "defaultSettings": {

        }

      }

    ]

  }

}
```

</details>



<details>
    <summary>dataloop.json</summary>

```
{
    "name": "item-viewer",
    "description": "Dataloop's image zoom viewer",
    "categories": [
        "viewer"
    ],
    "icon": "",
    "scope": "project",
    "components": {
        "panels": [
            {
                "name": "zoom-item-viewer",
                "supportedSlots": [
                    {
                        "type": "itemViewer",
                        "configuration": {
                            "layout": {
                                "leftBar": false,
                                "rightBar": false,
                                "bottomBar": false
                            },
                            "route": [ "/index.html" ]
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

</details>

To run them on your own, you need to:
1. Open the [Dataloop platform](https://console.dataloop.ai/projects/) and locate the FaaS -> Application Hub on and go to the `Developer` Tab. See image below:
![image](https://user-images.githubusercontent.com/58508793/232050310-2dbdaa14-a767-487d-94f9-b230994ddb99.png)

2. Click the Add function button located at the top-left corner.

3. Name your Application, set the address to the appropriate URL (in our case it is `local.dataloop.ai`), and specify the required slot (we are testing for Item Viewer).

4. And now you are ready to run your Application. Locate an Item in a sample Dataset and right-click on it. Click the `Open With` option and Click on your application name. You would be able to see the text `Hello World` on the Item if you used the given `App.js` file.

**Note:** For any troubleshooting, you can see the browser console and network tab that will help you fix any issues you see regarding your Application.


### <a name="typescript"> Using Typescript </a> :

Add the following lines to the `main.ts` file:

```
declare global {

    interface Window {

        dl: any

        XFrameManager: any

        GuestAgent: any

    }

}
```

### FAQ section:

Q. Why do we need the domain to be `local.dataloop.ai` to test the Application locally?
A: Dataloop AI platform needs to pass cookies to the guest Application in order to authenticate the Application and provide it access to the SDK backend.

Q. Why do we need HTTPS for running the Application locally?
A: Dataloop AI platform runs on HTTPS and it tries to access your `dataloop.json` file. If the local server is serving over HTTP and not on HTTPS, the [Mixed-Content Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content#loading_locally_delivered_mixed-resources) of most of the browsers won't allow the HTTP request for this `dataloop.json` file.





