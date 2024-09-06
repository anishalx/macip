#!/bin/bash

# Define a banner function
display_banner() {
  clear
  # Define color codes
  ORANGE='\033[38;5;208m'  # Orange color in 256-color mode
  RESET='\033[0m'          # Reset to default color

  # Function to print the banner with shadow effect
  print_banner() {
      echo -e "${ORANGE}                                                                  ${RESET}"
      echo -e "${ORANGE}                     ███╗   ███╗ █████╗  ██████╗██╗██████╗ ${RESET}"
      echo -e "${ORANGE}                     ████╗ ████║██╔══██╗██╔════╝██║██╔══██╗${RESET}"
      echo -e "${ORANGE}                     ██╔████╔██║███████║██║     ██║██████╔╝${RESET}"
      echo -e "${ORANGE}                     ██║╚██╔╝██║██╔══██║██║     ██║██╔═══╝ ${RESET}"
      echo -e "${ORANGE}                     ██║ ╚═╝ ██║██║  ██║╚██████╗██║██║    ${RESET}" 
      echo -e "${ORANGE}                                                       ${RESET}"
      echo -e "${ORANGE}         =============================================================${RESET}"
      echo -e "                     𝕍𝕖𝕣𝕤𝕚𝕠𝕟 : 2.0     𝕋𝕨𝕚𝕥𝕥𝕖𝕣 : anishalx7          "
      echo -e "${ORANGE}         =============================================================${RESET}"
  }

  # Print the banner
  print_banner

  # Add a line of text below the banner
  echo -e "${ORANGE}  START YOUR ANONYMOUS LIFE ...${RESET}"
  echo -e "${ORANGE}  [+] NOTE: Auto IP address change in every 5 minutes will be coming soon [+]
  ${RESET}"
}

# Call the banner function
display_banner

# Define the names of the Python tools
TOOLS=(
  "[+] MAC address change [+]"                 # 01_mac_changer.py
  "[+] auto MAC address change [+]"            # 02_auto_mac_changer.py
  "[+] IP address change [+]"                  # 03_ip_changer.py
  "[+] auto IP address change [+]"             # 04_auto_ip_changer.py
  "[+] MAC address and IP address change [+]"  # 05_macip_changer.py
  "[+] auto MAC address and IP address change [+]" # 06_auto_macip_changer.py
)

# Define the Python files corresponding to the tool names
FILES=(
  "tools/01_mac_changer.py"
  "tools/02_auto_mac_changer.py"
  "tools/03_ip_changer.py"
  "tools/04_auto_ip_changer.py"
  "tools/05_macip_changer.py"
  "tools/06_auto_macip_changer.py"
)

# Function to show the main menu
main_menu() {
  # Move cursor to row 12 (or adjust as needed) to ensure it starts below the banner
  tput cup 12 0
  echo "Main Menu"
  echo ""
  echo "  ${#TOOLS[@]} tools loaded"
  echo ""
  echo "Available Tools:"
  for i in "${!TOOLS[@]}"; do
    printf "  %d) %s\n" $((i+1)) "${TOOLS[$i]}"
  done
  echo ""
  echo "Available Commands:"
  echo "  exit      Completely exit MacIP"
  echo "  info #    Information on a specific tool"
  echo "  list      List available tools"
  echo "  options   Show MacIP configuration"
  echo "  update    Update MacIP"
  echo "  use #     Use a specific tool by its number"
  echo ""
  read -p "Enter command: " command args
}

