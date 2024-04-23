#!/bin/bash

# Ensure dialog is installed
command -v dialog >/dev/null 2>&1 || { echo >&2 "Dialog is required but not installed. Aborting."; exit 1; }

# Define dialog command options
DIALOG=${DIALOG=dialog}

# Main menu function
main_menu() {
    local choice
    while true; do
        choice=$($DIALOG --clear \
            --title "Main Menu" \
            --menu "Choose an option:" \
            15 40 5 \
            1 "Create Directory" \
            2 "Copy Files" \
            3 "Delete Files" \
            4 "Rename File" \
            5 "Option 5" \
            2>&1 >/dev/tty)

        case "$choice" in
            1) create_directory ;;
            2) copy_files ;;
            3) delete_files ;;
            4) rename_file ;;
            5) option_5 ;;
            *) exit ;;
        esac
    done
}

# Function to create directory
create_directory() {
    local dir_name
    dir_name=$($DIALOG --title "Create Directory" --inputbox "Enter directory name:" 10 30 2>&1 >/dev/tty)

    if [ -n "$dir_name" ]; then
        mkdir -p "$dir_name"
        if [ $? -eq 0 ]; then
            $DIALOG --title "Success" --msgbox "Directory '$dir_name' created successfully." 10 30
        else
            $DIALOG --title "Error" --msgbox "Failed to create directory." 10 30
        fi
    fi
}

# Function to copy files
copy_files() {
    local source_dir
    local dest_dir
    source_dir=$($DIALOG --title "Copy Files" --inputbox "Enter source directory:" 10 30 2>&1 >/dev/tty)
    dest_dir=$($DIALOG --title "Copy Files" --inputbox "Enter destination directory:" 10 30 2>&1 >/dev/tty)

    if [ -n "$source_dir" ] && [ -n "$dest_dir" ]; then
        cp -r "$source_dir"/* "$dest_dir"
        if [ $? -eq 0 ]; then
            $DIALOG --title "Success" --msgbox "Files copied successfully from '$source_dir' to '$dest_dir'." 10 30
        else
            $DIALOG --title "Error" --msgbox "Failed to copy files." 10 30
        fi
    fi
}

# Function to delete files
delete_files() {
    local dir
    dir=$($DIALOG --title "Delete Files" --inputbox "Enter directory to delete files from:" 10 30 2>&1 >/dev/tty)

    if [ -n "$dir" ]; then
        local files
        files=$($DIALOG --title "Delete Files" --inputbox "Enter file(s) to delete (separated by spaces):" 10 50 2>&1 >/dev/tty)
        
        if [ -n "$files" ]; then
            rm -f $dir/{$files}
            if [ $? -eq 0 ]; then
                $DIALOG --title "Success" --msgbox "Files deleted successfully from '$dir'." 10 30
            else
                $DIALOG --title "Error" --msgbox "Failed to delete files." 10 30
            fi
        fi
    fi
}

# Function to rename file
rename_file() {
    local dir
    local old_name
    local new_name
    dir=$($DIALOG --title "Rename File" --inputbox "Enter directory containing the file:" 10 30 2>&1 >/dev/tty)
    old_name=$($DIALOG --title "Rename File" --inputbox "Enter current name of the file:" 10 30 2>&1 >/dev/tty)
    new_name=$($DIALOG --title "Rename File" --inputbox "Enter new name of the file:" 10 30 2>&1 >/dev/tty)

    if [ -n "$dir" ] && [ -n "$old_name" ] && [ -n "$new_name" ]; then
        mv "$dir/$old_name" "$dir/$new_name"
        if [ $? -eq 0 ]; then
            $DIALOG --title "Success" --msgbox "File renamed successfully in '$dir'." 10 30
        else
            $DIALOG --title "Error" --msgbox "Failed to rename file." 10 30
        fi
    fi
}

# Option 5 function
option_5() {
    $DIALOG --title "Option 5" --msgbox "You chose Option 5." 10 30
}

# Execute main menu
main_menu
