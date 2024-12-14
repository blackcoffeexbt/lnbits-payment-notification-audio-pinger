# LNbits Payment Notification Audio Pinger

This is a Python script that plays an audible ping whenever an LNbits payment with a `status: success` is received via a Server-Sent Events (SSE) endpoint.

## Features
- Connects to the LNbits SSE endpoint.
- Detects successful payment events.
- Plays a `ping.mp3` sound file to notify the user.
- Automatically reconnects in case of network interruptions or server downtime.

## Prerequisites
- Python 3.11 or higher.
- An LNbits instance with a wallet and the readonly API key for the wallet.

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/blackcoffeexbt/lnbits-payment-notification-audio-pinger.git
cd lnbits-payment-notification-audio-pinger
```

### 2. Set Up a Virtual Environment
Create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # For Linux/MacOS
venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies
Install required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File
Create a `.env` file in the project directory with the following content:
```env
LNbits_HOST=<https://yourserver.com>
API_KEY=<your_api_key>
```
Replace `<your_api_key>` with your actual LNbits API key.

## Running the Script
Run the script directly:
```bash
python main.py
```

## Setting Up as a Linux Daemon
To run the script as a Linux daemon using `systemd`:

1. **Create a systemd Service File**
Create a new file called `/etc/systemd/system/lnbits-audio-notification.service`:
```ini
[Unit]
Description=LNbits Payment Audio Pinger
After=network.target

[Service]
User=<your_username>
WorkingDirectory=<path_to_project>
ExecStart=<path_to_project>/venv/bin/python <path_to_project>/sse_payment_listener.py
Restart=always

[Install]
WantedBy=multi-user.target
```
Replace `<your_username>` with your Linux username and `<path_to_project>` with the full path to your project directory.

2. **Reload systemd and Start the Service**
```bash
sudo systemctl daemon-reload
sudo systemctl start lnbits-audio-notification.service
sudo systemctl enable lnbits-audio-notification.service
```

3. **Check Service Status**
To check if the service is running:
```bash
sudo systemctl status lnbits-audio-notification.service
```

## License
This project is open-source and available under the MIT License.

## Acknowledgments
- [pygame](https://www.pygame.org/) for audio playback.
- [python-dotenv](https://pypi.org/project/python-dotenv/) for environment variable management.
- [sseclient](https://pypi.org/project/sseclient/) for SSE handling.

