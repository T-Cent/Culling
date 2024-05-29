<h1>Culling</h1>

<h2>Testing individual images</h2>

Clone the repository
--------
    git clone https://github.com/T-Cent/culling.git

In the terminal
--------

    >cd culling
    >powerhsell
    >pwsh.exe -ExecutionPolicy RemoteSigned
    >.\culling.ps1
*The third command is for when you are experiencing issues running the script as Microsoft does not allow you to run scripts by default as a safety precaution; here, I am changing the parameter for just this session. Hence, your setting would change to default when this season is terminated. You can learn more about execution policies here: 
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4* <br><br>
The script will now install `pipenv` and create a virtual environment to install `torch, torchvision, pillow, pygetwindow` <br>
It will then resize the terminal window and open images (**placed in the same folder as this repo, like the example image**) one by one with the predictions and ask you to verify them. <br>
In the end, you can choose to delete these files as they take up a lot of space. <br>
