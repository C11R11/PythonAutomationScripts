# Python Automation Scripts

## Setup or Modify Environment Variables in `/etc/bash.bashrc`
To manage system-wide environment variables:
1. Open the `/etc/bash.bashrc` file with a text editor (requires root privileges):
   ```sh
   sudo nano /etc/bash.bashrc
   ```
2. Add or modify environment variables as needed. For example:
   ```sh
   export SYSTEM_VARIABLE="system_value"
   export ANOTHER_SYSTEM_VARIABLE="another_system_value"
   ```

   The base for the focus firewall is this
   ```sh
   export BLOCK_SITES="\
www.mercadolibre.cl \
www.instagram.com \
instagram.com \
www.youtube.com \
whatsapp.com \
whatsapp.net \
snr.whatsapp.net \
cdn.whatsapp.net \
wa.me \
www.falabella.com \
www.plazamusica.cl \
listado.mercadolibre.cl \
whatsappbrand.com"
   ```

3. Save the file and exit the editor (in `nano`, press `CTRL+O`, then `Enter`, and `CTRL+X`).
4. Reload the shell configuration to apply the changes:
   ```sh
   source /etc/bash.bashrc
   ```

These changes will apply to all users on the system.

## Move (Update) Scripts to `~/bin`
To make your scripts globally accessible:
1. Ensure the `~/bin` directory exists:
   ```sh
   mkdir -p ~/bin
   ```
2. Copy or move your scripts to `~/bin`:
   ```sh
   cp /path/to/your/script.py ~/bin/
   ```
3. Make the script executable:
   ```sh
   chmod +x ~/bin/script.py
   ```
4. Add `~/bin` to your `PATH` if it’s not already included. Add the following to your shell configuration file:
   ```sh
   export PATH="$HOME/bin:$PATH"
   ```
5. Reload the shell configuration:
   ```sh
   source ~/.zshrc  # For zsh
   source ~/.bashrc # For bash
   ```

Your scripts in `~/bin` can now be run from anywhere in the terminal by typing their name.