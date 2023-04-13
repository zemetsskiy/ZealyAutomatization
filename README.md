# Getting Started (Windows OS)
Before you can use this program, you will need to have python3 installed on your computer. If you do not have it installed, you can download it from the [official website](https://www.python.org/downloads/).
I use 3.8.10 version, so u can do the same and download it [here](https://www.python.org/downloads/release/python-3810/). Scroll down and click a download link according to your OS version (32-bit or 64-bit).

Once you have Python installed, you can download this project from GitHub. To download, click on the green "Code" button on the repository page and select "Download ZIP."

After downloading and unzipping the project, you will need to install the required packages. To do so, follow these steps:

Open the command line.
Navigate to the directory where the project is located. For example, if the project is located in the Downloads folder, you would type `cd Downloads/project_name`. 
> U can copy folder absolute path (press shift and right click folder) and type `cd "absolute_path"`. Quotes are mandatory

Once you are in the project directory, type `pip install -r requirements.txt` and press Enter. This will install all the required packages for the program. 
After installing the required packages, you can launch the program by following these steps:

## Preparing config
### Preparing zealy tokens
Go to zealy.io and log in. Open dev tools: ctrl + shift + i. Go to console and paste this code: 
```
const cookies = document.cookie.split(';');
let accessToken = '';

cookies.forEach(cookie => {
  const cookieArray = cookie.split('=');
  const cookieName = cookieArray[0].trim();
  const cookieValue = cookieArray[1].trim();
  if (cookieName === 'access_token') {
    accessToken = cookieValue;
  }
});

console.log(accessToken);
```


### Next step
Move into project directory and find tokens.txt file.
Paste your tokens and proxies in the followind format: 
```
token1 proxy1
token2 proxy2
...
```

> u should paste your proxies in the following format: ip:port:username:password


# Start
Navigate to the directory where the project is located like u did it before.
Once you are in the project directory, type `python3 main.py` and press Enter.
