# Aplicação Distribuída

É uma aplicação tolerante a falhas e completamente transparente para o usuário.

Versão: Python 2

Sistema Operacional: Linux

Passos para executar a aplicação:

- Baixar e descompactar a pasta aplicacaodistribuida-master.zip, passar a pasta para sua pasta pessoal, ou outra pasta a sua escolha (nesse caso é preciso dar o comando cd seguido do nome da pasta para acessa-la pelo terminal) 
- Executar no terminal (Ctrl+Alt+Tab, ou botão direito do mouse) em diferentes máquinas (um .py por máquina) nessa sequência: mid.py, servername1.py e/ou servername2.py, server.py e cliente.py
- Como a aplicação vai executar em máquinas diferentes, será preciso alterar o IP (10.90 ...) dos componentes da aplicação (mid.py, servername1.py, etc) no código, para isso é preciso executar o comando ifconfig no terminal, que serve para descobrir o IP daquela máquina 
- Somente o cliente.py será usado para interagir com o sistema 
