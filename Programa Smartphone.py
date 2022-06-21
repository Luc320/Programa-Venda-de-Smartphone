varSmartphones = {'SAMSUNG S11':1199.99,'MOTOROLA G8':1350.50,'IPHONE 12':3299.99}
varVendedores = {1:'Ayrton',2:'Emerson',3:'Nelson',4:'Rubens',5:'Felipe'}

laco = 0
cont = 0


ValorTotalVendas = 0
ValorTotalComissao = 0
ValorTotalVendaVista = 0

varContMarca1 = 0
varContMarca2 = 0
varContMarca3 = 0



print ("====================================================================")
print ("                            ATIVIDADE 2                             ")
print ("--------------------------------------------------------------------")


print ("David Felix - 740433")
print ("Jonathan Alves - 740090")
print ("Lucas Sasso - 740968")
print ("Yago Henrique - 740178")
print ("--------------------------------------------------------------------")

while (laco != 4):
    print ("====================================================================")
    print ("                          FECHAMENTO DO DIA - TELA INICIAL          ")
    print ("====================================================================")
    print ("1 - Samsung S11")
    print ("2 - MOTOROLA G8")
    print ("3 - IPHONE 12")
    print ("4 - Exibir totalização")
    print ("--------------------------------------------------------------------")

    laco = int (input("Digite sua escolha ...................:"))
    if (laco == 1):
        varCodigoVendedor = int(input("Digite o codigo do vendedor.............:"))
        if (varCodigoVendedor >= 1 and varCodigoVendedor <= 5):
            cont = cont + 1
            varContMarca1 = varContMarca1 + 1
            varFormaPagamento = input ("Pagamento [V] à vista ou [P] parcelado:").upper()
            print ("--------------------------------------------------------------------")
            
            if (varFormaPagamento == "V"):
                porcentagemDesconto = int(input("Porcentagem de desconto a vista :"))
                desconto = varSmartphones['SAMSUNG S11'] * (porcentagemDesconto / 100)
                ValorVenda = varSmartphones ['SAMSUNG S11'] - desconto
                ValorTotalVendaVista = ValorTotalVendaVista + ValorVenda
                print ("Preço base..........:R$", varSmartphones ['SAMSUNG S11'])
                print ("Desconto ..........:R${:.2f}". format (desconto))
                print ("Venda à vista ......:R${:.2f}". format (ValorVenda))
                            
            else:
                ValorVenda = varSmartphones ['SAMSUNG S11']
                ValorParcela = ValorVenda / 6
                print ("6 parcelas de R${0:.2f} totalizando R${1:.2f}". format (ValorParcela,ValorVenda))
            varComissaoVendedor = ValorVenda * (5/100)
            ValorTotalVendas = ValorTotalVendas + ValorVenda
            ValorTotalComissao = ValorTotalComissao + varComissaoVendedor
            print ("====================================================================")
            print ("*** VENDA REGISTRADA " "#" ,cont, " - SAMSUNG S11")
            print ("*** VENDEDOR {0:} - Comissão R${1:.2f}". format (varVendedores[varCodigoVendedor],varComissaoVendedor))
                
        else:
            print (" Código do vendedor ")
            print (" Venda não foi registrada ")

            continue
    if (laco == 2):
        varCodigoVendedor = int(input("Digite o codigo do vendedor.......:"))
        if (varCodigoVendedor >= 1 and varCodigoVendedor <= 5):
            cont = cont + 1
            varContMarca2 = varContMarca2 + 1
            varFormaPagamento = input ("Pagamento [V] à vista ou [P] parcelado:").upper()
            print ("--------------------------------------------------------------------")
            
            
            if (varFormaPagamento == "V"):
                porcentagemDesconto = int(input("Porcentagem de desconto a vista :"))
                desconto = varSmartphones['MOTOROLA G8'] * (porcentagemDesconto / 100)
                ValorVenda = varSmartphones ['MOTOROLA G8'] - desconto
                ValorTotalVendaVista = ValorTotalVendaVista + ValorVenda
                print ("Preço base.........:R$", varSmartphones ['MOTOROLA G8'])
                print ("Desconto ........:R${:.2f}". format (desconto))
                print ("Venda à vista ......: R${:.2f}". format (ValorVenda))
                            
            else:
                ValorVenda = varSmartphones ['MOTOROLA G8']
                ValorParcela = ValorVenda / 6
                print ("6 parcelas de R${0:.2f} totalizando R${1:.2f}". format (ValorParcela,ValorVenda))
            varComissaoVendedor = ValorVenda * (5/100)
            ValorTotalVendas = ValorTotalVendas + ValorVenda
            ValorTotalComissao = ValorTotalComissao + varComissaoVendedor
            print ("====================================================================")
            print ("*** VENDA REGISTRADA " "#" ,cont, " - MOTOROLA G8")
            print ("*** VENDEDOR {0:} - Comissão R${1:.2f}". format (varVendedores[varCodigoVendedor],varComissaoVendedor))
                
        else:
            print ("Código do vendedor")
            print ("Venda não foi registrada")

            continue
    if (laco == 3):
        varCodigoVendedor = int(input("Digite o codigo do vendedor.............:"))
        if (varCodigoVendedor >= 1 and varCodigoVendedor <= 5):
            cont = cont + 1
            varContMarca3 = varContMarca3 + 1
            varFormaPagamento = input ("Pagamento [V] à vista ou [P] parcelado:").upper()
            print ("--------------------------------------------------------------------")
            
            if (varFormaPagamento == "V"):
                porcentagemDesconto = int(input("Porcentagem de desconto a vista :"))
                desconto = varSmartphones['IPHONE 12'] * (porcentagemDesconto / 100)
                ValorVenda = varSmartphones ['IPHONE 12'] - desconto
                ValorTotalVendaVista = ValorTotalVendaVista + ValorVenda
                print ("Preço base............:R$", varSmartphones ['IPHONE 12'])
                print ("Desconto .........: R${:.2f}". format (desconto))
                print ("Venda à vista ......:R$ {:.2f}". format (ValorVenda))
                        
            else:
                ValorVenda = varSmartphones ['IPHONE 12']
                ValorParcela = ValorVenda / 6
                print ("6 parcelas de R${0:.2f} totalizando R${1:.2f}". format (ValorParcela,ValorVenda))
            varComissaoVendedor = ValorVenda * (5/100)
            ValorTotalVendas = ValorTotalVendas + ValorVenda
            ValorTotalComissao = ValorTotalComissao + varComissaoVendedor
            
            print ("====================================================================")
            print ("*** VENDA REGISTRADA ", "#" ,cont, " - IPHONE 12")
            print ("*** VENDEDOR {0:} - Comissão R${1:.2f}". format (varVendedores[varCodigoVendedor],varComissaoVendedor))
                
        else:
            print ("** Código do vendedor **")
            print ("** Venda não foi registrada **")

            continue
    if (laco == 4):
        break
    else:
        continue



    
        
print ("====================================================================")
print ("                  TOTALIZAÇÕES DO DIA                               ")
print ("--------------------------------------------------------------------")
print ("Quantidade Total de Smartphones vendidos:  ", cont)
print ("Quantidade Vendida do SAMSUNG S11 ......: ", varContMarca1)
print ("Quantidade Vendida do MOTOROLA G8 ......: ", varContMarca2)
print ("Quantidade Vendida do IPHONE 12 ......: ", varContMarca3)
print ("--------------------------------------------------------------------")

print ("Soma total das vendas ......: R$ {:.2f}". format (ValorTotalVendas))
print ("Soma das vendas à vista ....: R$ {:.2f}". format (ValorTotalVendaVista))
print ("Soma total paga de comissão : R$ {:.2f}". format (ValorTotalComissao))
print ("====================================================================")
