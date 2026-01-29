# 🤖 Microsoft Teams Meeting Automation

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![MS Teams](https://img.shields.io/badge/Microsoft_Teams-Automation-6264A7?style=for-the-badge&logo=microsoftteams&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

*Automated attendance system for Microsoft Teams meetings with intelligent scheduling*

[⚡ Quick Start](#-quick-start) • [⚙️ Configuration](#️-configuration) • [📖 Usage](#-usage) • [⚠️ Disclaimer](#️-disclaimer)

</div>

---

## ⚠️ Disclaimer

**Important Legal & Ethical Notice**:

This tool is designed for **legitimate educational purposes** and personal time management. Users must:
- ✅ Have permission to automate their meeting attendance
- ✅ Use only with their own accounts
- ✅ Comply with institutional/organizational policies
- ✅ Respect meeting privacy and attendance requirements
- ❌ **NOT** use for fraudulent attendance
- ❌ **NOT** violate academic integrity policies

**The developer assumes NO responsibility for misuse. Use at your own risk.**

---

## 📖 Overview

MT Meeting Automation is an intelligent Python-based tool that automates Microsoft Teams meeting attendance. Perfect for managing multiple recurring meetings with complex schedules. The tool uses Selenium WebDriver to interact with Teams web interface and provides scheduled join/leave functionality.

## ✨ Features

- 🕐 **Smart Scheduling**: Join and leave meetings at precise times
- 📝 **INI Configuration**: Simple configuration file for easy setup
- 📊 **Detailed Logging**: Complete activity logs for troubleshooting
- 🌐 **Chrome Integration**: Automated browser handling with custom options
- 🔕 **Notification Management**: Automatic popup and permission handling
- 🎯 **Test Mode**: Instant join for testing configuration
- 👤 **Identity Management**: Automatic name entry for meetings

## 🚀 Quick Start

### Prerequisites

- **Python 3.6+** installed
- **Google Chrome** browser
- Active **Microsoft Teams** account
- Meeting link(s) to join

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/MT-meeting-automate.git
   cd MT-meeting-automate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
## ⚙️ Configuration

### config.ini Setup

The tool's behavior is controlled via `config.ini`. Create this file in the project root:

```ini
[Account]
name = Eren
surname = Akkoç

[Times]
enter_times = 09.00, 10.30, 12.00, 13.30
exit_times = 10.20, 11.50, 13.20, 14.50

[Settings]
tryNow = False

[Lesson]
link = "https://teams.microsoft.com/l/meetup-join/19%3ameeting_..."
```

### Configuration Parameters

#### 📋 Account Section
| Parameter | Description | Example |
|-----------|-------------|---------|
| `name` | Your first name (displayed in Teams) | `Eren` |
| `surname` | Your last name | `Akkoç` |

#### ⏰ Times Section
| Parameter | Description | Format |
|-----------|-------------|--------|
| `enter_times` | Join meeting times | `HH.MM` (comma-separated) |
| `exit_times` | Leave meeting times | `HH.MM` (comma-separated) |

**Example Schedule**:
```ini
enter_times = 08.00, 09.30, 11.00, 13.00
exit_times = 08.50, 10.20, 11.50, 13.50
```

#### ⚙️ Settings Section
| Parameter | Description | Values |
|-----------|-------------|--------|
| `tryNow` | Test mode - join immediately | `True` / `False` |

**Use Cases**:
- `tryNow = True` → Instant join for testing
- `tryNow = False` → Scheduled operation (production)

#### 🔗 Lesson Section
| Parameter | Description | Example |
|-----------|-------------|---------|
| `link` | Microsoft Teams meeting URL | Full meeting link |

**Getting Meeting Link**:
1. Open Teams meeting invitation
2. Click **"Join Microsoft Teams Meeting"**
3. Copy the full URL
4. Paste into config.ini (keep quotes)ul>
      <li><code>name</code>: Your first name.</li>
      <li><code>surname</code>: Your surname.</li>
    </ul>
  </li>
  <li><strong>Times:</strong>
    <ul>
      <li><code>enter_times</code>: Comma-separated list of times (HH.MM format) to join meetings.</li>
      <li><code>exit_times</code>: Comma-separated list of times (HH.MM format) to leave meetings.</li>
    </ul>
  </li>
  <li><strong>Settings:</strong>
    <ul>
      <li><code>tryNow</code>: Set to <code>True</code> to join the meeting immediately after starting the program for testing purposes.</li>
    </ul>
  </li>
  <li><strong>Lesson:</strong>
    <ul>
      <li><code>link</code>: The URL of the Microsoft Teams meeting to join.</li>
    </ul>
  </li>
</ul>

## 📖 Usage

### Running the Automation

```bash
# Start the automation
python main.py
```

The tool will:
1. ✅ Read configuration from `config.ini`
2. ✅ Initialize Chrome WebDriver
3. ✅ Monitor system time
4. ✅ Join meetings at `enter_times`
5. ✅ Leave meetings at `exit_times`

### Test Mode

To test your configuration immediately:

```ini
[Settings]
tryNow = True
```

Then run:
```bash
python main.py
```

The tool will join the meeting instantly without waiting for scheduled time.

### Production Mode

For scheduled operation:

```ini
[Settings]
tryNow = False
```

The tool will wait until scheduled times to join/leave meetings.

### Logging

All activities are logged to `logs/automation_log.log`:

```
2024-01-15 09:00:00 - INFO - Joining meeting...
2024-01-15 09:00:15 - INFO - Successfully joined meeting
2024-01-15 10:20:00 - INFO - Leaving meeting...
2024-01-15 10:20:05 - INFO - Successfully left meeting
```

**Log Features**:
- 📝 Timestamped entries
- 🔍 Detailed action tracking
- ⚠️ Error reporting
- 📊 Session statistics

## 🏗️ Project Structure

```
MT-meeting-automate/
├── main.py                  # Main automation script
├── config.ini              # Configuration file
├── requirements.txt        # Python dependencies
├── README.md              # This documentation
├── LICENSE                # MIT License
└── logs/                  # Log directory
    └── automation_log.log # Activity logs
```

## 🔧 Code Overview

### AutoEnter Class

The main automation class with key methods:

#### `readConfig()`
Reads and parses `config.ini` file:
```python
config = configparser.ConfigParser()
config.read('config.ini')
name = config['Account']['name']
times = config['Times']['enter_times'].split(',')
```

#### `setDriver()`
Configures Chrome WebDriver with automation-friendly options:
```python
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-notifications")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
```

#### `enterLesson()`
Joins Microsoft Teams meeting:
```python
def enterLesson(self):
    self.driver.get(self.meeting_link)
    # Enter name
    # Click join button
    # Handle permissions
```

#### `exitLesson()`
Leaves the current meeting:
```python
def exitLesson(self):
    # Click leave button
    # Confirm exit
    # Close browser
```

#### `main()`
Main loop - monitors time and triggers actions:
```python
def main(self):
    while True:
        current_time = datetime.now().strftime("%H.%M")
        if current_time in self.enter_times:
            self.enterLesson()
        elif current_time in self.exit_times:
            self.exitLesson()
        time.sleep(30)  # Check every 30 seconds
```

## 🐛 Troubleshooting

### Common Issues

#### Chrome Driver Not Found
```bash
# Solution: Update webdriver-manager
pip install --upgrade webdriver-manager
```

#### Meeting Link Invalid
```
Error: Unable to navigate to meeting
Solution: 
1. Check meeting link format
2. Ensure link is within quotes in config.ini
3. Verify meeting hasn't expired
```

#### Selenium Timeout Errors
```python
# Increase wait times in main.py
from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(driver, 20)  # Increase from 10 to 20
```

#### Browser Opens But Doesn't Join
```
Possible causes:
1. Teams web interface changed (update selectors)
2. Network connectivity issues
3. Account authentication required
```

#### Permission Popups Blocking Automation
```python
# Add to Chrome options in setDriver()
options.add_argument("--use-fake-ui-for-media-stream")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1
})
```

### Debug Mode

Enable detailed logging:

```python
# In main.py, add:
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Changed from INFO
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

## ⚡ Advanced Usage

### Multiple Meeting Links

For different meetings on different days:

```python
# Create multiple config files
config_monday.ini
config_tuesday.ini

# Run with specific config
python main.py --config config_monday.ini
```

### Headless Mode

Run without visible browser:

```python
# In setDriver() method, add:
options.add_argument("--headless")
options.add_argument("--disable-gpu")
```

### Auto-Start on Boot

#### Windows (Task Scheduler)
```batch
# Create startup.bat
@echo off
cd C:\path\to\MT-meeting-automate
python main.py
```

#### macOS/Linux (cron)
```bash
# Add to crontab
@reboot cd /path/to/MT-meeting-automate && python3 main.py
```

## 🔒 Security Best Practices

- 🔐 **Never commit** `config.ini` to public repositories
- 🗝️ Keep meeting links private
- 🛡️ Use `.gitignore` for sensitive files:
  ```gitignore
  config.ini
  *.log
  logs/
  ```
- 🔄 Regularly update dependencies
- 🚫 Don't share your automation setup

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### How to Contribute

1. **Fork the repository**
2. **Create feature branch**:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit changes**:
   ```bash
   git commit -m 'Add AmazingFeature'
   ```
4. **Push to branch**:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open Pull Request**

### Feature Ideas

- 📧 Email notifications for join/leave events
- 🌐 Web dashboard for schedule management
- 📱 Mobile app companion
- 🔔 Discord/Slack integration
- 📊 Attendance statistics
- 🎤 Audio/video control options
- 📅 Calendar integration (Google/Outlook)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Eren Akkoç

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

## 👤 Author

**Eren Akkoç**
- 🌐 GitHub: [@ernakkc](https://github.com/ernakkc)
- 📧 Email: ern.akkc@gmail.com
- 💼 LinkedIn: [Eren Akkoç](https://linkedin.com/in/erenakkoc)

## 🙏 Acknowledgments

- **Selenium Project** - Web automation framework
- **WebDriver Manager** - Automatic driver management
- **Microsoft Teams** - Meeting platform
- **Python Community** - Continuous support

---

<div align="center">

**🤖 Automate Your Meeting Attendance! ⏰**

*Remember: Use responsibly and ethically!*

[![GitHub stars](https://img.shields.io/github/stars/ernakkc/MT-meeting-automate?style=social)](https://github.com/ernakkc/MT-meeting-automate)
[![GitHub forks](https://img.shields.io/github/forks/ernakkc/MT-meeting-automate?style=social)](https://github.com/ernakkc/MT-meeting-automate/fork)

**⚠️ This tool is for legitimate use only. Always comply with your institution's policies. ⚠️**

</div>
