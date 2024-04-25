#!/bin/bash

# Define opçoes do comando dialog
DIALOG=${DIALOG=dialog}

# Função para verificar password
verificar_password() {
    local password="123"  # MUDAR PASSWORD AQUI
    local password_introduzida

    password_introduzida=$($DIALOG --clear \
        --title "Necessita Password" \
        --passwordbox "Introduzir password:" 10 30 2>&1 >/dev/tty)

    if [ "$password_introduzida" != "$password" ]; then
        $DIALOG --clear \
            --title "Password Incorreta" \
            --msgbox "Password Incorreta. Saindo da Aplicação" 10 30
        exit 1
    fi
}

# Menu Principal
main_menu() {
    local escolha
    while true; do
        escolha=$($DIALOG --clear \
            --title "Menu Principal" \
            --menu "Escolher a ferramenta:" \
            15 40 5 \
            1 "Criar Diretoria" \
            2 "Copiar Ficheiros" \
            3 "Apagar Ficheiros" \
            4 "Renomear Ficheiros" \
            2>&1 >/dev/tty)

        case "$escolha" in
            1) criar_diretoria ;;
            2) copiar_ficheiros ;;
            3) apagar_pastas ;;
            4) renomear_ficheiro ;;
            *) exit ;;
        esac
    done
}

# Funcao para criar diretoria
criar_diretoria() {
    local dir_nome
    dir_nome=$($DIALOG --title "Criar Diretoria" --inputbox "Introduzir nome da diretoria:" 10 30 2>&1 >/dev/tty)

    if [ -n "$dir_nome" ]; then
        mkdir -p "$dir_nome"
        if [ $? -eq 0 ]; then
            $DIALOG --title "Sucesso!" --msgbox "Diretoria '$dir_nome' criada com sucesso." 10 30
        else
            $DIALOG --title "Erro!" --msgbox "Erro ao criar diretoria." 10 30
        fi
    fi
}

# Funcao para copiar ficheiros
copiar_ficheiros() {
    local base_dir
    local nova_dir
    base_dir=$($DIALOG --title "Copiar Ficheiros" --inputbox "Introduzir path da diretoria:" 10 30 2>&1 >/dev/tty)
    nova_dir=$($DIALOG --title "Copy Files" --inputbox "Introduzir o path da diretoria de destino:" 10 30 2>&1 >/dev/tty)

    if [ -n "$base_dir" ] && [ -n "$nova_dir" ]; then
        cp -r "$base_dir"/* "$nova_dir"
        if [ $? -eq 0 ]; then
            $DIALOG --title "Sucesso!" --msgbox "Ficheiros de '$base_dir' para '$nova_dir' foram compiados com sucesso." 10 30
        else
            $DIALOG --title "Erro!" --msgbox "Erro ao copiar os ficheiros." 10 30
        fi
    fi
}

# Funcao para apagar pastas
apagar_pastas() {
    local pasta
    pasta=$($DIALOG --title "Apagar Pastas" --inputbox "Introduzir nome da pasta:" 10 30 2>&1 >/dev/tty)

    if [ -n "$pasta" ]; then
        rm -rf "$pasta"
        if [ $? -eq 0 ]; then
            $DIALOG --title "Sucesso!" --msgbox "Pasta '$pasta' apagada com sucesso." 10 30
        else
            $DIALOG --title "Erro!" --msgbox "Falha ao apagar a pasta." 10 30
        fi
    fi
}

# funçao para renomear ficheiros
renomear_ficheiro() {
    local dir
    local nome_antigo
    local novo_nome
    dir=$($DIALOG --title "Renomear Ficheiro" --inputbox "Introduzir path da diretoria do ficheiro:" 10 30 2>&1 >/dev/tty)
    nome_antigo=$($DIALOG --title "Renomear Ficheiro" --inputbox "Introduzir nome atual do ficheiro:" 10 30 2>&1 >/dev/tty)
    novo_nome=$($DIALOG --title "Renomear Ficheiro" --inputbox "Introduzir novo nome do ficheiro:" 10 30 2>&1 >/dev/tty)

    if [ -n "$dir" ] && [ -n "$nome_antigo" ] && [ -n "$novo_nome" ]; then
        mv "$dir/$nome_antigo" "$dir/$novo_nome"
        if [ $? -eq 0 ]; then
            $DIALOG --title "Sucesso!" --msgbox "Ficheiro renomeado com sucesso em '$dir'." 10 30
        else
            $DIALOG --title "Erro!" --msgbox "Falha ao renomear o ficheiro." 10 30
        fi
    fi
}

# verificar password
verificar_password

# Execute main menu
main_menu