#!/bin/bash

# 1. Create Directories in Home
echo "[+] Creating directories: Tools, Lab, Captures..."
mkdir -p ~/{Tools,Lab,Captures}

# 2. Update System
echo "[+] Updating system repositories..."
sudo apt update -y

# 3. Install Core Tools & SecLists
# We use 'apt' for seclists because it's optimized for Kali
echo "[+] Installing core packages and SecLists..."
sudo apt install -y seclists responder open-vm-tools-desktop fuse docker.io docker-compose wine git make

# Start and enable Docker
sudo systemctl enable --now docker

# 4. Install BloodHound Community Edition (Docker)
echo "[+] Setting up BloodHound CE..."
mkdir -p ~/Tools/BloodHound
cd ~/Tools/BloodHound
curl -L https://ghst.ly/getbhce > docker-compose.yml
sudo docker-compose up -d

# 5. Install Mythic C2
echo "[+] Setting up Mythic C2..."
cd ~/Tools
git clone https://github.com/its-a-feature/Mythic
cd Mythic
sudo make

# 6. Download Vulnserver for the Lab
echo "[+] Downloading Vulnserver to ~/Lab..."
cd ~/Lab
git clone https://github.com/stephenbradshaw/vulnserver.git

# 7. Download GhostPack Binaries
echo "[+] Downloading GhostPack Binaries to ~/Tools..."
cd ~/Tools
git clone https://github.com/r3motecontrol/Ghostpack-CompiledBinaries.git

# Final cleanup/info
echo "-------------------------------------------------------"
echo "[!] INSTALLATION COMPLETE"
echo "Directories: ~/Tools, ~/Lab, ~/Captures"
echo ""
echo "Tool Paths:"
echo " - SecLists: /usr/share/seclists"
echo " - Vulnserver: ~/Lab/vulnserver"
echo " - GhostPack: ~/Tools/Ghostpack-CompiledBinaries"
echo ""
echo "Services:"
echo " - BloodHound: http://localhost:8080"
echo " - Mythic: https://localhost:7443"
echo ""
echo "[*] PLEASE REBOOT NOW to enable VMware Tools features."
echo "-------------------------------------------------------"
