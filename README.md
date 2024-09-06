# **MacIP: MAC and IP Address Management Tool**

## **Overview**

MacIP is a powerful command-line tool designed to manage and automate MAC and IP address changes on Linux-based systems. This tool is useful for network administrators, penetration testers, and cybersecurity professionals who require dynamic control over network interfaces for privacy, testing, and network management purposes.

MacIP offers six essential tools to manage your network interface, allowing you to change MAC and IP addresses manually or automatically. The tool is built with ease of use in mind and is compatible with most Linux distributions.

---

## **Features**

- **MAC Address Management**: Change or automate MAC address assignments on your network interfaces.
- **IP Address Management**: Modify or automate IP address assignments for greater control and privacy.
- **Combined MAC and IP Management**: Use a combination of MAC and IP address management for more complex use cases.
- **Automation**: Automate the process of changing MAC and IP addresses for network testing or enhanced privacy.
- **Simple Command Interface**: Easy-to-use command-line interface with clear options and commands.

---

## **Tools Available**

1. **MAC Address Change**: Manually change the MAC address on a specified network interface.
2. **Auto MAC Address Change**: Automatically change the MAC address without user input.
3. **IP Address Change**: Manually change the IP address of a specified network interface.
4. **Auto IP Address Change**: Automatically change the IP address without user input.
5. **MAC and IP Address Change**: Change both MAC and IP addresses simultaneously.
6. **Auto MAC and IP Address Change**: Automate the process of changing both MAC and IP addresses.

---
## Software Requirements:
The following OSs are officially supported:

- Debian 8+
- Kali Linux Rolling 2018.1+

The following OSs are likely able to run macip:

- Deepin 15+
- Fedora 22+
- Linux Mint
- Parrot Security
- Ubuntu 15.10+
- Void Linux

## Setup

### update and upgrade your system

```bash
apt update && apt upgrade -y
```
---

## **Installation**

### **Prerequisites**
- **Python 3.x** installed on your system.
- Required packages specified in the `requirements.txt` file.

### **Clone the Repository**
```bash
git clone https://github.com/anishalx/macip.git
cd macip
```
### **Install Dependencies**
```bash
pip install -r requirements.txt
```
### **Make the Script Executable**
```bash
chmod +x macip.sh
```

### **Run MacIP**
```bash
./macip.sh
```
### **Usage**
After running the tool, you will see a simple menu listing the available tools and commands. You can interact with the tool using the following commands:

### **Commands**
### **Commands**

- `exit`: Exit MacIP completely.
- `info`: Display information about a specific tool.
- `list`: List all available tools.
- `options`: Show the current MacIP configuration.
- `update`: Update MacIP to the latest version.
- `use #`: Use a specific tool by its number (e.g., `use 1` to manually change the MAC address).

### **Example Usage**

**Manually Change MAC Address:**

```bash
use 1
```
- Enter the network interface (e.g., wlan0, eth0).
- Enter the new MAC address.

**Automatically Change IP Address:**
```bash
use 4
```
- Enter the network interface.

### **Updating MacIP**
You can update MacIP directly from the command-line using the `update` command:
```bash
update
```
This command will pull the latest version of MacIP from the GitHub repository and update the local files.


### **Contribution Guidelines**
We welcome contributions from the community! If you would like to contribute, follow these steps:
1. **Fork the repository.**
2. **Create a new branch for your feature or bug fix.**
3. **Commit your changes and push them to your fork.**
4. **Create a pull request, and we will review your submission.**


### **License**

## License

This project is licensed under the [MIT License](./LICENSE). See the LICENSE file for more details.



### **Acknowledgments**
- Special thanks to all the contributors who helped build and improve this tool.
- The project is designed to support ethical usage in cybersecurity and networking tasks.

### **Contact**
For any questions, issues, or feature requests, feel free to open an issue on GitHub or contact me at - **<a href="mailto:anishalx7@gmail.com" class="btn">Email Me</a>**



