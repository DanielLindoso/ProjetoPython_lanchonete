#Projeto Python Faculdade
pedidos = []
preco = []
precoHamburguer = 25.00
precoBatata = 14.00
precoCoxinha = 8.00
precoRefri = 6.00
precoSuco = 9.00

#----------------------MENU---------------------------------------------------------------------------------
print("-----LANCHONETE-----")
print("----SEJA BEM VINDO(A)----")
while True:
    print("________MENU________")
    print("[1]--Ver cardápio.")
    print("[2]--Escolher Item.")
    print("[3]--Seus pedidos.")
    print("[4]--Remover Item.")
    print("[5]--Finalizar pedido.")
    print("[0]--Sair.")
    opcao = int(input("Escolha uma das opções acima: "))
    print("\n")
    print("\n")
    if opcao == 0:
        print("-----------Processo Finalizado-----------")
        break
    
#-----------------OPÇÃO DE VER CARDÁPIO [1]------------------------------------------------------------------
    if opcao == 1:
        print("______CARDÁPIO______")
        print("[1]-----Hamburguer Artesanal      --> R$25,00")
        print("[2]-----Batata frita Grande       --> R$14,00")
        print("[3]-----Coxinha de Frango         --> R$8,00")
        print("[4]-----Refrigerante Lata(350ml)  --> R$6,00")   
        print("[5]-----Suco Natural de Laranja   --> R$9,00") 
        voltar = int(input("Digite 0 para voltar ao menu: "))
        print("\n")
        print("\n")
        if voltar == 0:
            print("________MENU________")
            print("[1]--Ver cardápio.")
            print("[2]--Escolher Item.")
            print("[3]--Seus pedidos.")
            print("[4]--Remover Item.")
            print("[5]--Finalizar pedido.")
            print("[0]--Sair.")
            opcao = int(input("Escolha uma das opções acima: "))
            print("\n")
            print("\n")
            if opcao == 0:
                print("-----------Processo Finalizado-----------")
                break
#-------------------OPÇÃO ESCOLHER ITEM [2]------------------------------------------------------------------
    elif opcao == 2:
        print("--------Escolha o item que deseja--------")
        while True:
            print("[1]-----Hamburguer Artesanal")
            print("[2]-----Batata frita Grande")
            print("[3]-----Coxinha de Frango")
            print("[4]-----Refrigerante Lata(350ml")
            print("[5]-----Suco Natural de Laranja")
            escolha = int(input("Escolha os seus itens: "))
            if escolha == 1:
                pedidos.append("Hamburguer Artesanal")
                preco.append(25.00)
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("Pedido Registrado com sucesso!!!")
                continuar = input("Deseja pedir algo mais? (s/n): ")
                if continuar == "s":
                    print("\n")
                    print("\n")
                    continue
                else:
                    break
            elif escolha == 2:
                pedidos.append("Batata frita Grande")
                preco.append(14.00)
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("Pedido Registrado com sucesso!!!")
                continuar = input("Deseja pedir algo mais? (s/n): ")
                if continuar == "s":
                    print("\n")
                    print("\n")
                    continue
                else:
                    break
            elif escolha == 3:
                pedidos.append("Coxinha de Frango")
                preco.append(8.00)
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("Pedido Registrado com sucesso!!!")
                continuar = input("Deseja pedir algo mais? (s/n): ")
                if continuar == "s":
                    print("\n")
                    print("\n")
                    continue
                else:
                    break
            elif escolha == 4:
                pedidos.append("Refrigerante Lata(350ml)")
                preco.append(6.00)
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("Pedido Registrado com sucesso!!!")
                continuar = input("Deseja pedir algo mais? (s/n): ")
                if continuar == "s":
                    print("\n")
                    print("\n")
                    continue
                else:
                    break
            elif escolha == 5:
                pedidos.append("Suco Natural de Laranja")
                preco.append(9.00)
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("Pedido Registrado com sucesso!!!")
                continuar = input("Deseja pedir algo mais? (s/n): ")
                if continuar == "s":
                    print("\n")
                    print("\n")
                    continue
                else:
                    break
            print("________MENU________")
            print("[1]--Ver cardápio.")
            print("[2]--Escolher Item.")
            print("[3]--Seus pedidos.")
            print("[4]--Remover Item.")
            print("[5]--Finalizar pedido.")
            print("[0]--Sair.")
            opcao = int(input("Escolha uma das opções acima: "))
            print("\n")
            print("\n")
            if opcao == 0:
                print("-----------Processo Finalizado-----------")
                break


#-------------------------OPÇÃO SEUS PEDIDOS [3]----------------------------------------------------------------------

    elif opcao == 3:
        len(pedidos)
        if len(pedidos) == 0:
            print("\n")
            print("\n")
            print("Você ainda não fez nenhum pedido!")
            voltar = input("Aperte enter para voltar ao menu: ")
         
        else:
            print("\n")
            print("\n")
            for i, item in enumerate(pedidos, start=1):
                print(f"{i} -> {item}")
            voltar = input("Aperte enter para voltar ao menu: ")


#---------------------------OPÇÃO REMOVER ITEM [4]----------------------------------------------------------------
           

    elif opcao == 4:
        while True:
            print("--------Escolha o item que deseja remover--------")
            print("\n")
            for i, item in enumerate(pedidos, start=1):
                print(f"{i} -> {item}")
            numero = int(input("Digite o número do item que deseja remover: "))
            removerP = pedidos.pop(numero - 1)
            removerV = preco.pop(numero - 1)
            print("------Item removido com sucesso!!!------")
            continuar = input("Deseja remover mais algum item? (s/n): ")
            if continuar == "s":
                continue
            else:
                break


#---------------------------OPÇÃO FINALIZAR PEDIDO [5]---------------------------------------------------------


    elif opcao == 5:
        if len(pedidos) == 0:
            print("\n")
            print("\n")
            print("\n")
            print("Você ainda não fez nenhum pedido!!!")
            novo_pedido = input("Deseja fazer um pedido? (s/n): ")
            if novo_pedido == "s":
                print("\n")
                print("\n")
                continue
            else:
                print("\n")
                print("\n")
                break
        else:
            print("\n")
            print("\n")
            print("------------Valor Total do pedido------------")  
            for i, item in enumerate(pedidos):
                preco_item = preco[i]
                print(f"{i + 1} -> {item} ---> R${preco_item}0")     
            sum(preco)
            print(f"O valor total do pedido é R${sum(preco)}0") 
            print("\n")
            print("_____FORMAS DE PAGAMENTO_____")
            print("[1] -- Pix")
            print("[2] -- Cartão(Débito)")
            print("[3] -- Cartão(Crédito à vista)")
            print("[4] -- Dinheiro")
            pagamento = int(input("Escolha a opção [] de pagamento: "))
            print("**********PAGAMENTO REALIZADO COM SUCESSO**********")
    


            print("APROVEITE O LANCHE")
            novo_pedido = input("Deseja fazer outro pedido? (s/n): ")
            if novo_pedido == "s":
                print("\n")
                print("\n")
                continue
            else:
                print("\n")
                print("\n")
                break


        
        
            

            

        