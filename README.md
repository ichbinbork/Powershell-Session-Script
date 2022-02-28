# Powershell-Session-Script
-It is a script written to extract suspicious logs from Powershell session logs.


-In order to use this script efficiently, the powershell transcription logging feature must be turned on.

-Script selects logs according to file size. Does not guarantee that the selected log file is malicious

## Why Should I Use This Script ?
-Powershell is widely used by attackers to perform Post-Exploitation operations. The most important reason for this is that Powershell is a part of the Windows operating system. Therefore, Powershell allows attackers to act as a normal user on the target system. An attacker using Powershell can run malicious commands on the operating system and bypass security measures by performing these operations with a user ID. In addition, Powershell allows attackers to use fileless malware, since operations performed through Powershell only run in memory.

## What is the Transcription Logging and How to Turn on ?

-This feature allows logging of all started and terminated Powershell sessions. If this feature is activated, the logs are saved in a specified text file. Each transaction is recorded with metadata to aid further analysis. Logging can be done by activating the Turn on PowerShell Transcription policy. Log files are saved under the directory specified with the "Transcript output directory" option. If no directory is specified, logs are saved under the user's "Documents" directory.



## How to Turn on Transcription Logging?
-Open cmd or PowerShell and type **gpedit.msc**. This will open the Group Policy Editor.
gpedit.msc
Navigate to **Computer Configuration – Administrative Templates – Windows Components –  Windows PowerShell** and double-klick “Turn on PowerShell Transcription”. Click on Enable and enter your prefered Output Directory.


![noname](https://user-images.githubusercontent.com/86713987/156067093-50201026-0ec9-4abc-8c49-bcbe9fbb9622.jpg)


## How can I Use This Script?
-First of all, as we talked about in the previous topic, we must turn on **Transcription Logging** and Make sure it's in the directory where the script is. Then open a powershell or cmd shell and type:
- `python main.py`

-In the second phase program is gonna ask you the location of the powershell session log files

![image](https://user-images.githubusercontent.com/86713987/156069238-5152d0b6-9fc5-4e69-98a5-c73fdee3c6e3.png)

-At this point, you should write the path entered in "Transcript output directory" as input.

-Then the program asks for the name of the new directory.

![image](https://user-images.githubusercontent.com/86713987/156071193-adfaa52c-1c3a-4246-8e4e-fbaf091822f7.png)

-The name of the new directory must not have been used in another directory before.


-Then you will see 

![image](https://user-images.githubusercontent.com/86713987/156071868-83074314-7a8c-46c3-9517-ca16a17503f8.png)

## Conclusion
-Now you can inspect the malicious powershell session logs in a single directory. It doesn't mean that all the files in the directory you just created will be malicious. These logs may have been created by a third-party software or operating system. 