# Function to display information about a specific tool
tool_info() {
  if [[ -z "$args" ]]; then
    echo "Usage: info <tool_number>"
    echo "Example: info 1"
    echo "This command provides information on a specific tool."
    return
  fi

  case $args in
    1)
      echo "[+] MAC address change [+]:"
      echo "This tool allows you to manually change the MAC address of your network interface."
      echo "Usage: Enter your network interface and new MAC address to spoof a new MAC."
      ;;
    2)
      echo "[+] auto MAC address change [+]:"
      echo "Automatically changes your MAC address to a random one at intervals."
      echo "Usage: Enter your network interface, and the tool will randomly select a new MAC address."
      ;;
    3)
      echo "[+] IP address change [+]:"
      echo "Manually change the IP address of your network interface."
      echo "Usage: Enter your network interface and new IP address to set."
      ;;
    4)
      echo "[+] auto IP address change [+]:"
      echo "Automatically changes your IP address to a random one at intervals."
      echo "Usage: Enter your network interface, and the tool will randomly assign a new IP address."
      ;;
    5)
      echo "[+] MAC address and IP address change [+]:"
      echo "Manually change both MAC and IP address of your network interface."
      echo "Usage: Enter your network interface, MAC address, and IP address."
      ;;
    6)
      echo "[+] auto MAC address and IP address change [+]:"
      echo "Automatically changes both your MAC and IP address at intervals."
      echo "Usage: Enter your network interface, and the tool will randomly assign new values for both."
      ;;
    *)
      echo "Invalid tool number. Please choose a valid tool number from the list."
      ;;
  esac
}

# Function to list available tools
list_tools() {
  echo "Available Tools:"
  for i in "${!TOOLS[@]}"; do
    printf "  %d) %s\n" $((i+1)) "${TOOLS[$i]}"
  done
}

# Function to show MacIP options
show_options() {
  echo "MacIP Configuration Options:"
  echo "  1) MAC address change:"
  echo "     - Allows you to change your MAC address manually."
  echo "  2) Auto MAC address change:"
  echo "     - Automatically assigns a random MAC address."
  echo "  3) IP address change:"
  echo "     - Change your IP address manually."
  echo "  4) Auto IP address change:"
  echo "     - Randomly assigns a new IP address at regular intervals."
  echo "  5) MAC and IP address change:"
  echo "     - Allows you to manually change both MAC and IP."
  echo "  6) Auto MAC and IP address change:"
  echo "     - Automatically assigns both new MAC and IP address at intervals."
}

# Function to run a specific tool
run_tool() {
  if [[ -z "$args" ]]; then
    echo "Usage: use <tool_number>"
    echo "Example: use 1"
    echo "Please specify the tool number to use. Type 'list' to see available tools."
    return
  fi

  if [[ "$args" =~ ^[0-9]+$ ]] && [[ "$args" -gt 0 && "$args" -le ${#TOOLS[@]} ]]; then
    tool_number=$args
    user_inputs=$(get_user_inputs "$tool_number")
    python3 "${FILES[$((tool_number-1))]}" $user_inputs || {
      echo "An error occurred while running the tool. Please check your inputs."
    }
  else
    echo "Invalid tool number. Please choose a valid tool number from the list."
  fi
}

# Function to prompt the user for additional inputs (interface, IP, or MAC address)
get_user_inputs() {
  local tool_number=$1
  local params=""

  if [[ "$tool_number" -eq 1 || "$tool_number" -eq 2 || "$tool_number" -eq 4 || "$tool_number" -eq 5 || "$tool_number" -eq 6 ]]; then
    read -p "Enter network interface (e.g., wlan0, eth0): " interface
    params="$params -i $interface"
  fi

  if [[ "$tool_number" -eq 1 || "$tool_number" -eq 5 ]]; then
    read -p "Enter MAC address (e.g., 00:11:22:33:44:55): " mac
    params="$params -m $mac"
  fi

  if [[ "$tool_number" -eq 3 || "$tool_number" -eq 5 ]]; then
    read -p "Enter IP address (e.g., 192.168.1.100): " ip
    params="$params -ip $ip"
  fi

  echo "$params"
}

# Function to update MacIP (placeholder for future implementation)
update_macip() {
  echo "Updating MacIP... (This is a placeholder for the actual update process.)"
}

# Main loop
while true; do
  main_menu
  case $command in
    exit)
      echo "Exiting MacIP."
      exit 0
      ;;
    info)
      tool_info
      ;;
    list)
      list_tools
      ;;
    options)
      show_options
      ;;
    update)
      update_macip
      ;;
    use)
      run_tool
      ;;
    *)
      echo "Invalid command. Please try again."
      ;;
  esac
  echo ""
  read -p "Press Enter to return to the main menu..."
done
