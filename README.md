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

![image](https://user-images.githubusercontent.com/68808330/231740100-4b167c26-29e2-4949-a8c1-bfa4afe39dbe.png)


### 1. Claim
Here u can see a set of functions: u can claim all quests at once, or use each function separately and claim quests by blocks:
![image](https://user-images.githubusercontent.com/68808330/231740347-1301a097-27df-4e67-87f0-de94be0b3467.png)
> 4. Claim Special Gift and 6. Claim Invites are disabled now due to the fact that I havent reached the required levels (4. Claim Special Gift requires 11 lvl) on any of my accounts that are required to complete quests, and I havent invited enough people through my referral link (6. Claim Invites), so I simply cannot collect the necessary data to submit a request
> I do not recommend to use Claim all function - zealy.io has a limit on the number of requests within a certain time period, so you may lose the ability to claim any quest for 10 minutes.

#### ex
You can find almsot all info about your claiming success in logs, lets see. So I have chosen `1. Claim` and `11. Claim Suiswap Friend Follow`: 
Zealy.io sends the same code response in the response request if u have either already claimed the quest or have not met the quest conditions, and you simply cannot claim it. Since these things cannot be distinguished, something from the above mentioned applies to you - you will see STATUS CODE 400.
![image](https://user-images.githubusercontent.com/68808330/231760623-8d956e72-0c2e-40d6-a988-eddea91e9389.png)


On the contrary, if everything is fine and you have met the quest conditions, you will see STATUS CODE 200 in the log

![image](https://user-images.githubusercontent.com/68808330/231762125-4b1e3350-46fa-4169-9c1c-e5fb70f2afb6.png)

> #e307 - first 4 digits of quest id. That will help u to identificate the quest u claimed or got problem with. If u click on the quest at zealy, u can find its id in the address bar. Some problems appeared wen i tried to put quest names to the logs, so i left it like this for now.

### 2. Show acoount xp
Iterates through all accounts and collects information about their level and amount of XP

![image](https://user-images.githubusercontent.com/68808330/231757008-aa38990a-dd4b-4c45-ab65-7f206ad6029e.png)



