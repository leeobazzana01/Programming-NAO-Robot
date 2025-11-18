# Programming the NAO Robot

This Repo contains all the codes to programming NAO Robot using the Software Choregraphe.

## Quick Choregraphe Installation Guide

### Step 1: Download Choregraphe
1. Go to Softbank Robotics Developer Center

2. Create an account or log in

3. Navigate to "Downloads" section

4. Download Choregraphe 2.8.x for your operating system (Windows/macOS)

### Step 2: Install Choregraphe
1. Windows:

Run the downloaded .exe file

Follow the installation wizard

Accept license agreement

Choose installation directory

2. macOS:

Open the downloaded .dmg file

Drag Choregraphe to Applications folder

Launch from Applications

### Step 3: Initial Setup
1. Launch Choregraphe

Connect to your NAO robot:

Click "Connect" button

Enter robot's IP address

Default port: 9559

Test connection with "Say" box

### Step 4: Configure Python SDK (Optional)

bash
#### Install NAOqi Python SDK
pip install path/to/naoqi-python-sdk.zip

### Step 5: Verify Installation
1. Create a new project

2. Drag a "Say" box to the diagram

3. Enter text and press "Play"

4. Robot should speak the text

### Troubleshooting
Connection issues: Check robot and computer are on same network

Firewall: Allow Choregraphe through firewall

Python path: Set correct Python interpreter in Preferences

Your NAO robot is now ready for programming!

## MODULE ORGANIZATION

**1. Core Modules**

Contains all the basic movements, postures, dances, etc...

**2. Vision Modules**

Contains the face detection, object tracking, color detection, and other codes.

**3. Audio Modules**

Here we have the audio modules, testing speech recognition, syntheses, sound processing and audio effects.

**4. Complex Behaviors**

We've the codes used to testing greeting, navigation, interactive demonstration, educational routines, and others.


