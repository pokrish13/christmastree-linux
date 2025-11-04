#!/bin/bash

echo "🎄 Installing Christmastree for Linux..."
echo ""

# Check if script exists
if [ ! -f "Christmastree" ]; then
    echo "❌ Error: Christmastree script not found in current directory"
    echo "   Please run this script from the directory containing Christmastree"
    exit 1
fi

# Copy to system bin directory
sudo cp Christmastree /usr/local/bin/

echo "✅ Installation complete!"
echo ""
echo "🎉 Now you can run: Christmastree"
echo "   To exit: Press Ctrl+C"
echo ""
echo "🌟 Spread holiday cheer! 🎅"
