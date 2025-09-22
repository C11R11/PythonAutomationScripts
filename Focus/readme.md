# Python Automation Scripts

## Setup or Modify Environment Variables
To centralize and manage environment variables:
1. Open your shell configuration file (e.g., `~/.zshrc` or `~/.bashrc`).
2. Add or modify environment variables as needed. For example:
   ```sh
   export MY_VARIABLE="my_value"
   export ANOTHER_VARIABLE="another_value"
   ```
3. Save the file and reload the shell configuration:
   ```sh
   source ~/.zshrc  # For zsh
   source ~/.bashrc # For bash
   ```

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