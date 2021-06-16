def led_board(numero):
    led_patron = {"0":"1111110" , "1":"0110000" , "2":"1101101", "3":"1111001", "4":"0110011", "5":"1011011", "6":"1011111","7":"1110000", "8":"1111111", "9":"1111011"}
    lst_c =[[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "]]
    board_list = ['','','','','']
    dig = str(numero)
    for num in dig:
        
        pat = led_patron[num]
        for i in range(7):
            if i == 0 and pat[i] == "1":
                lst_c[0][0] = lst_c[0][1] = lst_c[0][2] = "#"
            if i == 1 and pat[i] == "1":
                lst_c[0][2] = lst_c[1][2] = lst_c[2][2] = "#"
            if i == 2 and pat[i] == "1":
                lst_c[2][2] = lst_c[3][2] = lst_c[4][2] = "#"
            if i == 3 and pat[i] == "1":
                lst_c[4][0] = lst_c[4][1] = lst_c[4][2] = "#"
            if i == 4 and pat[i] == "1":
                lst_c[4][0] = lst_c[3][0] = lst_c[2][0] = "#"
            if i == 5 and pat[i] == "1":
                lst_c[2][0] = lst_c[1][0] = lst_c[0][0] = "#"
            if i == 6 and pat[i] == "1":
                lst_c[2][0] = lst_c[2][1] = lst_c[2][2] = "#"
        
        for linea in range(len(board_list)):
            board_list[linea] = board_list[linea] + "".join(lst_c[linea]) + " "
        lst_c =[[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "]]

    
        
        
    
    for r in board_list:
        print(r)



led_board(input("Ingrese el numero que desea visualizar en su tablero: "))

