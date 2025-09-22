#!/bin/bash

# Script to move all scripts in the current directory to ~/bin and make them executable

TARGET_DIR="$HOME/bin"

# Ensure the ~/bin directory exists
mkdir -p "$TARGET_DIR"

# Find all scripts in the current directory
for script in *.sh *.py; do
  if [ -f "$script" ]; then
    # Move the script to ~/bin
    cp "$script" "$TARGET_DIR/"

    # Make the script executable
    chmod +x "$TARGET_DIR/$(basename "$script")"

    echo "Moved and made executable: $script"
  fi
done

# Add ~/bin to PATH if not already present
if ! echo "$PATH" | grep -q "$HOME/bin"; then
  SHELL_CONFIG="$HOME/.zshrc"  # Change this to .bashrc if using bash
  echo "export PATH=\"$HOME/bin:$PATH\"" >> "$SHELL_CONFIG"
  echo "Added ~/bin to PATH in $SHELL_CONFIG. Please run 'source $SHELL_CONFIG' to apply changes."
else
  echo "~/bin is already in PATH."
fi

echo "All scripts have been moved to ~/bin and made executable."